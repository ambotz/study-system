#!/usr/bin/env python3
"""Turn photographed handwritten class notes into a session file's Notes and Signals.

Photos go in `_inbox/<class>/`. One run:

  1. converts each photo to a resized JPEG (macOS `sips`, no model usage),
  2. asks `claude -p` to transcribe the pages into JSON against a fixed schema,
  3. validates the JSON and works out which class meeting the pages belong to,
  4. renders markdown and writes it into the EXISTING placeholder in
     <class>/20-sessions/, filling only an empty `## Notes` section and blank
     Signals lines,
  5. archives the photos and reports what needs a human look.

With --append it instead adds the transcription beneath whatever is already
under `## Notes`, under a dated `### From photographed pages — M/D` heading, so
notes typed in class and notes photographed afterwards can live in one file.
Text already in the section is never rewritten: the new block is only ever
written after the last line you wrote.

It never creates a session file, never touches frontmatter or `## Readings`,
never overwrites content, never commits, and never sets `reconciled`
(CLAUDE.md sections 6 and 7). If anything is ambiguous it stops and writes nothing.

Usage:
  ingest_notes.py                       process every class with photos in its inbox
  ingest_notes.py --class conlaw        one class only
  ingest_notes.py --dry-run             show what would be written; write nothing
  ingest_notes.py --model opus          step up the model if a transcription misses
  ingest_notes.py --class conlaw --from-json out.json
                                        skip the model call and use a saved reply
                                        (testing, or after fixing a bad reply by hand)

Standard library only. Runs on the Mac's system python3 (3.8+).
"""
import argparse
import datetime
import glob
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.abspath(os.path.join(HERE, ".."))


def find_vault():
    """Walk up from this script to the vault root (the folder holding CLAUDE.md and busorg/)."""
    d = HERE
    while True:
        if os.path.isfile(os.path.join(d, "CLAUDE.md")) and os.path.isdir(os.path.join(d, "busorg")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            sys.exit("ERROR: could not find the vault root above %s" % HERE)
        d = parent


VAULT = find_vault()

CLASSES = {
    "busorg": {"prefix": "BusOrg", "professor": "Buccola", "name": "Business Organizations"},
    "conlaw": {"prefix": "ConLaw", "professor": "Baude", "name": "Constitutional Law I"},
}
IMG_EXT = {".heic", ".heif", ".jpg", ".jpeg", ".png"}
MAX_PX = 1800
SIGNAL_KEYS = ["doctrine", "hypo", "pushback", "hard_case", "doesnt_matter", "exam_signal"]
TEXT_BLOCKS = {"heading", "bullet", "numbered", "paragraph"}
CLAUDE_CANDIDATES = [
    "~/.local/bin/claude",
    "~/.claude/local/claude",
    "/opt/homebrew/bin/claude",
    "/usr/local/bin/claude",
]


def die(msg):
    sys.stderr.write("\nERROR: %s\nNothing was written.\n" % msg)
    sys.exit(1)


def natural_key(s):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", s)]


# ---------------------------------------------------------------- vault reading

def read_frontmatter(text):
    lines = text.split("\n")
    fm = {}
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def load_index(cls):
    """Every placeholder in <class>/20-sessions: session number, title, date, readings."""
    entries = []
    for path in sorted(glob.glob(os.path.join(VAULT, cls, "20-sessions", "*.md"))):
        text = open(path, encoding="utf-8").read()
        fm = read_frontmatter(text)
        if not fm.get("session", "").isdigit():
            continue
        readings = []
        in_readings = False
        for line in text.split("\n"):
            if line.startswith("## "):
                in_readings = line.strip() == "## Readings"
                continue
            if in_readings and line.startswith("- ") and line[2:].strip():
                readings.append(line[2:].strip())
        entries.append({
            "session": int(fm["session"]),
            "title": fm.get("title", ""),
            "date": fm.get("date", ""),
            "path": path,
            "readings": readings,
        })
    return entries


def note_stems():
    """Every note name in the vault, the way check_links.py counts them."""
    stems = set()
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")
                   and d not in ("99-templates", "_inbox", "_staging")]
        for f in files:
            if f.endswith(".md") and f != "CLAUDE.md":
                stems.add(f[:-3])
    return stems


