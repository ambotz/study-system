# law-vault — invariants

This file is the format law for this repo. It is not a summary of the charter;
it is the set of rules any agent or human writing into this vault must follow.
The charter (`study-system-charter.md`) holds the reasoning. This holds the rules.

---

## 1. The core rule: date in, doctrine out

Notes enter this vault **indexed by date** — a debrief from Tuesday's class, a
brief written the night before a reading. They must leave **indexed by doctrine**
— the rule on director loyalty, wherever it came from.

`/30-doctrine` is the asset. Everything in `/00-source`, `/10-cases`, and
`/20-sessions` is input. Everything in `/50-outline` and `/60-drills` is a
generated view of `/30-doctrine` and may be regenerated from it at any time.

Two of three fall classes are no-device, closed-book or one-page. Reconciliation
is therefore the **only** place synthesis happens. It cannot happen in the exam
room. An agent that files a debrief without updating the doctrine modules it
touches has done nothing useful.

## 2. Directory contract

```
<class>/
  00-source/      syllabus, readings, slides — read-only inputs, never edited
  10-cases/       one file per case, fixed schema
  20-sessions/    one file per class meeting, raw capture, date-named
  30-doctrine/    rule modules — the master DB
  40-professor/   instructor profile, past exams, hypo bank
  50-outline/     master -> attack -> one-pager/scaffold (generated)
  60-drills/      question bank, error log, timed attempts
  99-meta/        class-specific schema overrides and prompts
```

Classes: `busorg/` (Buccola), `conlaw/` (Baude), `legalfinance/` (Kelley).
Legal Finance is deliberately deferred — scaffolded, not populated.

Skills are repo-scoped and live in `.claude/skills/<name>/SKILL.md`. Professor-
specific behavior lives in the **data** (`40-professor/`), never in forked skill
code. If you find yourself writing `if professor == "Baude"` into a skill, the
thing you are encoding belongs in a professor file instead.

## 3. Doctrine module schema — FIXED

Body sections, in this order, no additions, no reordering:

1. Rule statement
2. Elements
3. Standard of review / burden
4. Exceptions
5. Leading case
6. Best counter-case
7. Professor gloss
8. Common trap

Frontmatter, required on every module:

```yaml
topic:               # string
sub-topic:           # string
professor-emphasis:  # integer 1-3
exam-likelihood:     # high | medium | low
confidence:          # integer 1-5, self-rated, human-set only
last-drilled:        # YYYY-MM-DD or null
```

This frontmatter is the study queue. Dataview reads it. If it drifts, the queue
breaks silently — an empty result looks the same as a passing one.

**`confidence` is human-set.** No agent writes or revises it. It is a self-rating
and an agent inferring it defeats the purpose of the field.

## 4. Session file schema — FIXED

One file per class meeting, named `YYYY-MM-DD.md`, in `<class>/20-sessions/`.
Captured within ~20 minutes of class, by dictation, against the same six prompts
every time:

1. What doctrine was on the table
2. What hypo he posed, and what he was fishing for
3. Where he pushed back on a student
4. What he called the hard case
5. What he said doesn't matter
6. Any exam signal

The six prompts are fixed so that the capture is comparable across weeks and
machine-readable without parsing prose. Session files are **raw capture**. They
are never cleaned up in place, never rewritten to read better, and never deleted
after reconciliation — they are the audit trail behind every doctrine module.

## 5. Case file schema — NOT YET SETTLED

`10-cases/` is scaffolded but has no fixed schema yet. **Do not create case files
and do not write a `case-brief` skill until this is settled with the human.**
Inventing a schema here and building on it is exactly the failure this section
exists to prevent.

## 6. Format law

- **Never freehand frontmatter.** A deterministic transform (OCR, tagging, an
  API call) asks a model for JSON against a schema, validates that JSON in a
  script, and lets the *script* write the YAML. A model writing YAML directly
  will eventually invent a key, and nothing will error.
- **Plain markdown is the source of truth.** Obsidian is a viewer. Gemini and
  NotebookLM are compute pointed at this vault. None of them is a second vault.
  If a tool's output isn't in this repo, it doesn't exist.
- **Generated files are never hand-edited.** Outlines and PDFs are regenerated
  from source. Editing a generated file means the next regeneration silently
  discards the edit.
- **Wikilinks over paths.** `[[Meinhard v. Salmon]]`, not a relative path, so
  the graph and backlinks work.
- One file per case. One file per class meeting. One file per rule.

## 7. Guardrails

- **Abrams Clinic material never enters this repo.** Not in any folder, not as a
  quotation, not as an anonymized example. This repo has a cloud remote and an
  agent with standing access. Clinic work needs a separate local-only vault or
  exclusion entirely.
- **The nightly job writes a proposed diff, never a direct commit.** The morning
  review of that diff is a recall pass and is the studying. Automating the gate
  away removes the learning and keeps only the artifact.
- **Agent write permissions are allowlisted to this vault directory only.**
- **No cloud folder sync over this directory.** The vault lives outside OneDrive
  deliberately. Git is the sync system. A periodic one-way mirror to OneDrive for
  backup is fine, but it must exclude `.git/`, and nothing may sync *into* here.
- **Keep `ANTHROPIC_API_KEY` unset** in any shell that runs this vault's jobs, so
  nothing silently routes to per-token Console billing instead of the Pro plan.

## 8. Open — do not silently resolve

These are unsettled. An agent that picks a default here and proceeds has made a
decision that was the human's to make. Ask.

- Case file schema (§5).
- Scheduling mechanism for the nightly job: local cron/launchd (needs a `pmset`
  wake schedule) vs. cloud Routines (needs the private remote, restricted to
  `claude/`-prefixed branches).
- Whether Harvey gives clean-enough Delaware corporate authority to shortcut the
  BusOrg case layer — test on three cases before designing around it.
- Legal Finance's exam-day tool (Exam4 kills the network; local Ollama was the
  sketch). Out of scope until the seminar's needs are clearer.
- Per-skill prompts. The charter is the spec, not the implementation.
