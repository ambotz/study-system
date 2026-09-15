# legalfinance — class override

Root `CLAUDE.md` is the format law for this repo. This file overrides it **for this
folder only**. Where the two conflict, this file wins inside `legalfinance/`. Where this
file is silent, the root governs — frontmatter is still `snake_case`, wikilinks are still
mandatory, house style is unchanged, and the guardrails in root § 8 apply everywhere.

---

## 1. Why this class diverges

BusOrg and Con Law are built for a closed-book exam. The asset is a doctrine module,
because the exam asks you to state a rule and apply it under time pressure with nothing in
front of you.

**Legal Finance has no exam.** The grade is 40% engagement and participation, 35% group
assignments, 25% an individual ~15-page paper due March 22, 2027. There is almost nothing
to memorise and three things to produce: **talk**, **documents**, and **a paper**.

The readings are also a different species. Nine classes, roughly forty-five readings, of
which **three are cases**. The rest are law review articles, government reports,
congressional testimony, pending bills, state statutes, bar ethics opinions, industry
white papers, trade press and one podcast. Many are **advocacy** — a funder explaining why
funding is good, a reinsurer explaining why it is expensive, the defence bar explaining
why it should be disclosed. A schema built to extract a holding will extract nothing from
any of them.

So the core rule changes shape:

> Notes enter indexed by **date**. They must leave indexed by **argument** and by
> **structure** — the contested question, wherever it came from, and the deal mechanic,
> however it was described.

`30-concepts/` and `50-positions/` are the assets. `60-deals/` and `70-paper/` are the
work product those assets feed. `00-source`, `10-readings` and `20-sessions` are input.

## 2. Directory contract — this folder

```
legalfinance/
  00-source/      syllabus, downloaded readings, model documents — read-only inputs
  10-readings/    one file per assigned reading, whatever its species
  20-sessions/    one file per seminar, date-named — raw capture
  30-concepts/    what a thing IS — structures, instruments, actors, mechanics
  40-professor/   Kelley profile, guest lecturers, what he rewards
  50-positions/   what is CONTESTED — one file per live question, both sides
  60-deals/       the transactional layer — term sheet anatomy, clause bank, assignments
  70-paper/       final project — candidate topics, source bank, thesis, drafts
  99-meta/        reading index and the generated workbook
```

Three renames from the repo default, and one addition. `10-cases` → `10-readings` because
three readings out of forty-five are cases. `30-doctrine` → `30-concepts` because this
course has structures, not rules. `50-outline` → `50-positions` and `60-drills` →
`60-deals` because there is no exam to outline for and no issue-spotter to drill.
`70-paper` is new and has no analogue in the other classes.

## 3. Reading file schema — FIXED

One file per assigned reading, in `10-readings/`, named by a short human title
(`Bedi and Marra - The Shadows of Litigation Finance`). Not by citation.

```yaml
---
reading: The Shadows of Litigation Finance
author: Suneal Bedi & William C. Marra
kind: article          # see the kind list below
publication: 74 Vand. L. Rev. 563
year: 2021
class: legalfinance
session: 1
read_for: 2026-09-30
topic: Rationale and economics
speaking_for: academic   # see the speaker list below
feeds_concept:
  - "[[...]]"
feeds_position:
  - "[[...]]"
url: https://bit.ly/3C7RVSS
access: open            # open | paywalled | canvas | handout
---
```

`kind` is one of: `article`, `report`, `testimony`, `statute`, `bill`, `rule`,
`ethics_opinion`, `news`, `podcast`, `model_doc`, `case`, `case_study`.

`speaking_for` is one of: `funder`, `claimholder`, `law_firm`, `defense_bar`, `insurer`,
`academic`, `government`, `regulator`, `press`, `neutral`. **This field is not optional
and it is not decoration.** Half the syllabus is written by people with a position in the
market. A reading whose speaker is unrecorded is a reading you will misuse in seminar.

Body sections, in this order:

- **Claim** — the thesis, in one or two bullets. If the piece has no thesis (a market
  report, a bill), state what it establishes instead.
- **Argument** — how it gets from premises to claim. Bullets. The steps, not a summary.
- **Evidence** — the data, cases or transactions it rests on, **and how good they are**.
  Sample size, date, who funded the study, what it cannot show. An industry survey of
  thirty-nine funders is not a census.
- **Who is speaking** — prose. The author's institutional position, what they sell or
  regulate, and what they would lose if the opposite view prevailed. Never editorialise;
  state the interest and let it sit.
- **Where it goes** — which concept files and which position files this feeds, and **on
  which side** of each position. Wikilinks.
- **Seminar hooks** — exactly three bullets. Each is one of: a fact nobody else in the
  room will have, an internal tension in the reading, or a question you would put to the
  author. This section is 40% of the grade; write it last and write it best.
- **Citable detail** — quotes and figures worth pinning, each with a page or section
  locator, for the paper. Optional for short pieces; mandatory for anything over twenty
  pages. The final paper takes Chicago-style citations, so capture the locator now.