def link_targets(cls):
    names = []
    for sub in ("10-cases", "30-doctrine"):
        for path in glob.glob(os.path.join(VAULT, cls, sub, "*.md")):
            names.append(os.path.basename(path)[:-3])
    return sorted(names)


# ---------------------------------------------------------------------- photos

def collect_photos(cls):
    inbox = os.path.join(VAULT, "_inbox", cls)
    if not os.path.isdir(inbox):
        return inbox, []
    files = [f for f in os.listdir(inbox)
             if not f.startswith(".") and os.path.isfile(os.path.join(inbox, f))
             and os.path.splitext(f)[1].lower() in IMG_EXT]
    return inbox, sorted(files, key=natural_key)


def convert_photos(inbox, files):
    """Resized JPEG per photo in <inbox>/_work. Returns {converted name: original name}."""
    work = os.path.join(inbox, "_work")
    if os.path.isdir(work):
        shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work, exist_ok=True)
    sips = shutil.which("sips")
    mapping = {}
    for f in files:
        stem, ext = os.path.splitext(f)
        out_name = stem + ".jpg"
        n = 2
        while out_name in mapping:
            out_name = "%s_%d.jpg" % (stem, n)
            n += 1
        src, dst = os.path.join(inbox, f), os.path.join(work, out_name)
        if sips:
            r = subprocess.run([sips, "-s", "format", "jpeg", "-Z", str(MAX_PX), src, "--out", dst],
                               capture_output=True, text=True)
            if r.returncode != 0 or not os.path.exists(dst):
                die("sips could not convert %s: %s" % (f, (r.stderr or r.stdout).strip()))
        else:
            try:
                from PIL import Image, ImageOps  # optional fallback, not on a stock Mac
                im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
                im.thumbnail((MAX_PX, MAX_PX))
                im.save(dst, "JPEG", quality=85)
            except Exception:
                if ext.lower() in (".jpg", ".jpeg"):
                    shutil.copyfile(src, dst)
                else:
                    die("cannot convert %s here (no `sips`). Run this on the Mac, or "
                        "AirDrop the photo as a JPEG." % f)
        mapping[out_name] = f
    return work, mapping


# ----------------------------------------------------------------------- model

def find_claude():
    found = shutil.which("claude")
    if found:
        return found
    for cand in CLAUDE_CANDIDATES:
        cand = os.path.expanduser(cand)
        if os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
    die("`claude` was not found. Install Claude Code, or add it to PATH, then run again.")


def build_prompt(cls, work, converted, index, targets):
    meta = CLASSES[cls]
    template = open(os.path.join(SKILL, "prompt.md"), encoding="utf-8").read()
    photos = "\n".join("- %s" % os.path.join(work, name) for name in sorted(converted, key=natural_key))
    rows = []
    for e in index:
        rows.append("%d | %s | %s | %s" % (e["session"], e["date"] or "(no date)", e["title"],
                                          "; ".join(e["readings"]) or "no assigned reading"))
    subs = {
        "{{CLASS_NAME}}": meta["name"],
        "{{PROFESSOR}}": meta["professor"],
        "{{PHOTOS}}": photos,
        "{{SESSION_INDEX}}": "\n".join(rows),
        "{{LINK_TARGETS}}": "\n".join(targets) if targets else "(none)",
    }
    for k, v in subs.items():
        template = template.replace(k, v)
    return template


