# legalfinance — class override

Root `CLAUDE.md` is the format law for this repo. This file overrides it **for this
folder only**. Where the two conflict, this file wins inside `legalfinance/`. Where this
file is silent, the root governs — frontmatter is still `snake_case`, wikilinks are still
mandatory, house style is unchanged, and the guardrails in root § 8 apply everywhere.

---

## 1. Why this class diverges

BusOrg and Con Law are built for a closed-book exam, and for a room where no device is
allowed. Those two facts are why the repo has `20-sessions/` and a reconcile step: capture
and synthesis are forced apart, so raw dictation lands first and doctrine modules are
updated later.

**Neither fact holds here.** There is no exam — 40% engagement and participation, 35%
group assignments, 25% an individual ~15-page paper. And devices are allowed, so notes can
be typed live. Capture and synthesis happen in the same keystroke, which removes the
entire capture-then-reconcile pipeline. There is no `20-sessions/` in this class and no
reconcile pass; notes go straight into the file they belong to.

The readings are a different species too. Nine classes, forty-six readings, of which
**three are cases**. The rest are law review articles, government reports, congressional
testimony, pending bills, bar ethics opinions, firm client alerts, trade press and one
podcast. Many are **advocacy**. A schema built to extract a holding extracts nothing from
a funder white paper.

> Notes enter indexed by **date**. They must leave indexed by **argument** and by
> **structure** — the contested question, and the deal mechanic.

`30-concepts/` and `50-positions/` are the assets. `60-deals/` and `70-paper/` are the
work product. `00-source/` and `10-readings/` are input.

## 2. Directory contract — this folder

```
legalfinance/
  00-source/      syllabus, downloaded readings, model documents — read-only
  10-readings/    one subfolder per class meeting; live class notes land here too
  30-concepts/    what a thing IS — structures, instruments, actors, mechanics
  40-professor/   Kelley, guest lecturers, what he rewards
  50-positions/   what is CONTESTED — one file per live question, both sides
  60-deals/       term sheet anatomy, clause bank, the three group assignments
  70-paper/       final project — candidate topics, source bank, drafts
  99-meta/        reading index and the generated workbook
```

**`10-readings/` is filed by class meeting**, one numbered subfolder each —
`01 - Rationale and economics`, `02 - Claimholder, firm and investor perspectives`, through
to `09`. Each holds that week's four to six readings, because that is the unit of
preparation: one seminar, one folder.

This is the opposite of the choice made in BusOrg, and deliberately. There, date folders
were rejected because a case assigned twice cannot live in two of them. **No reading on
this syllabus is assigned to more than one class**, so the conflict never arises. And
`10-readings/` is *input*, which the core rule already says arrives indexed by date; the
assets in `30-concepts/` and `50-positions/` are what must leave indexed by argument, and
those stay flat.

Wikilinks are path-independent, so `[[Burford - Legal Finance 101]]` resolves from anywhere
no matter which class folder holds it. Note names must therefore stay **unique vault-wide**,
as Obsidian requires and as `index_to_xlsx.py` assumes when it walks subfolders looking for
a reading's note.

No `20-sessions/`. Live class notes go into the reading being discussed, under
`## In seminar`. Material that attaches to no reading has two homes: exercise and
negotiation material goes to `60-deals/`, and what a practitioner or guest lecturer said
goes to `40-professor/`.

## 3. Reading file schema — two tiers

One file per assigned reading, in that class's subfolder of `10-readings/`, named by a
short human title (`Bedi and Marra - The Shadows of Litigation Finance`), never by
citation.

```yaml
---
reading: The Shadows of Litigation Finance
author: Suneal Bedi & William C. Marra
kind: article
publication: 74 Vand. L. Rev. 563
year: 2021
class: legalfinance
session: 1
read_for: 2026-09-30
topic: Rationale and economics
speaking_for: academic
feeds_concept:
  - "[[Concept name]]"
feeds_position:
  - "[[Question name]]"
url: https://bit.ly/3C7RVSS
access: open
---
```

`kind`: `article`, `report`, `testimony`, `statute`, `bill`, `rule`, `ethics_opinion`,
`news`, `podcast`, `model_doc`, `case`, `case_study`.

`access`: `open`, `paywalled`, `canvas`, `handout`.

`speaking_for`: `funder`, `defense_side`, `practitioner`, `academic`, `government`,
`press` — or **left blank where nobody is advocating**, as with a court opinion or a model
document. **This field is not decoration.** Most of this syllabus is written by people with
a position in the market; a reading whose speaker is unrecorded is one you will misuse out
loud. Where an author sits in more than one camp, record the one that pays them and say so
in the body.

**Tier the body to the reading.** Roughly fourteen readings are substantial articles and
reports and get the full form. The rest — news items, firm alerts, blog posts, case
studies, short rules — get the short form. Do not run seven headings over an 800-word
news piece.

### Full form

- **Claim** — the thesis in one or two bullets. Where a piece has no thesis (a market
  report, a bill), state what it establishes instead.
