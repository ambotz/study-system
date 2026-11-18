---
name: essay-grade
description: Grade a practice exam answer on writing craft against Ashwin's own 1L failure modes and the professor's circulated answers. Use when asked to grade, score, or critique a practice answer, attempt, or exam essay. Scores six axes, quotes the answer back as evidence, and writes an attempt file plus an error-log row. Does not grade substance except as a flagged note.
---

# essay-grade

Grades the **writing**, not the law. Substance errors are noted at the end and
never scored, because the diagnostic this skill implements found that the
measurable gap between Ashwin's 177s and his 184 was structural, not doctrinal.

Two inputs are mandatory and the skill stops without them:

- `99-exam-writing/1L writing diagnostic.md` — the six axes and what each failure looks like in his own prose.
- `<class>/40-professor/<Professor> - exam writing profile.md` — the per-professor polarity. Several axes invert between professors; grading Buccola against Baude's standard produces confidently wrong output.

**Professor behaviour lives in those profile files, never in this skill.** If a
judgment here needs an `if professor ==` branch, the thing being encoded belongs
in the profile instead.

## Procedure

1. **Locate the three documents.** The answer, the prompt it answers, and the
   professor profile for the class. No prompt means no grade on structure or
   budget — half the rubric is about whether the answer tracked the question —
   so ask for it rather than guessing.

2. **Run the metrics.**

   ```
   python3 .claude/skills/essay-grade/scripts/metrics.py <answer> --caps 1200,750,1050
   ```

   Omit `--caps` where the exam states none. The script strips Exam4 page
   banners automatically. Read the JSON before reading the answer: the first and
   second sentence of each section, the heading list, and the cap utilisation
   are three of the six axes already.

3. **Read the whole answer.** Scores depend on whether a counterargument was
   answered later, which is invisible until the end.

4. **Score the six axes, 0–3, with a quotation from the answer for each.** An
   axis scored without a quotation is not a grade, it is an impression. Where the
   answer does the right thing, quote that too — the exemplar move is as worth
   recording as the failure.

5. **Emit JSON and let the script write the file.** Never hand-write the
   frontmatter.

   ```
   python3 .claude/skills/essay-grade/scripts/write_grade.py --class busorg --vault . < grade.json
   ```

   Run with `--dry-run` first and show the rendered output, then write.

## Which axes a mode may score

A micro-drill cannot observe every axis, and scoring one it cannot see produces
a number with nothing behind it. The script enforces the set.

| Mode | Axes scored |
|---|---|
| `timed-full`, `short-form` | all six |
| `opening-paragraph` | 1 thesis placement, 5 commitment grammar |
| `outline` | 2 visible structure, 3 element discipline, 6 budget discipline |
| `rewrite` | whichever axis the rewrite targeted — at least one |

`score_max` is computed from the axes actually scored, so a 7/9 outline and a
14/18 timed-full are both legible in the error log without pretending to be the
same measurement.

**The two halves of the rubric split cleanly.** Axes 2, 3 and 6 are decided
before a word is written; axes 1 and 5 only exist on the page. That is why the
outline rep and the opening rep are run as a pair, and why the gap between them
is worth more than either score — see the combined rep in `exam-drill`.

## Grading an outline

Same 0–3 scale, different evidence. An outline is not prose and must not be
graded as though it were trying to be.

- **Visible structure.** Is there one entry per decision, in the order the
  decider hits them, with the professor's sourcing — Buccola's invented
  standard-of-review gates, Baude's mirror of the prompt's own labels and verbs?
  A list of topics is a 1. A sequence of gates is a 3.
- **Element discipline.** Does each gate carry its test with the elements
  enumerated and a holding attached, or just the gate's name? "Entire fairness"
  is a 1. "Entire fairness — not cleansed under 144(b)(1), no delegated
  committee, Enya voted → fair price and fair dealing, likely fails" is a 3.
- **Budget discipline.** Are words allocated per gate before drafting, and does
  the allocation track the point weights? An outline with no numbers on it
  scores 0 on this axis however good the substance, because allocation is the
  thing the drill exists to train.

Do not score an outline on prose quality, hedging, or sentence construction.
If the outline reveals a substance problem, it goes in `substance_notes`.

## The six axes

Each scores 0–3. The anchors are Ashwin's own answers, so the scale is
calibrated rather than abstract.

### 1. Thesis placement

Is the first sentence of each answer unit a single clean holding, and does
sentence two support it rather than contradict it?

- **3** — one clause, one disposition, nothing appended. *"The Court of Appeals should not overturn Riggs."*
- **2** — holding present but carrying a subordinate clause that does other work.
- **1** — holding arrives by sentence three, or the opening names a framework instead. *"Without Congress, the first major impact is the strength of statutory stare decisis will diminish."*
- **0** — sentences one and two contradict each other, as in Elements 2025 Q1A: *"The district court in CA should be bound by 9th circuit precedent… Instead of following the decision from ChatGPT, we should not allow the seizure."*

Benchmark: 28 of roughly 30 Baude exemplar units open with the bottom line.

### 2. Visible structure

Headings or run-in labels present, and **sourced correctly for this professor**.
The profile says which. Baude's answers mirror the prompt's own labels and
convert its verbs into sub-headings; Buccola's invent a standard-of-review
taxonomy on Q1 and use none at all on the theory essays.

