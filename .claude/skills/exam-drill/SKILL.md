---
name: exam-drill
description: Generate and run timed exam practice — full exams, short-form single-issue reps, opening-paragraph drills, and rewrites of past answers. Use when asked to drill, practise, run a timed attempt, set up exam practice, or build a hypo bank. Pulls material from 40-professor and 30-doctrine, enforces the real exam's constraints, and hands the result to essay-grade.
---

# exam-drill

Produces the rep, enforces the constraint, and hands the output to
`essay-grade`. It does not grade — the separation exists so an attempt is scored
against the rubric rather than against whatever the generator had in mind.

Five practice modes, plus rewrite. Each exists because the diagnostic named a
specific failure that mode attacks.

| Mode | Length | Attacks | Axes graded |
|---|---|---|---|
| `outline` | one question, 4–5 min | structure, element discipline, allocation | 2, 3, 6 |
| `opening-paragraph` | one opening per gate, ~7 min | thesis placement, commitment grammar | 1, 5 |
| `short-form` | one issue, 20–25 min | element discipline, counterargument weighting | all six |
| `timed-full` | full past exam, real clock | everything under a real budget | all six |
| `rewrite` | an answer already written | converts a named failure into a habit | the targeted axis |

**The rubric splits in half and the modes split with it.** Axes 2, 3 and 6 are
settled before a word is written; axes 1 and 5 only exist on the page. An
outline rep cannot see a softened verb and an opening rep cannot see a starved
section. Running only one kind leaves half the diagnostic untouched.

## Before generating anything

Read `<class>/40-professor/<Professor> - exam writing profile.md`. The
constraints the rep must replicate are stated there, and they differ:

- **Buccola** — three questions, 60/20/20, three hours, **closed-book and word-limited this year** where both past exams said "There are no word limits." Forty points every year are the paired-authority theory essay, and its framing is verbatim boilerplate.
- **Baude** — three questions, weights that move every year at 35 words per point, **in-class and closed-book this year** where every circulated answer came from an eight-hour open-book take-home. Q3 is a normative reform essay with no fact pattern, worth 20–30 points, every single year.

**Every circulated answer in this vault was written open-book.** Generating a rep
that allows lookup reproduces the wrong constraint. Default to closed-book for
both classes this year and say so in the rep header.

## Mode: outline

Four to five minutes on one question. No prose. This is the skill Baude tells
you to use, in the exam instructions themselves:

> "My advice is to sketch an outline to each of the questions before you
> actually begin to write. If you just dive in, you may get lost halfway
> through and you may run out of space."

Produce exactly three things per gate and nothing else:

1. **The gate, in the order the decider hits it.** Sourced per professor —
   Buccola's answers invent a standard-of-review sequence (*Direct or
   Derivative → Controlling Stockholder → Conflicted Director → Entire Fairness
   → Revlon → Unocal*); Baude's mirror the prompt's own labels and convert its
   verbs into sub-headings, which both 2023 scripts did independently with
   `Can?` / `Should?`.
2. **The holding for that gate**, in the professor's verdict word. Not "discuss
   whether it was cleansed" — *"not cleansed, no delegated committee under
   144(b)(1)."* A gate with no holding attached is a topic list.
3. **A word budget.** Baude's past caps run a constant 35 words per point, so
   the budget is arithmetic, not instinct. An outline with no numbers on it
   scores 0 on budget discipline however good the substance.

Target four to eight gates. An outline that runs to fifteen has not triaged,
which is the failure this mode exists to catch.

## Allocation is a checklist item, not a drill

Every shortfall in the 1L corpus sat in the question reached last — CivPro Q2 at
75% of cap, Contracts Q3 at roughly 40%. That is an allocation failure, and the
fix belongs at minute zero of a real attempt, not in its own practice mode.

The whole operation is arithmetic off the cover page: Baude's ratio has been a
constant **35 words per point** and his weights move every year, so read them
and multiply. Buccola has been a fixed **60/20/20** both years, so there is
nothing to decide at all. Neither takes sixty seconds, and neither improves with
repetition.

