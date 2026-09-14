#!/usr/bin/env python3
"""Render a class's case-index.json as a browsable workbook.

Generated output. Never hand-edit the workbook — edit case-index.json and
regenerate. The workbook carries no formulas: every column is either a fact from
the syllabus or a fact about the filesystem, so there is nothing for a
spreadsheet to compute.

Usage:
  index_to_xlsx.py                 # all classes that have an index
  index_to_xlsx.py --class busorg
"""
import argparse, datetime, json, os, re, sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, "..", ".."))

FONT = "Arial"
HEAD_FILL = PatternFill("solid", fgColor="1F3864")
HEAD_FONT = Font(name=FONT, size=10, bold=True, color="FFFFFF")
BODY = Font(name=FONT, size=10)
BODY_DIM = Font(name=FONT, size=10, color="808080")
TITLE = Font(name=FONT, size=14, bold=True)
BAND = PatternFill("solid", fgColor="F2F2F2")
THIN = Side(style="thin", color="D9D9D9")
EDGE = Border(bottom=THIN)

KIND_LABEL = {
    "case": "Case",
    "statute": "Statute",
    "rule": "Rule",
    "document": "Document",
    "note": "Note",
}
WEEKDAY = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def autosize(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def header_row(ws, row, labels):
    for i, label in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=label)
        c.fill, c.font = HEAD_FILL, HEAD_FONT
        c.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 28


