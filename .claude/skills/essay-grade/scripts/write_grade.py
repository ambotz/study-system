#!/usr/bin/env python3
"""Validate a grade JSON object and write the attempt file.

CLAUDE.md section 7: never freehand frontmatter. The model produces JSON against
the schema below, this script validates it, and this script writes the YAML.

Usage:
    python3 write_grade.py --class busorg < grade.json
    python3 write_grade.py --class conlaw --dry-run < grade.json

Writes <class>/60-drills/attempts/<date> - <source> - <mode>.md and appends one
line to <class>/60-drills/error-log.md.
"""

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

AXES = [
    "thesis_placement",
    "visible_structure",
    "element_discipline",
    "counterargument_weighting",
    "commitment_grammar",
    "budget_discipline",
]
MODES = {"timed-full", "short-form", "opening-paragraph", "rewrite"}
REQUIRED = {"source", "mode", "professor", "prompt_ref", "axes", "verdict", "next_rep"}


def fail(msg: str) -> None:
    print(f"write_grade: {msg}", file=sys.stderr)
    sys.exit(1)


def slug(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip()
    return re.sub(r"\s+", " ", text)[:60]


def validate(g: dict) -> None:
    missing = REQUIRED - g.keys()
    if missing:
        fail(f"missing required keys: {sorted(missing)}")
    if g["mode"] not in MODES:
        fail(f"mode must be one of {sorted(MODES)}, got {g['mode']!r}")
    if set(g["axes"]) != set(AXES):
        fail(f"axes must be exactly {AXES}, got {sorted(g['axes'])}")
    for axis, entry in g["axes"].items():
        if not isinstance(entry, dict):
            fail(f"axes.{axis} must be an object")
        if entry.keys() < {"score", "evidence", "fix"}:
            fail(f"axes.{axis} needs score, evidence, fix")
        if entry["score"] not in (0, 1, 2, 3):
            fail(f"axes.{axis}.score must be 0-3, got {entry['score']!r}")
        if not str(entry["evidence"]).strip():
            fail(f"axes.{axis}.evidence is empty — quote the answer")


def yaml_scalar(value) -> str:
    text = str(value).replace('"', "'")
    return f'"{text}"'


def render(g: dict, date: str) -> str:
    scores = {a: g["axes"][a]["score"] for a in AXES}
    fm = [
        "---",
        f"kind: exam_attempt",
        f"class: {g['professor_class']}",
        f"professor: {yaml_scalar(g['professor'])}",
        f"mode: {g['mode']}",
        f"source: {yaml_scalar(g['source'])}",
        f"prompt_ref: {yaml_scalar(g['prompt_ref'])}",
        f"date: {date}",
        "scores:",
    ]
    fm += [f"  {a}: {scores[a]}" for a in AXES]
    fm += [
        f"score_total: {sum(scores.values())}",
        f"score_max: {3 * len(AXES)}",
        "graded_by: essay-grade",
        "---",
        "",
    ]

    body = [f"# {g['source']} — {g['mode']}", ""]
    body += ["## Verdict", "", g["verdict"].strip(), ""]
    body += ["## Axes", ""]
    for axis in AXES:
        e = g["axes"][axis]
        body += [
            f"### {axis.replace('_', ' ').capitalize()} — {e['score']}/3",
            "",
            f"**Evidence.** {e['evidence'].strip()}",
            "",
            f"**Fix.** {e['fix'].strip()}",
            "",
        ]
    if g.get("substance_notes"):
        body += ["## Substance noted, not scored", "", g["substance_notes"].strip(), ""]
    body += ["## Next rep", "", g["next_rep"].strip(), ""]
    return "\n".join(fm + body)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class", dest="klass", required=True)
    ap.add_argument("--vault", default=".")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    try:
        grade = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        fail(f"stdin is not valid JSON: {exc}")

    grade["professor_class"] = args.klass
    validate(grade)

    date = grade.get("date") or dt.date.today().isoformat()
    vault = pathlib.Path(args.vault).resolve()
    drills = vault / args.klass / "60-drills"
    if not drills.is_dir():
        fail(f"no such folder: {drills}")

    attempts = drills / "attempts"
    out = attempts / f"{date} - {slug(grade['source'])} - {grade['mode']}.md"
    text = render(grade, date)

    total = sum(grade["axes"][a]["score"] for a in AXES)
    weakest = min(AXES, key=lambda a: grade["axes"][a]["score"])
    log_line = (
        f"| {date} | {grade['mode']} | {grade['source']} | {total}/{3 * len(AXES)} "
        f"| {weakest.replace('_', ' ')} | {grade['next_rep'].strip().splitlines()[0][:80]} |"
    )

    if args.dry_run:
        print(text)
        print("\n--- error-log line ---")
        print(log_line)
        return 0

    attempts.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")

    log = drills / "error-log.md"
    if not log.exists():
        log.write_text(
            "---\nkind: error_log\nclass: " + args.klass + "\ngenerated: true\n---\n\n"
            "# Error log\n\nOne row per graded attempt. Written by `essay-grade`; "
            "regenerate rather than hand-edit.\n\n"
            "| date | mode | source | score | weakest axis | next rep |\n"
            "|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    with log.open("a", encoding="utf-8") as fh:
        fh.write(log_line + "\n")

    print(f"wrote {out}")
    print(f"appended to {log}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
