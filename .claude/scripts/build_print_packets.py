#!/usr/bin/env python3
"""Build one printable PDF per class meeting from a class's PDF sources.

Deterministic. Reads <class>/99-meta/case-index.json for the syllabus order and
the paginated readings (source + printed start/end), and
<class>/99-meta/print-map.json for everything that has no printed page range
(statutes, rules, Canvas documents). Page ranges are cut straight out of the
source PDFs with qpdf, so the packets are the original scans, not re-typeset
text.

Each packet is:
  1. a cover sheet — class number, title, date, and every reading with its
     source pages and its page numbers inside the packet;
  2. the readings, in syllabus order;
  3. a small grey running label at the top-left of every page
     ("BusOrg · Class 6 · Smith v. Van Gorkom · B&C 120–134 · 7/31"), so a
     dropped stack sorts itself back out.

Also writes "00 - Contents.pdf": every packet, its date, pages and sheets.

A class whose whole assignment was scanned as one PDF can declare it in
print-map.json under "packet_source": {"<session>": {"file": ..., "runs":
[[first,last,offset], ...]}}. The packet body is then those page runs in order,
and the cover lists the readings without per-reading packet pages, since the
scan is already the assignment in syllabus order.

Printed page -> PDF page uses the source's fixed "offset" in case-index.json
(the same one extract_case.py relies on). EPUB sources are refused: an EPUB has
no pages to cut, and Con Law's packets were built from the EPUB separately.

Usage:
  build_print_packets.py --class busorg              # every class
  build_print_packets.py --class busorg --only 6 7   # just these classes
  build_print_packets.py --class busorg --duplex     # blank backs so each reading starts on a fresh sheet
  build_print_packets.py --class busorg --skip-repeats  # don't reprint a case already printed for an earlier class
  build_print_packets.py --class busorg --dry-run    # show the plan, write nothing

Output: <class>/00-source/print/Class NN - <Title>.pdf  (PDFs are gitignored;
regenerate rather than edit).

Requires: qpdf, pdftotext, pdfinfo (poppler), reportlab.
"""
import argparse, datetime, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))

SHORT_CLASS = {"busorg": "BusOrg", "conlaw": "Con Law", "legalfinance": "Legal Finance"}


# ---------------------------------------------------------------- helpers
def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    # qpdf exits 3 for warnings-only (e.g. damaged-but-recoverable xref); accept it.
    if p.returncode not in (0, 3):
        sys.exit(f"command failed: {' '.join(cmd)}\n{p.stderr.strip()}")
    return p.stdout


def page_count(path):
    return int(re.search(r"^Pages:\s+(\d+)", run(["pdfinfo", path]), re.M).group(1))


def page_sizes(path, n):
    out = run(["pdfinfo", "-f", "1", "-l", str(n), path])
    sizes = [(float(w), float(h)) for w, h in
             re.findall(r"^Page\s+\d+\s+size:\s+([\d.]+)\s+x\s+([\d.]+)", out, re.M)]
    return sizes if len(sizes) == n else [(612.0, 792.0)] * n


_TEXT = {}
def page_texts(path):
    """PDF page text, 1-indexed list (index 0 unused). pdftotext splits pages on \\f."""
    if path not in _TEXT:
        _TEXT[path] = [""] + run(["pdftotext", "-layout", path, "-"]).split("\f")
    return _TEXT[path]


def safe(s):
    return re.sub(r'[\\/:*?"<>|]', "", s).strip().rstrip(".")


def dash(a, b):
    return f"{a}" if a == b else f"{a}–{b}"


# ---------------------------------------------------------------- resolve
def locate_sections(srcdir, loc, secs, from_re=None, to_re=None):
    """PDF page span for each statutory section, found by its heading."""
    path = os.path.join(srcdir, loc["file"])
    pages = page_texts(path)
    heads = []
    any_re = re.compile(loc["any"], re.M)
    for i in range(1, len(pages)):
        for m in any_re.finditer(pages[i]):
            heads.append((i, m.start(), m.group(0)))
    spans = []
    for sec in secs:
        want = re.compile(loc["head"].format(sec=re.escape(sec)), re.M)
        k = next((k for k, (pg, pos, txt) in enumerate(heads) if want.match(txt)), None)
        if k is None:
            sys.exit(f"section {sec!r} not found in {loc['file']}")
        first = heads[k][0]
        last = heads[k + 1][0] if k + 1 < len(heads) else len(pages) - 1
        if from_re or to_re:
            text_pages = range(first, last + 1)
            if from_re:
                f = next((p for p in text_pages if re.search(from_re, pages[p], re.M)), None)
                if f is None:
                    sys.exit(f"from_re {from_re!r} not found in § {sec}")
                first = f
            if to_re:
                t = next((p for p in range(first, last + 1) if re.search(to_re, pages[p], re.M)), None)
                if t is None:
                    sys.exit(f"to_re {to_re!r} not found in § {sec}")
                last = t
        spans.append((sec, first, last))
    return path, spans