Reading every question before answering any is also not what a real sitting
looks like — it burns minutes and destroys momentum on a long issue-spotter.
Write the budget from the weights **before** reading question one, then read and
answer in order.

So: no `triage` mode. Step 1 of `timed-full` carries it instead, and it belongs
on the exam-day line of the one-pager.

## The combined rep — the one to run first

Fifteen minutes, one question, both halves of the rubric:

- **3 min** read the prompt
- **4 min** outline, as above
- **7 min** write the opening only, as below
- then **compare the two**

The comparison is the real output. Where the outline named a clean holding and
the prose lost it, the failure is transcription, not planning. Where the outline
was already a topic list, more writing practice will not help.

Elements 2025 Q1A is the worked example: in outline form, *"not strictly bound,
facts differ"* is a perfectly good bullet. On the page it came out as
*"should be bound by 9th circuit precedent… Instead of following the decision
from ChatGPT, we should not allow the seizure."* The plan was right and the
sentence lost it. That distinction is invisible unless both artifacts exist side
by side.

Grade as two entries — one `outline`, one `opening-paragraph` — against the same
`prompt_ref`, so the error log carries both and the delta is queryable.

## Mode: opening-paragraph

**One opening per gate, not one opening per question.** This is the correction
that matters: the unit is the analytical move, not the paper.

In a multi-issue answer there is no single holding to lead with, and the
circulated answers do not write a navigation paragraph — **one of fourteen**
Baude Con Law openings is a roadmap. Navigation is carried by headings. What
each heading then opens with is a disposition, in one or two sentences, and that
is the thing being drilled.

So a rep on a five-gate question is **five openings of 25–40 words**, not one
opening of 150. Same budget, five repetitions of the move instead of one.

### What a gate opening looks like

All three are verbatim from circulated answers.

> **Tax?** — "Based on Bailey and Sebelius, the GFSPT is not a tax under Congress's taxing-powers: (1) The cost of the tax is probably high enough to be a 'prohibitory financial punishment'; (2) there's no scienter requirement; (3) the 'tax' is collected by other agencies."

Heading, verdict, three-factor test enumerated inline — one sentence.

> **Standing** — "The State of California has standing to sue in this case."

Eleven words. A threshold issue cleared so the real analysis can start.

> **School** — "Same as State Courts, except replace DOJ with the Department of Education. It's also not responsible for collecting revenue."

Twenty words for a whole listed issue, by cross-reference. Under a cap, that is
the skill.

### The exception — single-thesis questions

Where the question has one call and one answer, the question *is* the unit, and
the opening is holding-plus-pre-scored-factors:

> "I believe that the judge should not allow Professor Vector to present this evidence to the jury. There are three main considerations here: whether the evidence is directly related to the case in question, whether the evidence is specific, and whether the probabilities involved are significant and large. The evidence is not directly related to the case, but it appears to be both specific and large."

Four sentences and the reader knows the holding, the test, and that two of three
factors cut against it. Baude's Q3 normative essay is always this shape.

### Running it

1. Draw a prompt and outline it first — the gates define the units.
2. State the professor's verdict word: `should` for Baude, `likely` for Buccola.
3. Write one opening per gate. Each leads with a disposition; none restates the question.

Grade on axes 1 and 5 only, one entry per question rather than per gate, with
the weakest gate opening quoted as the evidence.

## Mode: short-form

One issue, 20–25 minutes, 300–450 words.

Build the stem from a doctrine module: take its `Elements` and its
`Common trap`, then write a fact pattern that **turns on the trap**. The point of
a short-form rep is not coverage — it is forcing one line-drawing decision. The
`Facts` section of a two-layer BusOrg case file is built for this: a fact is
pivotal if changing it would change the result, so invert one pivotal fact and
ask what moves.

Require in every short-form answer:

