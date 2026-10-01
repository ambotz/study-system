#!/usr/bin/env python3
"""Turn wikilinks with no target note into plain italic text.

Obsidian renders a link to a nonexistent note as a dead link. A case the
readings discuss but that has no file of its own should read as an ordinary
case name instead. `[[Myers v. United States]]` becomes `*Myers v. United
States*`; `[[Myers v. United States|Myers]]` becomes `*Myers*`.

Only the body is touched — frontmatter is left alone, as are links already
sitting inside italics. Resolvable links are never changed.

  unlink_dead.py --class conlaw --session-min 5 [--dry-run]
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
LINK = re.compile(r"\[\[([^\]\n]+)\]\]")


def targets(base):
    """Every note name that exists anywhere in the class folder, plus vault root."""
    names = set()
    for root, _dirs, files in os.walk(base):
        if os.sep + "." in root:
            continue
        names |= {f[:-3] for f in files if f.endswith(".md")}
    names |= {f[:-3] for f in os.listdir(VAULT) if f.endswith(".md")}
    return names


def convert(text, have):
    """Replace dead links with italics. Returns (text, [dead targets hit])."""
    hits = []

    def sub(m):
        raw = m.group(1)
        tgt = raw.split("|")[0].split("#")[0].strip()
        if tgt in have:
            return m.group(0)
        shown = raw.split("|", 1)[1].strip() if "|" in raw else tgt
        hits.append(tgt)
        s = m.start()
        # Inside any emphasis run already open on this line? Then the name is
        # emphasised by the surrounding markers and adding more would break them.
        line_start = text.rfind("\n", 0, s) + 1
        bold = italic = False
        i = line_start
        while i < s:
            if text.startswith("**", i):
                bold = not bold
                i += 2
            elif text[i] == "*":
                italic = not italic
                i += 1
            else:
                i += 1
        if bold or italic:
            return shown
        return "*%s*" % shown

    return LINK.sub(sub, text), hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls", required=True)
    ap.add_argument("--session-min", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    base = os.path.join(VAULT, a.cls)
    ix = json.load(open(os.path.join(base, "99-meta", "case-index.json")))
    scope = set()
    for s in ix["sessions"]:
        if s["session"] < a.session_min:
            continue
        for r in s["readings"]:
            p = os.path.join(base, "10-cases", r["case"] + ".md")
            if os.path.exists(p):
                scope.add(p)

    have = targets(base)
    changed = total = 0
    for p in sorted(scope):
        src = open(p, encoding="utf-8").read()
        if src.startswith("---"):
            _, fm, body = src.split("---", 2)
            head = "---" + fm + "---"
        else:
            head, body = "", src
        new, hits = convert(body, have)
        if not hits:
            continue
        changed += 1
        total += len(hits)
        print("%-52s %2d  %s" % (os.path.basename(p)[:-3][:52], len(hits),
                                 ", ".join(sorted(set(hits))[:3])))
        if not a.dry_run:
            open(p, "w", encoding="utf-8").write(head + new)
    print("\n%s %d dead link(s) in %d file(s)" %
          ("would rewrite" if a.dry_run else "rewrote", total, changed))


if __name__ == "__main__":
    main()
