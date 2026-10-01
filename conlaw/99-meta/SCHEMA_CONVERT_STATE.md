# Con Law schema conversion — state

Everything here is set up. **Do not rebuild any of it.**

## Done and committed

- `CLAUDE.md` section 5 — two schemas, 5a Con Law one-pass (nine sections), 5b BusOrg/LF two-layer.
- `.claude/skills/case-brief/SKILL.md` — section order for both, finishing checklist with the dead-link check.
- `99-templates/case-brief-conlaw.md` — empty skeleton.
- `99-templates/case-brief-conlaw-EXAMPLE (Lovett).md` — finished file on the new schema. This IS the converted Lovett; do not redo it.
- 317 dead wikilinks unlinked across 53 Class 5+ files (`.claude/scripts/unlink_dead.py`).

## Ready on disk — reuse, do not regenerate

- `conlaw/99-meta/SCHEMA_CONVERT_GUIDE.md` — the conversion spec, with per-section word budgets (working copy mirrored in `_inbox/schema-v2/`).
- `_inbox/schema-v2/extracts/` — 27 casebook extracts (reading + 3 pages, so the numbered Notes are included). Regenerate only if missing: `extract_case.py "<case>" --class conlaw --plus 3 --out <f>`.
- `_inbox/schema-v2/manifest.json` — 36 cases, session number, extract filename or null.
- `_inbox/schema-v2/out/A..H/ASSIGN.md` — the 36 cases split 8 ways (A–D are 5 cases, E–H are 4).
- `_inbox/schema-v2/converted/` — converted files awaiting validation and commit.

## Converted so far

| Case | Status |
|---|---|
| United States v. Lovett | done, is the worked example |
| Humphrey's Executor v. United States | **converted but 2,620 words — needs trimming to band before commit.** Schema, links and gloss all check out. |

34 remain.

## Nine cases have no casebook extract

Trump v. Slaughter, Trump v. Cook, United States v. Nixon, Trump v. United States,
Ex parte McCardle, Bailey v. Drexel Furniture Co, National Pork Producers Council v. Ross,
In re Neagle, Dillon v. Gloss. The first eight are Canvas-only readings with no casebook
pages; Dillon's source is the Class 26 scan, which `extract_case.py` cannot resolve.
For these, keep the existing cold-call content and add the line the guide specifies.

## How to run it without burning usage

One agent, 2–3 cases, then validate and commit before dispatching the next. Large
fan-outs have hit the account session limit three times and lost the work. The
inputs above survive; only the agent output is lost, so keep batches small enough
to commit.

Validation before any commit: nine headings in order and nothing else at `##`;
Professor gloss empty; every wikilink resolves in `10-cases/` or `30-doctrine/`;
no link ends in a period; no wikilink spans a newline; no `***`; frontmatter and
any callout intact; word count in band.