- **Professor gloss** — left empty. Owned by `session-reconcile`, never by the agent
  writing the reading file.

**Cases keep the root case schema** (root § 5, two layers). There are three:
Maslowski, Fast Trak, and In re Nimitz. They live in `10-readings/` alongside everything
else, with `kind: case`.

## 4. Concept file schema — FIXED

One file per structure or term, in `30-concepts/`. Named by the thing
(`Prepaid forward purchase agreement`, `Champerty and maintenance`, `Portfolio funding`).

```yaml
---
concept: Prepaid forward purchase agreement
topic: Transaction structuring
kind: instrument       # structure | instrument | actor | market | doctrine
class: legalfinance
sessions: [1, 5]
professor_emphasis:
confidence: 1
---
```

Body sections:

- **What it is** — one paragraph a non-specialist could follow.
- **How it works** — the mechanics. Who pays whom, when, on what trigger, in what
  priority. Bullets, and a table wherever there is a waterfall or a priority stack.
- **Why it exists** — the economic problem it solves, and for whom. A structure that
  survives in this market solves somebody's tax, accounting, ethics or risk problem;
  name it.
- **Variants** — the named flavours and what distinguishes them.
- **What can go wrong** — failure modes, with the transaction or dispute where each
  showed up.
- **Where it shows up** — wikilinks to the readings and sessions that discuss it.
- **Professor gloss** — empty, owned by reconcile.

## 5. Position file schema — FIXED

One file per contested question, in `50-positions/`. Named as the **question**, neutrally
framed, without a question mark (a trailing `?` is fine in a filename but reads badly in a
wikilink): `Disclosure of funding agreements`, `Funder control over settlement`.

```yaml
---
question: Should litigation funding agreements be disclosed in discovery?
topic: Regulation
status: live           # live | settling | resolved
class: legalfinance
sessions: [4, 8]
---
```

Body sections:

- **The question** — one sentence, framed so that both sides would accept the framing.
  A loaded question produces a useless file.
- **The case for** — the strongest version, made by someone who believes it. Attribute
  each strand to the reading that makes it.
- **The case against** — the same standard. If one side is visibly weaker on the page,
  the file is not finished.
- **What the evidence actually shows** — where the empirical claims on both sides come
  from and what they will and will not support. Usually the honest answer is "less than
  either side says," and saying so precisely is the seminar contribution.
- **Where the law is now** — jurisdiction by jurisdiction, with dates. This area moves
  fast enough that an undated statement of the law is wrong within a quarter.
- **My view** — **Ashwin's, and only Ashwin's.** An agent never writes in this section,
  never drafts a placeholder, and never summarises what he might think. It is left as a
  heading with nothing under it. This is the section the paper and the participation
  grade come out of, and a pre-filled view defeats the point of the course.

## 6. Session file schema

Root § 6 gives six prompts built for a doctrinal lecture. This is a two-hour seminar with
guest lecturers, group exercises and negotiation rounds. Same principle — fixed prompts,
raw capture, never cleaned up in place — different prompts:

1. What question was actually on the table
2. Where the room split, and on what
3. What Kelley pushed back on, and what he let stand
4. What a practitioner said that is not in any reading
5. Anything said about the assignments, the paper, or what he wants
6. Deal mechanics named but not explained — the follow-up list

## 7. Deals and paper folders

`60-deals/` is working material, not a generated view, and is exempt from the
never-hand-edit rule in root § 7. It holds term sheet anatomy, a clause bank with the
variants seen in the model documents, and one workspace per graded group assignment
(term sheets due Oct 13, funding agreements due Oct 27, negotiation exercise in Class 7).

`70-paper/` holds candidate topics with a one-line thesis each, a source bank, and drafts.
Topic is due to Kelley by **December 1, 2026**, presented in Class 9 on **December 2**,
paper due **March 22, 2027**.

## 8. Sourcing rules — specific to this class

- **The syllabus links are the source of truth for what was assigned.** Where a link has
  rotted, record the citation and the fact that the link is dead; never substitute a
  different edition or a summary and present it as the reading.
- **`access: canvas` and `access: handout` readings cannot be retrieved by an agent.**
  Six readings and all the model documents fall in this class. They are listed in the
  index with `access` set accordingly, and they stay unwritten until Ashwin supplies the
  file. Do not write a reading file from the title alone.
- **Paywalled trade press** (Bloomberg Law, WSJ) may be unretrievable. Same rule: no file
  from the headline.
- **Bills and statutes are moving targets.** Record the version and date read
  (`S. 1821, 119th Cong., as introduced May 2025`). A bill file that does not say which
  print it describes is worthless three months later.
- **Numbers get a date and a source.** "About 23% rebound in new commitments" is a
  Westfleet 2025 figure, not a fact about the market. Carry the vintage with the number
  everywhere it appears.
