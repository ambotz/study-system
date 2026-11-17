---
name: session-reconcile
description: Turn one class meeting's raw capture into doctrine. Use when asked to reconcile a session, process class notes, fill Professor gloss, or update professor_emphasis and exam_likelihood. Reads a session file in 20-sessions, finds the modules its readings feed, writes the gloss and re-weights the two prediction fields from what the professor actually did, and flips reconciled. Never edits the session file's Notes and never touches confidence.
---

# session-reconcile

The only place synthesis happens. `CLAUDE.md` section 1: notes enter the vault
indexed by date and must leave indexed by doctrine. A debrief filed without
updating the modules it touched has done nothing.

This skill is also the **only** writer permitted to revise `professor_emphasis`
and `exam_likelihood`. Those two fields are predictions before the class and
evidence afterwards, and their whole value is that they track what the professor
did. A second writer with a different basis destroys that.

## What it may and may not write

| Field | This skill |
|---|---|
| `## Professor gloss` on a module | **writes** |
| `professor_emphasis` | **revises**, from class evidence only |
| `exam_likelihood` | **revises**, from class evidence only |
| `reconciled` on the session file | flips to `true` |
| `confidence` | **never** — self-rated, human only |
| `last_drilled` | never — `exam-drill` owns it |
| The session file's Notes or Signals | **never** — raw capture, never cleaned up in place |
| Module body sections 1–6 and 8 | never — a factual error there is a `doctrine-module` job |

The session file is the audit trail behind every module. It is never rewritten
to read better, never tidied, never deleted after reconciliation.

## State of the corpus

Checked 2026-11-17. Read this before planning a batch.

| | Sessions with Notes | Signals answered | **Empty placeholders** |
|---|---|---|---|
| conlaw | 21 of 27 | 1–4 of 6 prompts, never all six | **22–27** (Spending, NFIB v. Sebelius, Secession, Art. IV, Art. V, Art. VI) |
| busorg | 20 of 27 | 1–3 of 6 | **21–27** (Voting ×2, VC/PE-backed, Creditors, Non-Corporate Entities, Non-Stock Corporations, Review) |

Two consequences.

1. **Work from the Notes, not the Signals.** `CLAUDE.md` section 6 anticipates
   this: "Where the Signals are blank, reconcile works from the Notes." The Notes
   are good — 250 to 875 words per session, with inline exam flags already marked
   in bold, e.g. *"**Exam note: Baude's liquidation theory / readings → Dig
   deep**"*. Those bolded asides are the highest-grade evidence in the vault and
   should be quoted verbatim into the gloss.
2. **The empty sessions cannot be reconciled and must not be faked.** Skip them
   and report them. They are the most recent classes and therefore the closest to
   the exam — Con Law 22–23 are Spending and *NFIB v. Sebelius*, which is the
   tax-power-versus-penalty question that appeared on three of three past Baude
   exams. Capturing those six from handwritten notes is worth more than
   reconciling any three sessions that already have Notes.

## Procedure

1. **Read the session file whole.** Frontmatter, Readings, Notes, Signals.

2. **Resolve the target modules.** Follow the Readings wikilinks to
   `10-cases/`, then each case file's `feeds_module`. Add any module the Notes
   discuss that the readings did not — class often goes somewhere the assignment
   did not. A statute or rule in the Readings links straight to its module.

3. **Read each target module before writing to it.** The gloss has to sit
   against the existing Rule statement and Common trap without contradicting
   them, and the emphasis revision has to be a judgment about movement from the
   current value, not a fresh guess.

4. **Extract the professor evidence.** Four kinds, in descending value:
   - an explicit exam flag, bolded in the Notes or in Signal 6;
   - a hypo and what it was fishing for, which is how an exam question gets built;
   - what the professor called hard, or said does not matter — both are grading instructions;
   - pushback on a student, which marks the line he thinks people get wrong.

   Evidence that is only "we covered this" is not evidence. Coverage is already
   recorded by the session file existing.

5. **Write the gloss.** Two to five sentences, in the professor's frame, naming
   him where the view is his rather than the course's. Quote the Notes verbatim
   where they are already pointed. No meta-commentary, per the house style — the
   heading says what the section is.

   Good: *"Baude ran the liquidation theory hard here and flagged the readings as
   exam material. He treats Madison's conditions — practice reasoned on
   constitutionality, and practice repeated or settled — as the operative test,
   not as background."*

   Bad: *"This section records what the professor said about this topic in
   class."*

6. **Revise the two prediction fields, and justify the move.** Raise
   `professor_emphasis` where class treatment exceeded the syllabus's billing,
   lower it where he passed over something the syllabus made look central. Leave
   the field alone where class gave no evidence either way — an unchanged field
   is a legitimate output and better than noise.

7. **Emit JSON, let the script write.**

   ```
   python3 .claude/skills/session-reconcile/scripts/apply_reconcile.py \
       --vault . --dry-run < reconcile.json
   ```

   Review the dry run, then drop `--dry-run`. The script asserts that
   `confidence` and `last_drilled` did not move and that the session file changed
   in exactly one place; it aborts rather than writing if either check fails.

### JSON schema

```json
{
  "class": "conlaw",
  "session_file": "ConLaw 18 - The Commerce Clause.md",
  "modules": [
    {
      "module": "Enumerated powers and the Necessary and Proper Clause - Art. I § 8 cl. 18",
      "professor_emphasis": 3,
      "exam_likelihood": "high",
      "gloss": "Two to five sentences in the professor's frame.",
      "evidence": "The line from the Notes or Signals this rests on. Quoted."
    }
  ]
}
```

`professor_emphasis` and `exam_likelihood` are optional per module — omit them
where class gave no evidence. `gloss` and `evidence` are required; `evidence` is
what makes the revision auditable in December when the number looks wrong.

Passing `confidence` or `last_drilled` is a hard error.

## Batching

Reconcile in **syllabus order**, one session per unit of work, because later
classes revise earlier ones and the gloss should end up reflecting where he
landed. Where two sessions cover one topic — BusOrg 17–20 are all Takeovers,
Con Law 16–17 both the Bank — read all of them before writing to the shared
modules, then write once.

A session typically touches three to six modules. Twenty-one Con Law sessions
against 31 modules means most modules will be written more than once; later
passes should **revise** the gloss rather than append to it.

## Reporting back

After a batch, say:

- which sessions were reconciled and which were skipped as empty;
- every `professor_emphasis` and `exam_likelihood` that moved, with the old and new value and the one-line basis;
- modules that no session touched at all — in a closed-book exam those are either genuinely peripheral or a gap in the capture, and the difference matters;
- modules where the Notes contradict the module's Rule statement. Do not fix those here. Report them for a `doctrine-module` pass.

## On confidence

`confidence` stays at `1` across all 31 Con Law modules until Ashwin sets it,
and no agent may set it for him — `CLAUDE.md` section 4 is explicit, and it is
the field the drill queue leans on hardest.

What this skill can legitimately do is make his pass cheap: after a batch,
produce a **review list** of the touched modules ordered by the revised
`professor_emphasis`, so he rates the ones that matter first. A list he reads
and acts on is not an agent writing the field.
