#!/usr/bin/env python3
"""Apply one session's reconciliation to the doctrine modules it touched.

CLAUDE.md section 7: never freehand frontmatter. The model produces JSON against
the schema below; this script validates it and writes the YAML and the gloss.

Guarantees, enforced by assertion after every write:
  - `confidence` and `last_drilled` are never modified. They are not in the
    schema, and the script re-reads each module and aborts if either moved.
  - The session file changes in exactly one place: `reconciled: false` becomes
    `reconciled: true`. Every other byte must match, or the write is rolled back.
  - Only `professor_emphasis`, `exam_likelihood` and the `## Professor gloss`
    body section are touched on a module.

Usage:
    python3 apply_reconcile.py --vault . --dry-run < reconcile.json
    python3 apply_reconcile.py --vault . < reconcile.json
"""

import argparse
import json
import pathlib
import re
import sys

LIKELIHOOD = {"high", "medium", "low"}
FROZEN = ("confidence", "last_drilled")
GLOSS = "## Professor gloss"


def fail(msg: str) -> None:
    print(f"apply_reconcile: {msg}", file=sys.stderr)
    sys.exit(1)


def split_frontmatter(text: str, where: str):
    if not text.startswith("---\n"):
        fail(f"{where}: no frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{where}: unterminated frontmatter")
    return text[4:end + 1], text[end + 5:]


def read_key(fm: str, key: str):
    m = re.search(rf"^{re.escape(key)}:(.*)$", fm, re.M)
    return None if m is None else m.group(1).strip()


def set_key(fm: str, key: str, value: str, where: str) -> str:
    pattern = rf"^{re.escape(key)}:.*$"
    if not re.search(pattern, fm, re.M):
        fail(f"{where}: no `{key}` key to update — refusing to invent one")
    return re.sub(pattern, f"{key}: {value}", fm, count=1, flags=re.M)


def set_gloss(body: str, gloss: str, where: str) -> str:
    start = body.find(GLOSS)
    if start == -1:
        fail(f"{where}: no `{GLOSS}` section — the module is off schema")
    after = body.find("\n## ", start + len(GLOSS))
    tail = body[after:] if after != -1 else "\n"
    return body[:start] + f"{GLOSS}\n\n{gloss.strip()}\n" + tail


def validate(payload: dict) -> None:
    for key in ("class", "session_file", "modules"):
        if key not in payload:
            fail(f"missing required key: {key}")
    if not payload["modules"]:
        fail("modules is empty — a reconciliation that touches nothing is not a reconciliation")
    for i, m in enumerate(payload["modules"]):
        where = f"modules[{i}]"
        for key in ("module", "gloss", "evidence"):
            if not str(m.get(key, "")).strip():
                fail(f"{where}.{key} is empty")
        for key in FROZEN:
            if key in m:
                fail(f"{where} carries `{key}` — that field is not reconcilable")
        if "professor_emphasis" in m and m["professor_emphasis"] not in (1, 2, 3):
            fail(f"{where}.professor_emphasis must be 1-3, got {m['professor_emphasis']!r}")
        if "exam_likelihood" in m and m["exam_likelihood"] not in LIKELIHOOD:
            fail(f"{where}.exam_likelihood must be one of {sorted(LIKELIHOOD)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=".")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        fail(f"stdin is not valid JSON: {exc}")
    validate(payload)

    vault = pathlib.Path(args.vault).resolve()
    klass = payload["class"]
    session = vault / klass / "20-sessions" / payload["session_file"]
    if not session.is_file():
        fail(f"no such session file: {session}")

    planned = []
    for m in payload["modules"]:
        path = vault / klass / "30-doctrine" / f"{m['module']}.md"
        if not path.is_file():
            fail(f"no such module: {path}")
        original = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(original, m["module"])
        frozen_before = {k: read_key(fm, k) for k in FROZEN}

        if "professor_emphasis" in m:
            fm = set_key(fm, "professor_emphasis", str(m["professor_emphasis"]), m["module"])
        if "exam_likelihood" in m:
            fm = set_key(fm, "exam_likelihood", m["exam_likelihood"], m["module"])
        body = set_gloss(body, m["gloss"], m["module"])

        updated = "---\n" + fm + "---\n" + body
        fm_after, _ = split_frontmatter(updated, m["module"])
        frozen_after = {k: read_key(fm_after, k) for k in FROZEN}
        if frozen_before != frozen_after:
            fail(f"{m['module']}: frozen field moved ({frozen_before} -> {frozen_after}) — aborting")
        planned.append((path, original, updated, m))

    session_text = session.read_text(encoding="utf-8")
    s_fm, s_body = split_frontmatter(session_text, session.name)
    if read_key(s_fm, "reconciled") == "true":
        print(f"note: {session.name} is already reconciled; re-running will overwrite the gloss",
              file=sys.stderr)
    s_new = "---\n" + set_key(s_fm, "reconciled", "true", session.name) + "---\n" + s_body
    # The only permitted change is the flag itself. On a re-run the file is
    # already `true`, so the two texts are identical; on a first run they differ
    # by exactly that one line.
    if s_new != session_text and s_new.replace("reconciled: true", "reconciled: false", 1) != session_text:
        fail("session file would change in more than the `reconciled` flag — aborting")

    if args.dry_run:
        for path, original, updated, m in planned:
            print(f"--- {path.relative_to(vault)}")
            print(f"    professor_emphasis -> {m.get('professor_emphasis', '(unchanged)')}")
            print(f"    exam_likelihood    -> {m.get('exam_likelihood', '(unchanged)')}")
            print(f"    gloss ({len(m['gloss'].split())} words): {m['gloss'].strip()[:160]}")
            print(f"    evidence: {m['evidence'].strip()[:160]}")
        print(f"--- {session.relative_to(vault)}\n    reconciled -> true")
        print(f"\n{len(planned)} module(s) would change. No files written.")
        return 0

    for path, _original, updated, _m in planned:
        path.write_text(updated, encoding="utf-8")
    session.write_text(s_new, encoding="utf-8")
    print(f"reconciled {session.name} -> {len(planned)} module(s) updated")
    for path, _o, _u, m in planned:
        print(f"  {m['module']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
