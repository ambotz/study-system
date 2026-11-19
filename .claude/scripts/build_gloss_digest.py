#!/usr/bin/env python3
"""Compile a read-through digest from a class's doctrine modules.

Per module: the governing provision, the first sentence of the Rule statement
(the baseline), the Professor gloss (what the professor actually did with it),
and the Common trap (the wrong answer that sounds right). Ordered by
professor_emphasis, then exam_likelihood.

    python3 .claude/scripts/build_gloss_digest.py conlaw --out <file>

The digest is generated. Anything above the GENERATED marker in the output file
is preserved on rebuild, so a hand-written synthesis survives.
"""
import argparse, datetime as dt, pathlib, re, sys

MARK = "<!-- GENERATED BELOW — rebuilt by build_gloss_digest.py; edits here are discarded -->"
RANK = {"high": 0, "medium": 1, "low": 2}


def sec(text, name):
    i = text.find(f"## {name}")
    if i == -1:
        return ""
    nxt = text.find("\n## ", i + 3)
    return (text[i + len(name) + 3: nxt] if nxt != -1 else text[i + len(name) + 3:]).strip()


def first_sentence(s):
    s = " ".join(s.split())
    m = re.search(r"(?<=[.!?])\s+(?=[A-Z])", s)
    return s[: m.start()] if m else s


def key(text):
    e = re.search(r"^professor_emphasis:\s*(\d)", text, re.M)
    l = re.search(r"^exam_likelihood:\s*(\S+)", text, re.M)
    return (-(int(e.group(1)) if e else 0), RANK.get(l.group(1) if l else "", 3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("klass")
    ap.add_argument("--out", required=True)
    ap.add_argument("--trap-bullets", type=int, default=3)
    args = ap.parse_args()

    mods = sorted(pathlib.Path(args.klass, "30-doctrine").glob("*.md"),
                  key=lambda p: key(p.read_text(errors="replace")))
    out, n = [], 0
    for p in mods:
        t = p.read_text(errors="replace")
        gloss = sec(t, "Professor gloss")
        if not gloss:
            continue
        n += 1
        e = re.search(r"^professor_emphasis:\s*(\d)", t, re.M)
        l = re.search(r"^exam_likelihood:\s*(\S+)", t, re.M)
        sub = re.search(r"^sub_topic:\s*(.*)$", t, re.M)
        trap = [ln for ln in sec(t, "Common trap").splitlines() if ln.strip().startswith("-")]
        out += [f"## {p.stem}", "",
                f"`{e.group(1) if e else '?'}/{l.group(1) if l else '?'}` · {sub.group(1).strip() if sub else ''}", "",
                "**Baseline.** " + first_sentence(sec(t, "Rule statement")), "",
                "**Gloss.** " + " ".join(gloss.split()), ""]
        if trap:
            out += ["**Traps.**", ""] + trap[: args.trap_bullets] + [""]
        out += [f"→ [[{p.stem}]]", "", "---", ""]

    body = MARK + "\n\n" + f"*{n} modules, compiled {dt.date.today().isoformat()}.*\n\n" + "\n".join(out)
    dest = pathlib.Path(args.out)
    head = ""
    if dest.exists():
        prev = dest.read_text()
        head = prev.split(MARK)[0] if MARK in prev else ""
    dest.write_text(head + body)
    print(f"{dest}: {n} modules")


if __name__ == "__main__":
    sys.exit(main())