def call_model(prompt, model, inbox):
    claude = find_claude()
    env = dict(os.environ)
    if env.pop("ANTHROPIC_API_KEY", None):
        print("note: ANTHROPIC_API_KEY was set; ignored for this run so usage stays on the Pro plan "
              "(CLAUDE.md section 8).")
    cmd = [claude, "-p", prompt, "--model", model, "--allowedTools", "Read",
           "--output-format", "json", "--max-turns", "20"]
    print("Reading the photos with Claude (%s) — this usually takes a minute or two..." % model)
    try:
        r = subprocess.run(cmd, cwd=VAULT, env=env, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        die("the model call timed out after 15 minutes.")
    raw = r.stdout
    dump = os.path.join(inbox, "_last_model_output.txt")
    with open(dump, "w", encoding="utf-8") as fh:
        fh.write(raw + "\n--- stderr ---\n" + r.stderr)
    if r.returncode != 0:
        detail = r.stderr.strip()[:500]
        try:
            detail = str(json.loads(raw).get("result", detail))[:500]
        except (ValueError, AttributeError):
            pass
        hint = ""
        if "login" in detail.lower():
            hint = ("\n\nClaude Code on this Mac is not signed in. Open Terminal, run `claude`, type "
                    "/login, sign in with your claude.ai account, then run this again.")
        die("`claude -p` exited with status %d: %s%s\n(raw output: %s)"
            % (r.returncode, detail, hint, dump))
    text = raw
    try:
        wrapper = json.loads(raw)
        if isinstance(wrapper, dict) and "result" in wrapper:
            if wrapper.get("is_error"):
                die("`claude -p` reported an error: %s" % str(wrapper.get("result"))[:500])
            text = wrapper["result"]
    except ValueError:
        pass
    return extract_json(text, dump)


def extract_json(text, where):
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    start, end = t.find("{"), t.rfind("}")
    if start == -1 or end == -1:
        die("the model's reply contained no JSON. Raw output is in %s." % where)
    try:
        return json.loads(t[start:end + 1])
    except ValueError as exc:
        die("the model's reply was not valid JSON (%s). Raw output is in %s." % (exc, where))


# ------------------------------------------------------------------ validation

def validate(obj, converted_names):
    problems = []
    if not isinstance(obj, dict) or not isinstance(obj.get("sessions"), list) or not obj["sessions"]:
        die("reply has no `sessions` list.")
    seen_pages = []
    for si, s in enumerate(obj["sessions"]):
        tag = "sessions[%d]" % si
        if not isinstance(s, dict):
            problems.append("%s is not an object" % tag)
            continue
        if not isinstance(s.get("header"), str):
            problems.append("%s.header must be a string" % tag)
        cn = s.get("class_number")
        if cn is not None and not isinstance(cn, int):
            problems.append("%s.class_number must be an integer or null" % tag)
        d = s.get("date")
        if d is not None and not (isinstance(d, str) and re.match(r"^\d{4}-\d{2}-\d{2}$", d)):
            problems.append("%s.date must be YYYY-MM-DD or null" % tag)
        pages = s.get("pages")
        if not (isinstance(pages, list) and pages and all(isinstance(p, str) for p in pages)):
            problems.append("%s.pages must be a non-empty list of file names" % tag)
        else:
            for p in pages:
                if p not in converted_names:
                    problems.append("%s.pages names a photo that is not in the inbox: %s" % (tag, p))
                seen_pages.append(p)
        sig = s.get("signals")
        if not (isinstance(sig, dict) and all(isinstance(sig.get(k), str) and sig.get(k).strip()
                                              for k in SIGNAL_KEYS)):
            problems.append("%s.signals needs all six keys as non-empty strings (use \"—\")" % tag)
        blocks = s.get("blocks")
        if not (isinstance(blocks, list) and blocks):
            problems.append("%s.blocks must be a non-empty list" % tag)
            continue
        for bi, b in enumerate(blocks):
            bt = "%s.blocks[%d]" % (tag, bi)
            if not isinstance(b, dict):
                problems.append("%s is not an object" % bt)
                continue
            typ = b.get("type")
            if typ in TEXT_BLOCKS:
                txt = b.get("text")
                if not (isinstance(txt, str) and txt.strip()):
                    problems.append("%s.text must be a non-empty string" % bt)
                elif re.match(r"^\s*(#|---)", txt):
                    problems.append("%s.text would break the file's heading structure" % bt)
                lvl = b.get("level", 0)
                if typ in ("bullet", "numbered") and lvl not in (0, 1, 2):
                    problems.append("%s.level must be 0, 1 or 2" % bt)
            elif typ == "diagram":
                if b.get("form") not in ("mermaid", "text"):
                    problems.append("%s.form must be mermaid or text" % bt)
                code = b.get("code")
                if not (isinstance(code, str) and code.strip()):
                    problems.append("%s.code must be a non-empty string" % bt)
                elif "```" in code:
                    problems.append("%s.code contains a code fence" % bt)
                elif b.get("form") == "mermaid" and not re.match(r"^\s*(flowchart|graph)\s", code):
                    problems.append("%s mermaid code must start with `flowchart` or `graph`" % bt)
            else:
                problems.append("%s has unknown type %r" % (bt, typ))
    dupes = sorted({p for p in seen_pages if seen_pages.count(p) > 1})
    if dupes:
        problems.append("a photo is assigned to more than one session: %s" % ", ".join(dupes))
    missing = sorted(set(converted_names) - set(seen_pages))
    if missing:
        problems.append("these photos were not assigned to any session: %s" % ", ".join(missing))
    if problems:
        die("the model's reply failed validation:\n  - " + "\n  - ".join(problems))
    return obj["sessions"]


LINK_RE = re.compile(r"\[\[([^\]\|#\n]+)(?:[#\|]([^\]\n]*))?\]\]")


def unwrap_bad_links(text, stems, bad):
    """Keep a wikilink only if its target is a real note; otherwise unwrap to plain text."""
    def fix(m):
        target, alias = m.group(1).strip(), m.group(2)
        if target in stems:
            return m.group(0)
        bad.append(target)
        return alias.strip() if alias else target
    return LINK_RE.sub(fix, text)


# --------------------------------------------------------------------- routing

def resolve(cls, sess, index):
    header = sess.get("header", "")
    cn, date = sess.get("class_number"), sess.get("date")
    if cn is not None:
        hits = [e for e in index if e["session"] == cn]
        if len(hits) != 1:
            die("header %r says class %s, but no single placeholder has that session number." % (header, cn))
        entry = hits[0]
        if date and entry["date"] and entry["date"] != date:
            die("header %r gives %s, but session %d is dated %s in the vault. Check the header."
                % (header, date, cn, entry["date"]))
        return entry
    if date:
        hits = [e for e in index if e["date"] == date]
        if len(hits) == 1:
            return hits[0]
        if not hits:
            die("no %s placeholder is dated %s (header %r). Add the date to the placeholder, or "
                "write \"Class N\" on the page." % (cls, date, header))
        die("more than one %s meeting is dated %s (header %r): %s. Write \"Class N\" on the page."
            % (cls, date, header, ", ".join(str(e["session"]) for e in hits)))
    die("could not tell which meeting the pages headed %r belong to (no class number, no date)." % header)


# ------------------------------------------------------------------- rendering

def render_notes(blocks, photo_links, stems, bad_links):
    out = []

    def sep():
        if out and out[-1] != "":
            out.append("")

    counters = {}
    prev_list = False
    prev_kind = None
    for b in blocks:
        typ = b["type"]
        if typ in ("bullet", "numbered"):
            lvl = b.get("level", 0)
            if not prev_list or (lvl == 0 and prev_kind not in (None, typ)):
                sep()
            if lvl == 0:
                prev_kind = typ
            text = " ".join(unwrap_bad_links(b["text"], stems, bad_links).split())
            indent = "    " * lvl
            if typ == "numbered":
                counters[lvl] = counters.get(lvl, 0) + 1
                for deeper in [k for k in counters if k > lvl]:
                    del counters[deeper]
                out.append("%s%d. %s" % (indent, counters[lvl], text))
            else:
                out.append("%s- %s" % (indent, text))
            prev_list = True
            continue
        prev_list = False
        prev_kind = None
        counters = {}
        sep()
        if typ == "heading":
            out.append("### " + " ".join(unwrap_bad_links(b["text"], stems, bad_links).split()))
            out.append("")
        elif typ == "paragraph":
            out.append(" ".join(unwrap_bad_links(b["text"], stems, bad_links).split()))
        elif typ == "diagram":
            if b.get("title"):
                out.append("**%s**" % " ".join(b["title"].split()))
                out.append("")
            out.append("```" + b["form"])
            out.extend(b["code"].strip("\n").split("\n"))
            out.append("```")
    sep()
    out.append("Source photos: " + ", ".join("[[%s]]" % n for n in photo_links))
    return "\n".join(out)


SIGNAL_RE = re.compile(r"^(\d)\. (\*\*.+?:\*\*)\s*(.*)$")


def apply_to_file(entry, cls, notes_text, signals, stems, bad_links, dry, append=False):
    path = entry["path"]
    text = open(path, encoding="utf-8").read()
    fm = read_frontmatter(text)
    rel = os.path.relpath(path, VAULT)
    if fm.get("class") != cls or fm.get("session") != str(entry["session"]):
        die("%s frontmatter does not match class/session." % rel)
    if fm.get("reconciled", "false").lower() != "false":
        die("%s is already reconciled; refusing to add raw notes to it." % rel)
    lines = text.split("\n")
    try:
        i_notes = lines.index("## Notes")
        i_sig = lines.index("## Signals")
    except ValueError:
        die("%s is missing `## Notes` or `## Signals`." % rel)
    if lines.count("## Notes") != 1 or lines.count("## Signals") != 1 or i_notes > i_sig:
        die("%s has an unexpected section layout." % rel)
    existing = lines[i_notes + 1:i_sig]
    has_content = any(l.strip() for l in existing)
    if has_content and not append:
        die("%s already has content under Notes. Session files are raw capture and are never "
            "overwritten. Rerun with --append to add the new pages beneath what is there, "
            "or empty the section to replace it." % rel)
    tail = lines[i_sig:]
    sig_positions = [(k, SIGNAL_RE.match(l)) for k, l in enumerate(tail)]
    sig_positions = [(k, m) for k, m in sig_positions if m]
    if len(sig_positions) != 6:
        die("%s does not have the six Signals lines." % rel)
    filled = 0
    for k, m in sig_positions:
        n = int(m.group(1))
        if not m.group(3).strip():
            value = " ".join(unwrap_bad_links(signals[SIGNAL_KEYS[n - 1]], stems, bad_links).split())
            tail[k] = "%d. %s %s" % (n, m.group(2), value)
            filled += 1
    if has_content:
        # Keep every line the user wrote, then add the new pages after it.
        kept = existing[:]
        while kept and not kept[-1].strip():
            kept.pop()
        stamp = datetime.date.today().strftime("%-m/%-d") if os.name != "nt" else datetime.date.today().strftime("%m/%d")
        block = ["", "### From photographed pages — %s" % stamp, ""] + notes_text.split("\n")
        new_lines = lines[:i_notes + 1] + kept + block + [""] + tail
    else:
        new_lines = lines[:i_notes + 1] + [""] + notes_text.split("\n") + [""] + tail
    new_text = "\n".join(new_lines)
    # Everything above `## Notes` must be byte-identical.
    head_old, head_new = "\n".join(lines[:i_notes + 1]), "\n".join(new_lines[:i_notes + 1])
    if head_old != head_new:
        die("internal check failed: frontmatter or Readings would change.")
    if not dry:
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(new_text)
        os.replace(tmp, path)
    return filled


# ------------------------------------------------------------------------ main

def run_class(cls, args):
    inbox, files = collect_photos(cls)
    if not files:
        return False
    meta = CLASSES[cls]
    print("\n== %s: %d photo(s) in the inbox ==" % (meta["prefix"], len(files)))
    index = load_index(cls)
    if not index:
        die("no session placeholders found under %s/20-sessions. Run make_session_files.py first." % cls)
    work, converted = convert_photos(inbox, files)
    stems = note_stems()

    if args.from_json:
        obj = json.load(open(args.from_json, encoding="utf-8"))
    else:
        prompt = build_prompt(cls, work, converted, index, link_targets(cls))
        obj = call_model(prompt, args.model, inbox)

    if args.dry_run and args.from_json:
        converted_names = set(p for s in obj.get("sessions", []) for p in s.get("pages", []))
    else:
        converted_names = set(converted)
    sessions = validate(obj, converted_names)

    # Preflight: resolve every session and check every destination before writing anything.
    plan, targets_seen = [], set()
    for s in sessions:
        entry = resolve(cls, s, index)
        if entry["path"] in targets_seen:
            die("two groups of pages both resolve to %s." % os.path.basename(entry["path"]))
        targets_seen.add(entry["path"])
        num = "%02d" % entry["session"]
        photo_names = ["%s %s p%d.jpg" % (meta["prefix"], num, i + 1) for i in range(len(s["pages"]))]
        photos_dir = os.path.join(VAULT, cls, "20-sessions", "_photos")
        for pn in photo_names:
            if os.path.exists(os.path.join(photos_dir, pn)) and not args.dry_run:
                die("%s already exists in _photos; this meeting has been ingested before." % pn)
        plan.append((s, entry, photo_names, photos_dir))

    reports = []
    for s, entry, photo_names, photos_dir in plan:
        bad = []
        notes = render_notes(s["blocks"], photo_names, stems, bad)
        filled = apply_to_file(entry, cls, notes, s["signals"], stems, bad, args.dry_run, args.append)
        if args.dry_run:
            print("\n--- would write into %s ---\n%s\n" % (os.path.relpath(entry["path"], VAULT), notes))
            for k, key in enumerate(SIGNAL_KEYS, 1):
                print("  Signal %d: %s" % (k, s["signals"][key]))
        reports.append({
            "file": os.path.relpath(entry["path"], VAULT),
            "header": s["header"],
            "unsure": notes.count("[?]"),
            "check": notes.count("[check:"),
            "signals_filled": filled,
            "bad_links": sorted(set(bad)),
            "flags": s.get("flags", []),
        })
        if not args.dry_run:
            os.makedirs(photos_dir, exist_ok=True)
            for page, pn in zip(s["pages"], photo_names):
                shutil.copyfile(os.path.join(work, page), os.path.join(photos_dir, pn))

    if not args.dry_run:
        # Everything is written and archived in _photos; only now is the inbox emptied.
        # The original stays in the phone's Photos library.
        for name in files:
            os.remove(os.path.join(inbox, name))
        dump = os.path.join(inbox, "_last_model_output.txt")
        if os.path.exists(dump):
            os.remove(dump)
    shutil.rmtree(work, ignore_errors=True)

    verb = "Would write" if args.dry_run else "Wrote"
    for r in reports:
        print("\n%s %s  (header: %s)" % (verb, r["file"], r["header"]))
        print("  %d word(s) marked [?], %d [check: …] note(s), %d Signals line(s) filled"
              % (r["unsure"], r["check"], r["signals_filled"]))
        for f in r["flags"]:
            if isinstance(f, dict):
                print("  - %s: %s" % (f.get("quote", "?"), f.get("reason", "")))
        if r["bad_links"]:
            print("  links removed because no such note exists: " + ", ".join(r["bad_links"]))
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--class", dest="cls", choices=sorted(CLASSES))
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--append", action="store_true",
                    help="add the transcription beneath notes already under ## Notes, "
                         "under a dated heading, instead of refusing")
    ap.add_argument("--from-json")
    args = ap.parse_args()
    if args.from_json and not args.cls:
        die("--from-json needs --class.")
    classes = [args.cls] if args.cls else sorted(CLASSES)
    did = False
    for cls in classes:
        did = run_class(cls, args) or did
    if not did:
        print("The inbox is empty. AirDrop photos, then drop them into _inbox/busorg/ or _inbox/conlaw/.")
        return
    if not args.dry_run:
        r = subprocess.run([sys.executable, os.path.join(VAULT, ".claude", "scripts", "check_links.py")],
                           capture_output=True, text=True)
        first = r.stdout.strip().split("\n")[0] if r.stdout.strip() else ""
        print("\nLink check: %s" % first)
        if r.returncode != 0:
            print(r.stdout)
        print("\nNext: open the session file(s) in Obsidian, fix anything marked [?], polish as needed, "
              "then commit and push yourself.")


if __name__ == "__main__":
    main()