- **Argument** — the steps from premises to claim. Bullets. Steps, not summary.
- **Evidence** — what it rests on **and how good that is**. Sample size, date, who funded
  the study, what it cannot show. A survey of thirty-nine funders is not a census.
- **Who is speaking** — prose. The author's position in the market, what they sell or
  regulate, and what they lose if the other side wins. State the interest; do not
  editorialise.
- **Where it goes** — which concepts and which positions this feeds, and **on which side**
  of each. Wikilinks.
- **Seminar hooks** — exactly three bullets. Each is a fact nobody else will have, a
  tension inside the reading, or a question for the author. This section is the
  participation grade; write it last and write it best.
- **Citable detail** — quotes and figures worth pinning, each with a page or section
  locator. The paper takes Chicago-style citations, so capture the locator now.
- **In seminar** — empty until class. Typed live.

### Short form

- **Claim** — what it says, in two or three bullets.
- **Who is speaking** — one or two sentences.
- **Seminar hooks** — one to three bullets.
- **In seminar** — empty until class.

**Cases keep the root case schema** (root § 5, two layers), with `kind: case`, and live in
their class folder with everything else. There are three: Maslowski and Fast Trak in
Class 4, In re Nimitz in Class 8.

## 4. Concept file schema

One file per structure or term, in `30-concepts/`, named by the thing
(`Prepaid forward purchase agreement`, `Champerty and maintenance`).

```yaml
---
concept: Prepaid forward purchase agreement
topic: Transaction structuring
kind: structure        # structure | instrument | actor | market | doctrine
class: legalfinance
sessions: [1, 5]
---
```

- **What it is** — one paragraph a non-specialist could follow.
- **How it works** — the mechanics. Who pays whom, when, on what trigger, in what
  priority. A table wherever there is a waterfall or a priority stack.
- **Why it exists** — the problem it solves, and for whom. A structure that survives in
  this market solves somebody's tax, accounting, ethics or risk problem. Name it.
- **Variants** — the named flavours and what separates them.
- **What can go wrong** — failure modes, each with the transaction or dispute where it
  showed up.
- **Where it shows up** — wikilinks to the readings that discuss it.

Keep these short. Most entries here are vocabulary you need to recognise in a room, not
doctrine you need to reconstruct from memory. A concept file that runs past a screen is
either a position file in disguise or belongs in `60-deals/` with the drafting work.

## 5. Position file schema

One file per contested question, in `50-positions/`, named as the question without a
question mark (`Disclosure of funding agreements`, `Funder control over settlement`).

```yaml
---
question: Should litigation funding agreements be disclosed in discovery?
topic: Regulation
status: live           # live | settling | resolved
class: legalfinance
sessions: [4, 8]
---
```

- **The question** — one sentence, framed so both sides would accept the framing. A loaded
  question produces a useless file.
- **The case for** — the strongest version, made by someone who believes it. Attribute
  each strand to the reading that makes it.
- **The case against** — the same standard. If one side is visibly weaker on the page, the
  file is not finished.
- **What the evidence actually shows** — where the empirical claims come from and what
  they will and will not support. The honest answer is usually "less than either side
  says," and saying so precisely is the seminar contribution.
- **Where the law is now** — jurisdiction by jurisdiction, with dates. This area moves
  fast enough that an undated statement of the law is wrong within a quarter.
- **My view** — **Ashwin's, and only Ashwin's.** An agent never writes here, never drafts
  a placeholder, never summarises what he might think. It stays a heading with nothing
  under it. This is where the paper and the participation grade come from.

## 6. Deals and paper

`60-deals/` is working material, not a generated view, and is exempt from the
never-hand-edit rule in root § 7. It holds term sheet anatomy, a clause bank of the
variants seen in the model documents, and one workspace per graded assignment — term
sheets due **Oct 13**, funding agreements due **Oct 27**, negotiation exercise in Class 7
on **Nov 11**.

`70-paper/` holds candidate topics with a one-line thesis each, a source bank, and drafts.
Topic due to Kelley **Dec 1, 2026**; presented in Class 9 on **Dec 2**; paper due
**Mar 22, 2027**.

## 7. Sourcing rules

- **The syllabus links are the source of truth for what was assigned.** Where a link has
  rotted, record the citation and the fact that it is dead. Never substitute a different
  edition or a summary and present it as the reading.
- **`access: canvas` and `access: handout` readings cannot be retrieved by an agent** —
  seven of them, including every model document. They stay unwritten until Ashwin supplies
  the file. Paywalled trade press may be unretrievable for the same practical reason. **No
  reading file is ever written from a title alone.**
- **Bills and statutes are moving targets.** Record the print and date read
  (`S. 1821, 119th Cong., as introduced May 2025`). A bill file that does not say which
  version it describes is worthless in three months.
- **Numbers carry a vintage.** "About a 23% rebound in new commitments" is a Westfleet
  2025 figure, not a fact about the market. Carry the source and the year everywhere the
  number appears.
