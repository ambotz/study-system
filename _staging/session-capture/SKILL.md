---
name: session-capture
description: Turn photographed handwritten class notes into the Notes and Signals of the matching session file in busorg/ or conlaw/ 20-sessions. Use when notes photos are in _inbox/ and need to be filed. Fills only empty sections of an existing placeholder; never creates, overwrites, or commits.
---

# session-capture

Photographed handwritten notes in, filled session file out. Photos replace the dictated debrief as the primary capture for the two no-device classes (Bus Orgs and Con Law I). Legal Finance is out of scope: devices are allowed there and live notes go on the reading files.

## How to run

1. AirDrop the photos to the Mac (JPEG or HEIC both work).
2. Drag them into `_inbox/busorg/` or `_inbox/conlaw/`. The folder is the class; the script does not guess it.
3. Double-click `Ingest Notes.command` in the vault root, or run in Terminal from the vault:
   `python3 .claude/skills/session-capture/scripts/ingest_notes.py`
   Options: `--class conlaw`, `--dry-run` (show, write nothing), `--model opus` (step up if a transcription misses).
4. Open the session file in Obsidian. Fix anything marked `[?]`, resolve each `[check: …]`, and polish. Then commit and push yourself.

## What it does

- Converts each photo to a JPEG no larger than 1800 px with macOS `sips`. This uses no model tokens and cuts the image cost of the model call.
- Calls `claude -p` once per class with the photos, a compact session index (number, date, title, readings), and the class's case and doctrine-module names. The reply is JSON against the schema in `prompt.md`. `ANTHROPIC_API_KEY` is stripped from the call so usage stays on the Pro plan.
- Validates the JSON in the script. The script, not the model, writes the markdown. No frontmatter is written or changed.
- Works out which meeting the pages belong to: BusOrg by the date in the header, matched against the placeholder's `date`; ConLaw by the "Class N" header, because every ConLaw placeholder date is blank. If zero or several meetings match, it stops.
- Writes into the existing `<Class> NN - <Title>.md`: the `## Notes` body and blank Signals lines only. Refuses if Notes already has content, if the file is reconciled, or if the section layout has drifted.
- Saves the resized JPEGs to `<class>/20-sessions/_photos/<Class> NN pK.jpg` (linked from the end of Notes), empties the inbox (the original stays in your phone's Photos library), and runs `check_links.py`. A photo leaves the inbox only after its notes are written, so anything still in the inbox has not been filed.

## Rules the transcription follows

- Raw capture (CLAUDE.md §6): his wording and order, no summary, no added law.
- Unclear word: best reading plus `[?]`. Apparent misstatement where the intended reference is clear: his words kept, plus `[check: correction]`. Nothing is corrected silently. Substantive fixes belong to `session-reconcile`.
- Diagrams: Mermaid `flowchart` for relationship drawings, a short ASCII sketch for spatial ones. Labels and connections he drew only.
- Signals are filled only where the notes clearly support an answer, otherwise `—`. Never inferred.
- Wikilinks only to real notes. A link to a name that does not exist is unwrapped to plain text and reported.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| "no placeholder is dated …" | header date not in the placeholder | write "Class N" on the page, or add the date to the placeholder |
| "already has content under Notes" | Notes was filled before | add the new pages by hand; the script never appends |
| "model's reply failed validation" | malformed JSON | raw reply is in `_inbox/<class>/_last_model_output.txt`; fix it and rerun with `--from-json` |
| "photos were not assigned" | a photo is missing from every session's `pages` | rerun; if it repeats, use `--model opus` |
| Mermaid block shows as text | syntax the renderer rejects | edit the block by hand; the photo is linked below it |

## Files

- `scripts/ingest_notes.py` — the whole pipeline (standard library only).
- `prompt.md` — the transcription prompt and JSON schema. Edit here to change behaviour.
- `fixtures/` — `busorg-01.json` and `conlaw-01.json`, the reference output for the first session, usable with `--from-json`.
