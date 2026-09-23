#!/usr/bin/env python3
"""Render a class's case-index.json as one browsable reading list.

Generated output. Never hand-edit; edit case-index.json and regenerate. Every
line is a fact from the index: the reading's name as a wikilink, its kind, the
pages in the edition on the shelf, and the syllabus's own page citation.

Usage:
  index_to_byclass.py --class conlaw
"""
import argparse, datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))
WEEKDAY = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
KIND = {"case": "case", "statute": "statute", "rule": "rule",
        "document": "document", "note": "note"}


def readings_dir(ix):
    return ix.get("readings_dir", "10-cases")


ACCESS = {"open": "open", "paywalled": "paywalled", "canvas": "Canvas only",
          "handout": "handout"}
SPEAKER = {"funder": "funder", "claimholder": "claimholder",
           "defense_side": "defence side", "practitioner": "practitioner",
           "academic": "academic", "government": "government", "press": "press"}
BLOCKED = ("canvas", "handout")


SEC_RE = re.compile(r"(?:§+\s*)?(\d+(?:\.\d+)?[A-Za-z]?)((?:\s*\([^)]+\))*)")
RULE_RE = re.compile(r"\b(1[34][a-d](?:-\d+)?)\b", re.I)


NOISE = [re.compile(x, re.I) for x in (
    r"\b\d+\s+Del\.\s*C\.", r"\bDel\.\s*C\.", r"\bDel\.\s*Ct\.\s*Ch\.",
    r"\((?:pre|post)[^)]*\)", r"\bSB\s*\d+", r"\b(?:18|19|20)\d\d\b",
    r"\bRestatement\s*\((?:Second|Third)\)", r"\beffective[^,;)]*",
)]


def sections(text):
    """Citation tokens: a bare section, each of its subsections, and SEC rule ids.

    "8 Del. C. 144(a),(d)(6)" gives 144, 144(a) and 144(d)(6). A section cited
    without subsections gives only the bare number, which matches any
    subsection of it; a section cited with subsections does not match a module
    that cites a different subsection.
    """
    for pat in NOISE:
        text = pat.sub(" ", text)
    bare, subs, rules = set(), set(), set()
    for m in SEC_RE.finditer(text):
        base, tail = m.group(1), m.group(2) or ""
        parts = re.findall(r"\(([^)]+)\)", tail)
        if parts:
            subs.update(f"{base}({x})" for x in parts)
        else:
            bare.add(base)
    rules.update(r.lower() for r in RULE_RE.findall(text))
    return bare, subs, rules


def module_index(cls):
    """Doctrine module name -> the citation tokens in its authority field."""
    d = os.path.join(VAULT, cls, "30-doctrine")
    if not os.path.isdir(d):
        return {}
    idx = {}
    for n in sorted(os.listdir(d)):
        if not n.endswith(".md"):
            continue
        text = open(os.path.join(d, n)).read()
        if not text.startswith("---\n"):
            continue
        head = text[4:].split("\n---\n", 1)[0]
        auth, keep = [], False
        for ln in head.split("\n"):
            if ln.startswith("authority:"):
                keep = True
                continue
            if keep and ln.startswith("  - "):
                auth.append(ln[4:].strip())
            elif keep and not ln.startswith(" "):
                break
        idx[n[:-3]] = sections(" ; ".join(auth))
    return idx


def rule_hit(a, b):
    return any(x == y or x.startswith(y) or y.startswith(x) for x in a for y in b)


def modules_for(r, midx):
    """Modules whose authority covers this provision, closest match first.

    A subsection match outranks a match on the section as a whole, and a
    provision cited with subsections never matches on the bare number alone.
    """
    bare, subs, rules = sections(r["case"])
    hits = []
    for name, (mbare, msubs, mrules) in midx.items():
        if subs & msubs:
            score = 3
        elif subs and {t.split("(")[0] for t in subs} & mbare:
            score = 2
        elif bare & (mbare | {t.split("(")[0] for t in msubs}):
            score = 2
        elif rules and rule_hit(rules, mrules):
            score = 1
        else:
            continue
        hits.append((-score, name))
    return [n for _s, n in sorted(hits)][:3]


def stem(r):
    """The note's filename: the short form where the index gives one, and never
    the '(redux)' suffix, which marks a second assignment of one file."""
    return re.sub(r"\s*\(redux\)$", "", r.get("file") or r["case"])


def line(ix, r, style, have, midx=None):
    name = stem(r)
    label = r["case"] if r["case"] != name else None
    link = f"[[{name}|{label}]]" if label else f"[[{name}]]"
    bits = []
    if "start" in r:
        bits.append(f"pp. {r['start']}–{r['end']}")
    bits.append(KIND.get(r["kind"], r["kind"]))
    if style == "links":
        if r.get("speaker"):
            bits.append(SPEAKER.get(r["speaker"], r["speaker"]))
        bits.append(ACCESS.get(r.get("access", ""), r.get("access", "")))
    elif "start" not in r and r.get("note"):
        bits.insert(0, r["note"])
    mods = []
    if r["kind"] in ("statute", "rule"):
        mods = modules_for(r, midx or {})
        bits.append("doctrine module, no reading file" if not mods else "doctrine module")
    elif name not in have:
        bits.append("**no file**" if r.get("access") not in BLOCKED else "not retrievable")
    out = f"- {link} — " + " · ".join(b for b in bits if b)
    for m in mods:
        out += f"\n    - → [[{m}]]"
    if r.get("url"):
        out += f"\n    - {r['url']}"
    if r.get("flag"):
        out += f"\n    - {r['flag']}"
    elif style == "links" and r.get("note"):
        out += f"\n    - {r['note']}"
    return out


def build(cls):
    p = os.path.join(VAULT, cls, "99-meta", "case-index.json")
    with open(p) as f:
        ix = json.load(f)
    rdir = os.path.join(VAULT, cls, readings_dir(ix))
    have = set()
    for root, _d, files in os.walk(rdir):
        have.update(n[:-3] for n in files if n.endswith(".md"))
    style = ix.get("style", "pages")
    midx = module_index(cls)

    L = [f"# {cls} — readings by class", ""]
    ex = ix.get("exam", {})
    L.append(" · ".join(x for x in (ix.get("course"), ix.get("professor"),
                                     ix.get("term")) if x))
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
            L.append(line(ix, r, style, have, midx))
        L.append("")

    if ix.get("assignments"):
        L += ["## Graded deliverables", ""]
        for a in ix["assignments"]:
            L.append(f"- **{a['due']} — {a['title']}**"
                     + (f" ({a['weight']})" if a.get("weight") else ""))
            if a.get("detail"):
                L.append(f"    - {a['detail']}")
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
