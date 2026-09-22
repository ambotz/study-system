#!/usr/bin/env python3
"""Extract one reading's text from a class's paginated source.

Deterministic. Takes a case name, looks up its source and printed page range in
case-index.json, converts printed pages to PDF pages using that source's fixed
offset, and shells out to pdftotext.

The offsets are a property of the PDFs, not a guess: every sampled page in the
Badawi & Casey scan prints a page number exactly 6 less than its PDF index, and
the case pack prints page numbers equal to its PDF index. Verified across pages
13, 37, 43, 50, 120, 200, 400 and 700.

EPUB sources carry the print edition's page numbers as embedded page-break
markers (<span epub:type="pagebreak" title="N">), so for an EPUB the printed
page is the EPUB page and the offset is null. Con Law's 4th-ed. casebook is one.

Usage:
  extract_case.py --class conlaw "Gundy v. United States" --plus 1
  extract_case.py --list
  extract_case.py --session 6
  extract_case.py "Smith v. Van Gorkom"
  extract_case.py "Smith v. Van Gorkom" --out /tmp/vangorkom.txt
"""
import argparse, html, json, os, re, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
INDEX = os.path.join(VAULT, "busorg", "99-meta", "case-index.json")
SRCDIR = os.path.join(VAULT, "busorg", "00-source")


def set_class(cls):
    global INDEX, SRCDIR
    INDEX = os.path.join(VAULT, cls, "99-meta", "case-index.json")
    SRCDIR = os.path.join(VAULT, cls, "00-source")


_EPUB = {}
_PB = re.compile(r'<span[^>]*epub:type="pagebreak"[^>]*title="([^"]+)"[^>]*>(?:</span>)?')


def epub_pages(path):
    """Printed page label -> text, split on the embedded page-break markers."""
    if path in _EPUB:
        return _EPUB[path]
    z = zipfile.ZipFile(path)
    names = z.namelist()
    opf_name = next(n for n in names if n.endswith(".opf"))
    opf = z.read(opf_name).decode("utf-8")
    base = os.path.dirname(opf_name)
    href = {}
    for tag in re.findall(r"<item\b[^>]*>", opf):
        i = re.search(r'\bid="([^"]+)"', tag)
        h = re.search(r'\bhref="([^"]+)"', tag)
        if i and h:
            href[i.group(1)] = h.group(1)
    pages, cur, buf = {}, "front", []
    for idref in re.findall(r'<itemref\b[^>]*idref="([^"]+)"', opf):
        doc = z.read(os.path.join(base, href[idref]).lstrip("/")).decode("utf-8")
        doc = re.sub(r"(?is)<head.*?</head>", "", doc)
        pieces = _PB.split(doc)
        # split() alternates text, label, text, label ...
        for k, piece in enumerate(pieces):
            if k % 2 == 1:
                pages.setdefault(cur, []).append("".join(buf)); buf = []
                cur = piece
                continue
            t = re.sub(r"(?i)</p>|<br\s*/?>|</h\d>|</li>", "\n", piece)
            t = html.unescape(re.sub(r"<[^>]+>", "", t))
            buf.append(t)
    pages.setdefault(cur, []).append("".join(buf))
    out = {k: re.sub(r"\n{3,}", "\n\n", "".join(v)).strip() for k, v in pages.items()}
    _EPUB[path] = out
    return out


def load():
    with open(INDEX) as f:
        return json.load(f)


def readings(ix):
    for s in ix["sessions"]:
        for r in s["readings"]:
            yield s, r


def find(ix, name):
    name_l = name.lower()
    exact = [(s, r) for s, r in readings(ix) if r["case"].lower() == name_l]
    if exact:
        return exact[0]
    part = [(s, r) for s, r in readings(ix) if name_l in r["case"].lower()]
    if len(part) == 1:
        return part[0]
    if not part:
        sys.exit(f"No reading matches {name!r}. Try --list.")
    sys.exit("Ambiguous. Matches:\n  " + "\n  ".join(r["case"] for _, r in part))


def extract(ix, reading, plus=0):
    if "source" not in reading:
        sys.exit(
            f"{reading['case']!r} is a {reading['kind']}, not a paginated case "
            f"reading. Note: {reading.get('note', 'see 00-source')}"
        )
    src = ix["sources"][reading["source"]]
    path = os.path.join(SRCDIR, src["file"])
    if not os.path.exists(path):
        sys.exit(f"Source PDF missing: {path}")
    if path.lower().endswith(".epub"):
        pg = epub_pages(path)
        first, last = reading["start"], reading["end"] + plus
        body = "\n\n".join(f"[p. {n}]\n{pg[str(n)]}" for n in range(first, last + 1)
                            if str(n) in pg)
        return (f"# {reading['case']}\n# source: {src['label']}\n"
                f"# printed pages {first}-{last} (epub page markers)\n\n{body}\n")
    first = reading["start"] + src["offset"]
    last = reading["end"] + src["offset"] + plus
    out = subprocess.run(
        ["pdftotext", "-layout", "-f", str(first), "-l", str(last), path, "-"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        sys.exit(f"pdftotext failed: {out.stderr.strip()}")
    header = (
        f"# {reading['case']}\n"
        f"# source: {src['label']}\n"
        f"# printed pages {reading['start']}-{reading['end']} "
        f"(pdf pages {first}-{last})\n\n"
    )
    return header + out.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("case", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--session", type=int)
    ap.add_argument("--out")
    ap.add_argument("--class", dest="cls", default="busorg")
    ap.add_argument("--plus", type=int, default=0,
                    help="extra pages past the end of the range (procedure step 2)")
    a = ap.parse_args()
    set_class(a.cls)
    ix = load()

    if a.list:
        for s in ix["sessions"]:
            print(f"\n{s['session']:>2}. {s['date'] or 'TBD'}  {s['title']}")
            for r in s["readings"]:
                loc = (f"[{r['source']} {r['start']}-{r['end']}]"
                       if "source" in r else f"[{r['kind']}]")
                print(f"      {r['case']}  {loc}")
        return

    if a.session is not None:
        s = next((x for x in ix["sessions"] if x["session"] == a.session), None)
        if not s:
            sys.exit(f"No session {a.session}")
        parts = [extract(ix, r, a.plus) for r in s["readings"] if "source" in r]
        text = "\n\n".join(parts)
    elif a.case:
        text = extract(ix, find(ix, a.case)[1], a.plus)
    else:
        sys.exit("Give a case name, --session N, or --list.")

    if a.out:
        with open(a.out, "w") as f:
            f.write(text)
        print(f"wrote {len(text)} chars -> {a.out}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