- **3** — every question carries structure from the right source, and a reader can navigate the answer without reading it.
- **1** — structure on the first question only, the rest undifferentiated prose.
- **0** — none anywhere, as in CivPro 2025.

Across Ashwin's four graded answers this axis correlated exactly with grade.
It is the cheapest point in the rubric.

### 3. Element discipline

Is the governing test marched, or named and abandoned? **Polarity is per
professor.** Baude: *"Don't assume that I'll know you know the basics; show
me!"* — enumerate. Buccola: *"complicating simple issues … signals a weak grasp"*
— fold the test into the sentence and hang the authority off the end.

Score the fit to the professor, not the enumeration itself. The 184's
*"(1) they are bought with an investment of money, (2) in Steep, (3) …"* is a 3
on Baude and a 1 on Buccola.

Also score here: **did the answer kill the doctrines it rejected, with a
reason?** *"Regulation crowdfunding is not viable since no registered funding
portal was used"* is the move. Silent omission is not.

### 4. Counterargument weighting

Is the losing argument stated at its strongest, attributed to a holder, answered,
and then **graded**?

- **3** — all four beats, with an explicit weight verdict: *"This is a fairly weak argument, however"* · *"and more convincingly"* · *"the inducement argument is the weakest link of the defense."*
- **2** — counter raised and answered, no weight verdict. This is Ashwin's default.
- **1** — counter raised and left hanging.
- **0** — no counter, or the losing side front-loaded before the holding, as in CivPro Q3 where four losing arguments precede *"However, none of these arguments will likely be enough."*

The weight verdict appears throughout every benchmark set and once across four
of Ashwin's exams. Treat its absence as the standing finding it is.

### 5. Commitment grammar

Hedges on the argument, commitment on the verb — and the right verdict word for
the professor (`should` for Baude, `likely` for Buccola).

Check `softened_own_verb` in the metrics output first. *"We should probably
follow"* and *"will probably give us authority"* are automatic deductions.

- **3** — hedged subject, unhedged verb throughout; verdict words carry a named disposition.
- **1** — flat assertion with no visible weighing, which on a Levmore-type grader reads as the evasion he penalises, or conclusions placed at paragraph end where they read as summary.
- **0** — own verbs softened.

Do **not** reward low hedge density. The Rappaport models hedge at 1.5–3.3 per
1,000 words and the Baude exemplars at 5.7–14.2; Ashwin's 1L answers ran
0.30–0.96 and scored at or below median. The target is placement, not scarcity.

### 6. Budget discipline

Words per section against the stated cap, and whether any shortfall is
concentrated.

- **3** — 97%+ on every section. Baude's exemplars hit 98.1–100.0% on fifteen of fifteen.
- **2** — one section between 85% and 97%.
- **1** — one section below 80%. CivPro Q2 at 75%, Contracts Q3 at ~40%.
- **0** — over cap on an exam that says *"I won't read additional words,"* which is pure loss.

Where the exam states no cap, score allocation against the point weighting
instead: Buccola's strong answers run 58–66% / 18–25% / 16–21% against 60/20/20.

## Output

One attempt file in `<class>/60-drills/attempts/` and one appended row in
`<class>/60-drills/error-log.md`, both written by `write_grade.py`. The error log
is the thing to read in week ten: a single axis sitting at 1 across six attempts
is the drill to run, and a single axis climbing from 1 to 3 is the habit that
took.

### JSON schema

```json
{
  "source": "Buccola 2024 Q1",
  "mode": "timed-full",
  "professor": "Buccola",
  "prompt_ref": "busorg/40-professor/Business_Organizations.Buccola.2024.Fall.Exam.pdf",
  "date": "2026-11-18",
  "verdict": "Two or three sentences. What this answer would read like to the grader.",
  "axes": {
    "thesis_placement":          {"score": 2, "evidence": "quote", "fix": "one instruction"},
    "visible_structure":         {"score": 3, "evidence": "quote", "fix": "..."},
    "element_discipline":        {"score": 1, "evidence": "quote", "fix": "..."},
    "counterargument_weighting": {"score": 2, "evidence": "quote", "fix": "..."},
    "commitment_grammar":        {"score": 2, "evidence": "quote", "fix": "..."},
    "budget_discipline":         {"score": 3, "evidence": "quote", "fix": "..."}
  },
  "substance_notes": "Optional. Doctrinal errors, flagged and not scored.",
  "next_rep": "One concrete drill, naming the mode and the target."
}
```

`fix` is one instruction the next attempt can follow, not a paragraph of advice.
"Put the holding in sentence one" is a fix; "work on your structure" is not.

Carry only the axes the mode allows. An `outline` grade carries three keys and
an `opening-paragraph` grade two. The script rejects the wrong set rather than
silently scoring air.

## What this skill does not do

- **It does not score substance.** Doctrinal errors go in `substance_notes`, flagged, unscored. Grading both at once lets a strong doctrinal answer hide a structural failure, which is exactly the pattern the 177s show.
- **It does not touch `confidence` on any doctrine module.** That field is self-rated and human-only.
- **It does not revise `professor_emphasis` or `exam_likelihood`.** Only `session-reconcile` may.
- **It does not rewrite the answer.** A rewrite is a separate rep, run through `exam-drill` in rewrite mode so the before and after are both on the record.
