#!/usr/bin/env python3
"""Create one placeholder session file per class meeting in <class>/20-sessions/.

Deterministic. Reads <class>/99-meta/case-index.json and writes, for every
class meeting, a file named by class number:

    busorg/20-sessions/BusOrg 06 - Modern Deference.md
    conlaw/20-sessions/ConLaw 06 - Appointment & Removal.md
    legalfinance/20-sessions/LegalFin 04 - Champerty, usury and legal ethics.md

Legal Finance meets once a week, so its files are one per weekly seminar, titled
by that week's 10-readings folder. Its Signals are seminar prompts (arguments,
structures, deal work, paper), not exam prompts, and it has no `reconciled`
flag because that class has no reconcile pass (legalfinance/CLAUDE.md).

The class prefix keeps note names unique vault-wide, which Obsidian wikilinks
need. Each file carries script-written frontmatter, the day's readings as
wikilinks (statutes link to the doctrine module that carries them), and the
two capture sections: raw Notes, then the six Signals.

NEVER overwrites. A session file is raw capture; once it exists this script
leaves it alone, so it is safe to rerun after the syllabus changes (new
meetings get files, existing ones are untouched).

Usage:
  make_session_files.py --class busorg
  make_session_files.py --class conlaw --dry-run
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from index_to_byclass import module_index, modules_for  # noqa: E402

PREFIX = {"busorg": "BusOrg", "conlaw": "ConLaw", "legalfinance": "LegalFin"}
PROFESSOR = {"busorg": "Buccola", "conlaw": "Baude", "legalfinance": "Kelley"}

EXAM_SIGNALS = [
    "Doctrine on the table",
    "Hypo, and what he was fishing for",
    "Pushback on a student",
    "What he called the hard case",
    "What he said doesn't matter",
    "Exam signal",
]
SEMINAR_SIGNALS = [
    "Questions on the table",
    "What Kelley or the guest pushed on, and what got rewarded",
    "Arguments that moved me (which position files)",
    "Structures or mechanics explained (which concept files)",
    "Deal / assignment relevance",
    "Paper idea",
]
SIGNALS = {"busorg": EXAM_SIGNALS, "conlaw": EXAM_SIGNALS, "legalfinance": SEMINAR_SIGNALS}


def q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def safe(s):
    return re.sub(r'[\\/:*?"<>|#^\[\]]', "", s).strip().rstrip(".")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls", required=True, choices=sorted(PREFIX))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    base = os.path.join(VAULT, a.cls)
    ix = json.load(open(os.path.join(base, "99-meta", "case-index.json")))
    midx = module_index(a.cls) if os.path.isdir(os.path.join(base, "30-doctrine")) else {}
    reading_dir = os.path.join(base, ix.get("readings_dir", "10-cases"))
    notes = {os.path.splitext(f)[0] for _, _, fs in os.walk(reading_dir) for f in fs}
    week_dirs = {}
    for d in (os.listdir(reading_dir) if os.path.isdir(reading_dir) else []):
        m = re.match(r"(\d+) - (.+)", d)
        if m and os.path.isdir(os.path.join(reading_dir, d)):
            week_dirs[int(m.group(1))] = m.group(2)
    outdir = os.path.join(base, "20-sessions")
    prof = PROFESSOR[a.cls]
    made = skipped = 0

    for s in ix["sessions"]:
        n = s["session"]
        if n == 0:          # optional pre-quarter background, not a class meeting
            continue
        short = week_dirs.get(n, s["title"])
        fname = f"{PREFIX[a.cls]} {n:02d} - {safe(short)}.md"
        path = os.path.join(outdir, fname)
        if os.path.exists(path):
            skipped += 1
            continue

        links = []
        for r in s["readings"]:
            if r["kind"] in ("statute", "rule"):
                mods = modules_for(r, midx)
                links.append(f"{r['case']} → " + ", ".join(f"[[{m}]]" for m in mods) if mods else r["case"])
            elif r.get("file") and r["file"] in notes:
                links.append(f"[[{r['file']}]]")
            elif r["case"] in notes:
                links.append(f"[[{r['case']}]]")
            else:
                links.append(f"{r.get('file') or r['case']} *(no reading file yet)*")

        fm = ["---",
              f"class: {a.cls}",
              f"session: {n}",
              f"title: {q(s['title'])}",
              f"date: {s['date'] if s.get('date') else ''}",
              f"professor: {prof}"]
        if a.cls != "legalfinance":
            fm.append("reconciled: false")
        fm += ["---", ""]
        body = [f"# {PREFIX[a.cls]} {n} — {short}", "", "## Readings", ""]
        body += [f"- {l}" for l in links] or ["- *no assigned reading*"]
        body += ["", "## Notes", "", "", "## Signals", ""]
        body += [f"{i}. **{p}:** " for i, p in enumerate(SIGNALS[a.cls], 1)]
        body += [""]
        text = "\n".join(fm + body)

        print(("would write " if a.dry_run else "wrote ") + fname)
        if not a.dry_run:
            os.makedirs(outdir, exist_ok=True)
            with open(path, "w") as f:
                f.write(text)
        made += 1

    print(f"\n{a.cls}: {made} {'to create' if a.dry_run else 'created'}, {skipped} already existed (untouched)")


if __name__ == "__main__":
    main()
