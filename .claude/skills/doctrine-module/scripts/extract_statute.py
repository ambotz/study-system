#!/usr/bin/env python3
"""Pull the text of one statutory section, rule, or Exchange Act section.

Deterministic. Finds the section's heading in the right source document and
returns everything up to the next heading. Never paraphrases, never summarises.

Sources and their heading forms, all verified against the files in 00-source:

  dgcl      DCGL 8 Full.pdf            "§ 141 Board of directors..."
  dgcl144pre / dgcl144post             standalone pre/post SB 21 extracts
  dgcl220pre / dgcl220post             standalone pre/post SB 21 extracts
  sb21                                 SB 21 Redline.pdf (whole document)
  chancery  chancery rules 2026.pdf    "Rule 23.1. Derivative Actions..."
  sea34     sea1934.pdf                "SEC. 13. (a) Every issuer..."

Usage:
  extract_statute.py 141                     # DGCL section, whole
  extract_statute.py 141 --sub a             # only subsection (a)
  extract_statute.py 144 --source dgcl144pre
  extract_statute.py 144 --source dgcl144post
  extract_statute.py 23.1 --source chancery
  extract_statute.py 14 --source sea34
  extract_statute.py --list                  # every DGCL heading found
"""
import argparse, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SRC = os.path.join(VAULT, "busorg", "00-source")

SOURCES = {
    "dgcl":        ("DCGL 8 Full.pdf",            r"^§\s*{sec}\s+\S", r"^§\s*\d+[A-Z]?\s+\S"),
    "chancery":    ("chancery rules 2026.pdf",    r"^\s*Rule\s+{sec}\.\s+\S", r"^\s*Rule\s+\d+(\.\d+)?\.\s+\S"),
    "sea34":       ("sea1934.pdf",                r"^\s*SEC\.\s*{sec}\.", r"^\s*SEC\.\s*\d+[A-Z]?\."),
    "dgcl144pre":  ("8 Del. C. 144 (pre-SB 21).pdf",  None, None),
    "dgcl144post": ("8 Del. C. 144 post-SB 21).pdf",  None, None),
    "dgcl220pre":  ("8 Del. C. 220 (pre-SB 21).pdf",  None, None),
    "dgcl220post": ("8 Del. C. 220 (post-SB 21).pdf", None, None),
    "sb21":        ("SB 21 Redline.pdf",              None, None),
}


def text(key):
    fn = SOURCES[key][0]
    path = os.path.join(SRC, fn)
    if not os.path.exists(path):
        sys.exit(f"Source missing: {path}")
    out = subprocess.run(["pdftotext", "-layout", path, "-"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"pdftotext failed on {fn}: {out.stderr.strip()}")
    return out.stdout


def section(key, sec):
    body = text(key)
    _, head_tpl, any_head = SOURCES[key]
    if head_tpl is None:          # whole-document source
        return body
    start_re = re.compile(head_tpl.format(sec=re.escape(sec)), re.M)
    m = start_re.search(body)
    if not m:
        sys.exit(f"Section {sec!r} not found in {SOURCES[key][0]}. Try --list.")
    rest = body[m.start():]
    nxt = re.compile(any_head, re.M)
    n = nxt.search(rest, pos=1)
    return rest[:n.start()] if n else rest


def subsection(block, sub):
    """Return just subsection (sub) — e.g. 'a' or 'b'(2) written as 'b'."""
    pat = re.compile(r"^\s*(?:---)?\(%s\)" % re.escape(sub), re.M)
    m = pat.search(block)
    if not m:
        sys.exit(f"Subsection ({sub}) not found in this section.")
    rest = block[m.start():]
    nxt = re.compile(r"^\s*(?:---)?\([a-z]\)", re.M).search(rest, pos=1)
    return rest[:nxt.start()] if nxt else rest


def clean(s):
    s = s.replace("---", "")
    s = re.sub(r"^\s*Title 8 - Corporations\s*$", "", s, flags=re.M)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("section", nargs="?")
    ap.add_argument("--source", default="dgcl", choices=sorted(SOURCES))
    ap.add_argument("--sub")
    ap.add_argument("--raw", action="store_true", help="skip whitespace cleanup")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list:
        body = text(a.source)
        pat = SOURCES[a.source][2]
        if not pat:
            sys.exit(f"{a.source} is a whole-document source; no headings to list.")
        for m in re.finditer(pat[:-3] + r".{0,70}", body, re.M):
            print(" ", m.group(0).strip())
        return

    if not a.section:
        sys.exit("Give a section number, or --list.")

    block = section(a.source, a.section)
    if a.sub:
        block = subsection(block, a.sub)
    print(block if a.raw else clean(block))


if __name__ == "__main__":
    main()
