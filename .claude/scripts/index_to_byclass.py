#!/usr/bin/env python3
"""Render a class's case-index.json as one browsable reading list.

Generated output. Never hand-edit; edit case-index.json and regenerate. Every
line is a fact from the index: the reading's name as a wikilink, its kind, the
pages in the edition on the shelf, and the syllabus's own page citation.

Usage:
  index_to_byclass.py --class conlaw
"""
import argparse, datetime, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
WEEKDAY = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
KIND = {"case": "case", "statute": "statute", "rule": "rule",
        "document": "document", "note": "note"}


def readings_dir(ix):
    return ix.get("readings_dir", "10-cases")


def line(ix, r, has_file):
    bits = []
    src = ix["sources"].get(r.get("source"), {})
    if "start" in r:
        bits.append(f"pp. {r['start']}–{r['end']}")
    elif r.get("note"):
        bits.append(r["note"])
    bits.append(KIND.get(r["kind"], r["kind"]))
    if r["kind"] in ("statute", "rule"):
        bits.append("doctrine module, no reading file")
    elif not has_file:
        bits.append("**no file**")
    tail = " · ".join(bits)
    out = f"- [[{r['case']}]] — {tail}"
    if r.get("flag"):
        out += f"\n    - {r['flag']}"
    return out


def build(cls):
    p = os.path.join(VAULT, cls, "99-meta", "case-index.json")
    with open(p) as f:
        ix = json.load(f)
    rdir = os.path.join(VAULT, cls, readings_dir(ix))
    have = {n[:-3] for n in os.listdir(rdir) if n.endswith(".md")}

    L = [f"# {cls} — readings by class", ""]
    ex = ix.get("exam", {})
    L.append(f"{ix.get('course', '')} · {ix.get('professor', '')} · {ix.get('term', '')}")
    if ix.get("meets"):
        L.append(f"Meets {ix['meets']}. {ex.get('format', '')}")
    L.append("")
    L.append(f"Generated {datetime.date.today().isoformat()} from `99-meta/case-index.json`. "
             f"Do not edit; regenerate with `.claude/scripts/index_to_byclass.py --class {cls}`.")
    L.append("")
    src_lines = [f"- `{k.upper()}` — {v['label']}" for k, v in ix.get("sources", {}).items()]
    if src_lines:
        L += ["## Sources", ""] + src_lines + [""]

    part = None
    for s in ix["sessions"]:
        if s.get("part") and s["part"] != part:
            part = s["part"]
            L += [f"## {part}", ""]
        n = s["session"]
        label = "Optional background" if s.get("optional") else f"Class {n}"
        date = ""
        if s.get("date"):
            d = datetime.date.fromisoformat(s["date"])
            date = f" · {WEEKDAY[d.weekday()]} {s['date']}"
        syl = s["readings"][0].get("syllabus_pp") if s["readings"] else None
        syl = f" · syllabus pp. {syl}" if syl else ""
        L.append(f"### {label} — {s['title']}{date}")
        if s.get("note"):
            L.append(f"*{s['note']}*")
        L.append("")
        if not s["readings"]:
            L += ["- *no assigned reading*", ""]
            continue
        for r in s["readings"]:
            L.append(line(ix, r, r["case"] in have))
        L.append("")

    out = os.path.join(VAULT, cls, "99-meta", "by-class.md")
    with open(out, "w") as f:
        f.write("\n".join(L).rstrip() + "\n")
    return out, sum(len(s["readings"]) for s in ix["sessions"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls", required=True)
    a = ap.parse_args()
    out, n = build(a.cls)
    print(f"wrote {os.path.relpath(out, VAULT)} ({n} readings)")


if __name__ == "__main__":
    main()