def resolve(ix, pmap, srcdir, reading):
    """-> list of parts {path, first, last, label}, or (None, reason)."""
    name = reading["case"]
    if "source" in reading:
        src = ix["sources"][reading["source"]]
        path = os.path.join(srcdir, src["file"])
        if path.lower().endswith(".epub"):
            return None, "EPUB source — no pages to cut"
        short = pmap.get("source_short", {}).get(reading["source"], reading["source"].upper())
        return [{"path": path,
                 "first": reading["start"] + src["offset"],
                 "last": reading["end"] + src["offset"],
                 "label": f"{short} {dash(reading['start'], reading['end'])}"}], None

    spec = pmap.get("readings", {}).get(name)
    if not spec:
        return None, "no entry in print-map.json"
    parts = []
    for p in spec:
        if "file" in p:
            path = os.path.join(srcdir, p["file"])
            if not os.path.exists(path):
                return None, f"missing file {p['file']}"
            if "pages" in p:
                a, _, b = str(p["pages"]).partition("-")
                first, last = int(a), int(b or a)
            else:
                first, last = 1, page_count(path)
            label = p.get("label") or os.path.splitext(p["file"])[0]
            parts.append({"path": path, "first": first, "last": last, "label": label})
        else:
            loc = pmap["locators"][p["section_in"]]
            path, spans = locate_sections(srcdir, loc, p["sections"],
                                          p.get("from_re"), p.get("to_re"))
            # merge adjacent/overlapping sections into one run
            spans.sort(key=lambda s: s[1])
            runs = []
            for sec, a, b in spans:
                if runs and a <= runs[-1]["last"] + 1:
                    runs[-1]["last"] = max(runs[-1]["last"], b)
                    runs[-1]["secs"].append(sec)
                else:
                    runs.append({"first": a, "last": b, "secs": [sec]})
            for r in runs:
                label = p.get("label") or (
                    loc["label"].format(sec=r["secs"][0]) if len(r["secs"]) == 1
                    else loc["label"].replace("§ {sec}", "§§ " + ", ".join(r["secs"])))
                parts.append({"path": path, "first": r["first"], "last": r["last"],
                              "label": label})
    return parts, None


# ---------------------------------------------------------------- render
def fmt_date(d):
    if not d:
        return "date TBD"
    return datetime.date.fromisoformat(d).strftime("%A, %B %-d, %Y")


def make_cover(path, course, session, rows, notes, total, duplex):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

    st = {
        "course": ParagraphStyle("c", fontName="Helvetica", fontSize=10, textColor=colors.grey),
        "title": ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=22, leading=26, spaceBefore=6),
        "date": ParagraphStyle("d", fontName="Helvetica", fontSize=12, spaceBefore=4, spaceAfter=14),
        "cell": ParagraphStyle("x", fontName="Helvetica", fontSize=10, leading=12.5),
        "head": ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=9, textColor=colors.grey),
        "note": ParagraphStyle("n", fontName="Helvetica", fontSize=9, leading=11.5, textColor=colors.HexColor("#444444")),
        "foot": ParagraphStyle("f", fontName="Helvetica", fontSize=7.5, textColor=colors.grey),
    }
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    story = [Paragraph(esc(course), st["course"]),
             Paragraph(f"Class {session['session']} — {esc(session['title'])}", st["title"]),
             Paragraph(fmt_date(session.get("date")), st["date"])]
    data = [[Paragraph(h, st["head"]) for h in ("", "Reading", "Source", "Packet pp.")]]
    for i, r in enumerate(rows, 1):
        data.append([Paragraph(str(i), st["cell"]), Paragraph(esc(r["name"]), st["cell"]),
                     Paragraph(esc(r["src"]), st["cell"]), Paragraph(r["pp"], st["cell"])])
    t = Table(data, colWidths=[18, 250, 170, 62], repeatRows=1)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.black),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, colors.HexColor("#cccccc")),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story += [t, Spacer(1, 10)]
    for n in notes:
        story.append(Paragraph("• " + esc(n), st["note"]))
    story += [Spacer(1, 14), Paragraph(
        f"{total} pages{' (duplex: blank backs inserted)' if duplex else ''}. Generated "
        f"{datetime.date.today().isoformat()} by .claude/scripts/build_print_packets.py from "
        f"99-meta/case-index.json and 99-meta/print-map.json. Regenerate rather than edit.",
        st["foot"])]
    if duplex:
        story.append(PageBreak())
        story.append(Spacer(1, 1))
    SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54,
                      topMargin=54, bottomMargin=54, title=f"Class {session['session']}").build(story)


def make_blank(path):
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(path, pagesize=(612, 792)); c.showPage(); c.save()