- a holding in sentence one;
- the test marched or folded, per the professor's polarity;
- one counterargument stated at its strongest, attributed, answered, and **graded** — *"this is the weaker argument because…"*;
- a named missing fact with what it would change, where the professor invites it. Baude asks for this in terms and it is free points; Buccola says "you should not assume facts not in the prompt," so flag the gap without filling it.

## Mode: timed-full

A full past exam under the real constraints. These are the expensive reps —
budget maybe six across the quarter, not twenty.

1. **Set the clock and the caps before reading the prompt.** Write the per-question word budget at the top of the answer file. For Baude, derive it from the point weights at 35 words per point; the weights move every year, so read them off the page rather than reusing last year's.
2. **Write the word budget before reading question one.** Sixty seconds, straight off the cover page's weights. Every shortfall in the 1L corpus sat in the question reached last, and that is fixed here or not at all.
3. **Closed-book.** No casebook, no outline, no vault. A one-page sheet only where the real exam allows one.
4. **Hand the result to `essay-grade` unedited.** An attempt tidied before grading measures nothing.

Available material, by professor:

- `busorg/40-professor/` — Buccola 2023 and 2024 exams with circulated answers, Birdthistle 2025 as a contrast. The file named `...2026.Winter.Memo.pdf` is a student answer script, not professor commentary.
- `conlaw/40-professor/` — Baude 2018, 2021, 2023 with five circulated answers.
- `1L/.../Elements - Exam Study/` — Baude's Elements 2019, 2021, 2024 with seven circulated answers. Different course, same grader, and the largest exemplar set available.

## Mode: rewrite

Take an answer already written and rewrite it to fix **one** named axis. Cheapest
way to convert a diagnosis into a habit, because the substance is already settled
and all the attention goes to the prose.

Good candidates from the 1L corpus, each with a known defect:

- Elements 2025 Q1A — the contradictory opening. Rewrite to one clean holding.
- Elements 2025 Q2 and Q3 — 748 and 1,042 words with no internal structure. Rewrite with headings only; change nothing else.
- CivPro 2025 Q1B — a chronological tour of Twombly through Swanson that mentions the plaintiff twice. Rewrite to apply the standard to Barbara's complaint.
- CivPro 2025 Q3 — the losing arguments front-loaded. Rewrite with the holding first and the losers answered in place.

Grade the rewrite on the targeted axis and record both scores, so the error log
shows the delta.

## Generating a hypo bank

Where a class has no past-exam material for a topic, generate stems into
`<class>/40-professor/hypo-bank.md` rather than scattering them. Build each stem
from a doctrine module and record which module it came from, so a rep can be
traced back to the rule it tests.

Draw preferentially from modules with `professor_emphasis: 3` and
`exam_likelihood: high`, and from the archetypes the professor actually repeats.
For Baude the highest-yield targets are the tax-power-versus-penalty question,
which appeared in 2018 Q1, 2021 Q1 and 2023 Q2, and the [[Youngstown Sheet & Tube Co. v. Sawyer (1952)|Youngstown]]
categories, which anchor two of three Q1s. For Buccola it is the paired-authority
essay: build pairs across case/case, statute/case and statute/statute lines, and
drill the recurring Delaware themes — legislative retrenchment after an unpopular
decision, ex ante predictability, private ordering, deference to market practice.

## After the attempt

1. Hand the answer to `essay-grade`, which writes the attempt file and the error-log row.
2. Update `last_drilled` on each doctrine module the rep covered. **This is the only frontmatter field this skill may write**, and only on a completed attempt.

   ```
   python3 .claude/scripts/build_cards.py --help
   ```

   Use a script to set the date; do not hand-edit the YAML.
3. Leave `confidence` alone. It is self-rated and human-only, and it is the field the drill queue leans on hardest.
4. Leave `professor_emphasis` and `exam_likelihood` alone. Only `session-reconcile` may revise them, because their whole value is that they track what the professor actually did in class.

## What this skill does not do

- It does not grade. `essay-grade` does.
- It does not write session or case files.
- It does not generate a hypo that smuggles in facts the professor's instructions forbid assuming.
