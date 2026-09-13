#!/usr/bin/env python3
"""Extract one case's text from the BusOrg source PDFs.

Deterministic. Takes a case name, looks up its source and printed page range in
case-index.json, converts printed pages to PDF pages using that source's fixed
offset, and shells out to pdftotext.

The offsets are a property of the PDFs, not a guess: every sampled page in the
Badawi & Casey scan prints a page number exactly 6 less than its PDF index, and
the case pack prints page numbers equal to its PDF index. Verified across pages
13, 37, 43, 50, 120, 200, 400 and 700.

Usage:
  extract_case.py --list
  extract_case.py --session 6
  extract_case.py "Smith v. Van Gorkom"
  extract_case.py "Smith v. Van Gorkom" --out /tmp/vangorkom.txt
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
INDEX = os.path.join(VAULT, "busorg", "99-meta", "case-index.json")
SRCDIR = os.path.join(VAULT, "busorg", "00-source")


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


def extract(ix, reading):
    if "source" not in reading:
        sys.exit(
            f"{reading['case']!r} is a {reading['kind']}, not a paginated case "
            f"reading. Note: {reading.get('note', 'see 00-source')}"
        )
    src = ix["sources"][reading["source"]]
    path = os.path.join(SRCDIR, src["file"])
    if not os.path.exists(path):
        sys.exit(f"Source PDF missing: {path}")
    first = reading["start"] + src["offset"]
    last = reading["end"] + src["offset"]
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
    a = ap.parse_args()
    ix = load()

    if a.list:
        for s in ix["sessions"]:
            print(f"\n{s['session']:>2}. {s['date']}  {s['title']}")
            for r in s["readings"]:
                loc = (f"[{r['source']} {r['start']}-{r['end']}]"
                       if "source" in r else f"[{r['kind']}]")
                print(f"      {r['case']}  {loc}")
        return

    if a.session:
        s = next((x for x in ix["sessions"] if x["session"] == a.session), None)
        if not s:
            sys.exit(f"No session {a.session}")
        parts = [extract(ix, r) for r in s["readings"] if "source" in r]
        text = "\n\n".join(parts)
    elif a.case:
        text = extract(ix, find(ix, a.case)[1])
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