def make_stamps(path, sizes, labels):
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    c = canvas.Canvas(path)
    for (w, h), lab in zip(sizes, labels):
        c.setPageSize((w, h))
        if lab:
            c.setFont("Helvetica", 7)
            c.setFillColor(colors.HexColor("#777777"))
            c.drawString(22, h - 16, lab)
        c.showPage()
    c.save()


def make_contents(path, course, entries):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    cell = ParagraphStyle("x", fontName="Helvetica", fontSize=9.5, leading=12)
    head = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.grey)
    esc = lambda s: s.replace("&", "&amp;")
    data = [[Paragraph(h, head) for h in ("Class", "Date", "Title", "Readings", "Pages", "Sheets*")]]
    tp = ts = 0
    for e in entries:
        data.append([Paragraph(str(e["n"]), cell), Paragraph(e["date"], cell), Paragraph(esc(e["title"]), cell),
                     Paragraph(str(e["readings"]), cell), Paragraph(str(e["pages"]), cell),
                     Paragraph(str(e["sheets"]), cell)])
        tp += e["pages"]; ts += e["sheets"]
    data.append([Paragraph("<b>Total</b>", cell), "", "", "", Paragraph(f"<b>{tp}</b>", cell),
                 Paragraph(f"<b>{ts}</b>", cell)])
    t = Table(data, colWidths=[36, 70, 220, 56, 50, 50], repeatRows=1)
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.black),
                           ("LINEBELOW", (0, 1), (-1, -2), 0.25, colors.HexColor("#cccccc")),
                           ("LINEABOVE", (0, -1), (-1, -1), 0.6, colors.black),
                           ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story = [Paragraph(f"<b>{esc(course)}</b> — print packets", ParagraphStyle("t", fontName="Helvetica", fontSize=16, spaceAfter=12)),
             t, Spacer(1, 8),
             Paragraph("*Sheets assume double-sided printing of the packet as generated.",
                       ParagraphStyle("n", fontName="Helvetica", fontSize=8, textColor=colors.grey))]
    SimpleDocTemplate(path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54).build(story)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls", required=True)
    ap.add_argument("--only", type=int, nargs="*")
    ap.add_argument("--duplex", action="store_true")
    ap.add_argument("--skip-repeats", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    base = os.path.join(VAULT, a.cls)
    ix = json.load(open(os.path.join(base, "99-meta", "case-index.json")))
    pm_path = os.path.join(base, "99-meta", "print-map.json")
    pmap = json.load(open(pm_path)) if os.path.exists(pm_path) else {}
    srcdir = os.path.join(base, "00-source")
    outdir = os.path.join(srcdir, "print")
    course = f"{pmap.get('course', a.cls)} · {ix.get('professor', '')} · {ix.get('term', '')}"
    tag = SHORT_CLASS.get(a.cls, a.cls)

    printed_before = {}   # (path, first, last) -> class number, for --skip-repeats
    contents, problems = [], []
    tmp = tempfile.mkdtemp()
    blank = os.path.join(tmp, "blank.pdf")
    if not a.dry_run:
        os.makedirs(outdir, exist_ok=True)
        make_blank(blank)

    for s in ix["sessions"]:
        if not s["readings"]:
            continue
        if a.only and s["session"] not in a.only:
            continue
        n = s["session"]
        rows, notes, pieces, labels = [], [], [], []
        seen_pages = {}       # (path, page) -> reading that printed it in this packet
        cursor = 2 + (1 if a.duplex else 0)   # packet page where the next reading starts

        whole = (pmap.get("packet_source") or {}).get(str(n))
        if whole:
            path = os.path.join(srcdir, whole["file"])
            if not os.path.exists(path):
                problems.append(f"Class {n}: missing scan {whole['file']}")
                continue
            runs = whole.get("runs") or [[1, page_count(path), 0]]
            label = whole.get("label", "5th ed. scan")
            span = "; ".join(dash(f + o, l + o) for f, l, o in runs)
            scanned = [r for r in s["readings"] if r.get("source")]
            extra = [r for r in s["readings"] if not r.get("source")]
            for r in scanned:
                rows.append({"name": r["case"], "src": f"{label} {span}", "pp": "in this packet"})
            for f, l, o in runs:
                pieces.append((path, f, l))
                for pg in range(f, l + 1):
                    labels.append(f"{label} · p. {pg + o}")
                cursor += l - f + 1
            # readings outside the scan (Canvas documents) follow it, resolved through print-map
            for r in extra:
                parts, why = resolve(ix, pmap, srcdir, r)
                if parts is None:
                    rows.append({"name": r["case"], "src": "NOT PRINTED", "pp": "—"})
                    notes.append(f"{r['case']}: not printed ({why}).")
                    problems.append(f"Class {n}: {r['case']} — {why}")
                    continue
                start = cursor
                for q in parts:
                    pieces.append((q["path"], q["first"], q["last"]))
                    for _pg in range(q["first"], q["last"] + 1):
                        labels.append(f"{r['case']} · {q['label']}")
                    cursor += q["last"] - q["first"] + 1
                rows.append({"name": r["case"],
                             "src": "; ".join(q["label"] for q in parts),
                             "pp": dash(start, cursor - 1)})
                if a.duplex and (cursor - start) % 2:
                    pieces.append((blank, 1, 1)); labels.append(None); cursor += 1
            notes.append(f"This packet is the 5th-edition scan of the whole assignment ({span}), "
                         f"so the readings run in syllabus order without separate page cuts.")

        for r in (s["readings"] if not whole else []):
            name = r["case"]
            parts, why = resolve(ix, pmap, srcdir, r)
            srcdesc = "; ".join(p["label"] for p in parts) if parts else "—"
            if parts is None:
                rows.append({"name": name, "src": "NOT PRINTED", "pp": "—"})
                notes.append(f"{name}: not printed ({why}).")
                problems.append(f"Class {n}: {name} — {why}")
                continue
            if "skim" in (r.get("note") or "").lower():
                notes.append(f"{name}: skim.")
            key = tuple((p["path"], p["first"], p["last"]) for p in parts)
            if a.skip_repeats and r["kind"] == "case" and key in printed_before:
                rows.append({"name": name, "src": srcdesc, "pp": f"see Class {printed_before[key]}"})
                continue

            start = cursor
            for p in parts:
                fresh = [pg for pg in range(p["first"], p["last"] + 1)
                         if (p["path"], pg) not in seen_pages]
                dup = (p["last"] - p["first"] + 1) - len(fresh)
                if dup:
                    other = seen_pages[(p["path"], next(pg for pg in range(p["first"], p["last"] + 1)
                                                        if (p["path"], pg) in seen_pages))]
                    notes.append(f"{name}: {p['label']} — {dup} page(s) already printed in this packet "
                                 f"with {other}; not repeated.")
                # contiguous runs of fresh pages
                runs = []
                for pg in fresh:
                    if runs and pg == runs[-1][1] + 1:
                        runs[-1][1] = pg
                    else:
                        runs.append([pg, pg])
                for f, l in runs:
                    pieces.append((p["path"], f, l))
                    for pg in range(f, l + 1):
                        seen_pages[(p["path"], pg)] = name
                        labels.append(f"{name} · {p['label']}")
                    cursor += l - f + 1
            end = cursor - 1
            if end < start:
                rows.append({"name": name, "src": srcdesc, "pp": "above"})
                continue
            rows.append({"name": name, "src": srcdesc, "pp": dash(start, end)})
            printed_before.setdefault(key, n)
            if a.duplex and (end - start + 1) % 2:
                pieces.append((blank, 1, 1)); labels.append(None); cursor += 1

        total = cursor - 1
        fname = f"Class {n:02d} - {safe(s['title'])}.pdf"
        date = s.get("date") or ""
        contents.append({"n": n, "date": date, "title": s["title"],
                         "readings": len(s["readings"]), "pages": total,
                         "sheets": (total + 1) // 2})
        print(f"Class {n:>2}  {total:>4} pp  {fname}")
        for row in rows:
            print(f"          {row['pp']:>9}  {row['name']}  [{row['src']}]")
        if a.dry_run:
            continue

        cover = os.path.join(tmp, f"cover{n}.pdf")
        make_cover(cover, course, s, rows, notes, total, a.duplex)
        cover_pages = page_count(cover)
        if cover_pages != (2 if a.duplex else 1):
            problems.append(f"Class {n}: cover ran to {cover_pages} pages; packet page numbers on it are off by {cover_pages - (2 if a.duplex else 1)}")
        cmd = ["qpdf", "--empty", "--pages", cover, f"1-{cover_pages}"]
        for path, f, l in pieces:
            cmd += [path, dash(f, l).replace("–", "-")]
        body = os.path.join(tmp, f"body{n}.pdf")
        run(cmd + ["--", body])

        npages = page_count(body)
        full = [None] * cover_pages + labels
        full = [f"{tag} · Class {n} · {lab} · {i}/{npages}" if lab else None
                for i, lab in enumerate(full, 1)]
        stamps = os.path.join(tmp, f"stamps{n}.pdf")
        make_stamps(stamps, page_sizes(body, npages), full)
        run(["qpdf", body, "--overlay", stamps, "--", os.path.join(outdir, fname)])

    if contents and not a.dry_run and not a.only:
        make_contents(os.path.join(outdir, "00 - Contents.pdf"), course, contents)
    if problems:
        print("\nProblems:")
        for p in problems:
            print("  " + p)
        sys.exit(1)


if __name__ == "__main__":
    main()