def build(cls, ix, out):
    wb = Workbook()

    # ---------- Readings ----------
    ws = wb.active
    ws.title = "Readings"
    ws["A1"] = f"{cls} — {ix.get('professor', '')}, {ix.get('term', '')}"
    ws["A1"].font = TITLE
    exam = ix.get("exam", {})
    ws["A2"] = f"Exam: {exam.get('date','')} {exam.get('time','')} — {exam.get('format','')}"
    ws["A2"].font = BODY_DIM
    ws["A3"] = f"Generated {datetime.date.today().isoformat()} from 99-meta/case-index.json. Do not edit; regenerate."
    ws["A3"].font = BODY_DIM

    cols = ["Session", "Date", "Day", "Session title", "Reading", "Kind",
            "Source", "Printed pp.", "PDF pp.", "Brief written", "Feeds module"]
    header_row(ws, 5, cols)
    ws.freeze_panes = "A6"

    cases_dir = os.path.join(VAULT, cls, "10-cases")
    r = 6
    for s in ix["sessions"]:
        d = datetime.date.fromisoformat(s["date"])
        if not s["readings"]:
            vals = [s["session"], d, WEEKDAY[d.weekday()], s["title"],
                    "— no assigned reading —", "", "", "", "", "", ""]
            for i, v in enumerate(vals, start=1):
                c = ws.cell(row=r, column=i, value=v)
                c.font = BODY_DIM
                c.border = EDGE
            ws.cell(row=r, column=2).number_format = "yyyy-mm-dd"
            r += 1
            continue

        for j, rd in enumerate(s["readings"]):
            src = ix["sources"].get(rd.get("source"), {})
            off = src.get("offset")
            printed = pdf = ""
            if "start" in rd:
                printed = f"{rd['start']}–{rd['end']}"
                pdf = f"{rd['start'] + off}–{rd['end'] + off}"

            written = ""
            if rd["kind"] in ("case", "document", "note"):
                # A case assigned twice carries a " (redux)" suffix in the index so
                # the by-session view is complete, but there is still one file.
                stem = re.sub(r"\s*\(redux\)$", "", rd["case"])
                path = os.path.join(cases_dir, stem + ".md")
                written = "yes" if os.path.exists(path) else "no"

            module = ""
            if rd["kind"] in ("statute", "rule"):
                module = "doctrine module"
            elif rd["kind"] in ("document", "note"):
                module = "document note"

            vals = [
                s["session"] if j == 0 else "",
                d if j == 0 else "",
                WEEKDAY[d.weekday()] if j == 0 else "",
                s["title"] if j == 0 else "",
                rd["case"],
                KIND_LABEL.get(rd["kind"], rd["kind"]),
                rd.get("source", "").upper() or rd.get("note", ""),
                printed, pdf, written, module,
            ]
            for i, v in enumerate(vals, start=1):
                c = ws.cell(row=r, column=i, value=v)
                c.font = BODY if rd["kind"] == "case" else BODY_DIM
                c.alignment = Alignment(vertical="top", wrap_text=(i in (4, 5)))
                if s["session"] % 2 == 0:
                    c.fill = BAND
                if j == len(s["readings"]) - 1:
                    c.border = EDGE
            if j == 0:
                ws.cell(row=r, column=2).number_format = "yyyy-mm-dd"
            r += 1

    ws.auto_filter.ref = f"A5:{get_column_letter(len(cols))}{r - 1}"
    autosize(ws, [8, 12, 6, 34, 46, 11, 9, 12, 12, 13, 15])

    # ---------- Sessions ----------
    ws2 = wb.create_sheet("Sessions")
    ws2["A1"] = f"{cls} — session summary"
    ws2["A1"].font = TITLE
    cols2 = ["Session", "Date", "Day", "Title", "Readings", "Statutes & rules",
             "Other", "Notes written"]
    header_row(ws2, 3, cols2)
    ws2.freeze_panes = "A4"
    r = 4
    for s in ix["sessions"]:
        d = datetime.date.fromisoformat(s["date"])
        rs = s["readings"]
        ncase = sum(1 for x in rs if x["kind"] in ("case", "document", "note"))
        nstat = sum(1 for x in rs if x["kind"] in ("statute", "rule"))
        noth = len(rs) - ncase - nstat
        nwritten = sum(
            1 for x in rs if x["kind"] in ("case", "document", "note")
            and os.path.exists(os.path.join(cases_dir, x["case"] + ".md"))
        )
        vals = [s["session"], d, WEEKDAY[d.weekday()], s["title"], ncase, nstat,
                noth, f"{nwritten} / {ncase}" if ncase else ""]
        for i, v in enumerate(vals, start=1):
            c = ws2.cell(row=r, column=i, value=v)
            c.font = BODY
            c.alignment = Alignment(vertical="top", wrap_text=(i == 4))
            c.border = EDGE
        ws2.cell(row=r, column=2).number_format = "yyyy-mm-dd"
        r += 1
    autosize(ws2, [8, 12, 6, 38, 8, 16, 8, 14])

    # ---------- Sources ----------
    ws3 = wb.create_sheet("Sources")
    ws3["A1"] = "Source PDFs and page mapping"
    ws3["A1"].font = TITLE
    ws3["A2"] = ("Printed page is what the syllabus cites. PDF page is what a reader "
                 "opens. The offset is a fixed property of each scan.")
    ws3["A2"].font = BODY_DIM
    header_row(ws3, 4, ["Key", "Source", "File", "PDF page = printed page +"])
    r = 5
    for key, src in ix["sources"].items():
        for i, v in enumerate([key.upper(), src["label"], src["file"], src["offset"]], start=1):
            c = ws3.cell(row=r, column=i, value=v)
            c.font = BODY
            c.border = EDGE
        r += 1
    autosize(ws3, [8, 46, 52, 26])

    wb.save(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="cls")
    a = ap.parse_args()
    classes = [a.cls] if a.cls else ["busorg", "conlaw", "legalfinance"]
    made = 0
    for cls in classes:
        p = os.path.join(VAULT, cls, "99-meta", "case-index.json")
        if not os.path.exists(p):
            if a.cls:
                sys.exit(f"No index at {p}")
            continue
        with open(p) as f:
            ix = json.load(f)
        out = os.path.join(VAULT, cls, "99-meta", "case-index.xlsx")
        build(cls, ix, out)
        print("wrote", os.path.relpath(out, VAULT))
        made += 1
    if not made:
        sys.exit("No case-index.json found in any class folder.")


if __name__ == "__main__":
    main()
