---
name: doctrine-module
description: Create or update a rule module in 30-doctrine against the fixed schema in CLAUDE.md section 4. Use when a case brief needs a module to point at, when a statute or rule reading needs a home, or when asked to build out the doctrine layer for a class. Modules are the asset; everything else in the vault is input to them or a generated view of them.
---

# doctrine-module

Writes one file to `<class>/30-doctrine/<Rule name>.md`.

`30-doctrine` is the asset this vault exists to build. `10-cases` and
`20-sessions` are inputs to it; `50-outline` and `60-drills` are generated views
of it. A module is organised by **rule**, never by case and never by class date.

`CLAUDE.md` is authoritative for the schema, the field-ownership table and the
house style. This file is the procedure.

## Two ways a module gets created

**From a case.** A case brief's `feeds_module` names a module. If that module
does not exist, create it. The case becomes the `Leading case` — or, if a leading
case is already there, the module absorbs the new case as a counter-case, an
exception, or a refinement of an existing element.

**From a statute or rule.** A reading whose `kind` in `case-index.json` is
`statute`, `rule`, `document`, or `note` has no opinion to brief and never
produces a case file. It produces a module built from the text of the provision
itself. Twenty-two of the seventy BusOrg readings take this path, including
§§ 144 and 220 in both their pre- and post-SB 21 forms.

For a statute module:

- **Pull the text with the extractor**, never from memory:

  ```
  python3 .claude/skills/doctrine-module/scripts/extract_statute.py 141 --sub a
  python3 .claude/skills/doctrine-module/scripts/extract_statute.py 144 --source dgcl144post
  python3 .claude/skills/doctrine-module/scripts/extract_statute.py 23.1 --source chancery
  python3 .claude/skills/doctrine-module/scripts/extract_statute.py 14 --source sea34
  ```

  Sources: `dgcl`, `dgcl144pre`, `dgcl144post`, `dgcl220pre`, `dgcl220post`, `sb21`,
  `chancery`, `sea34`. `--list` prints every heading in a source.

- **Quote the operative language, tightly.** A paraphrase of a statute is a
  different statute, so never paraphrase — but never reproduce a whole subsection
  either. Quote the phrase that does the work and summarise the scaffolding around
  it in your own words, clearly marked as such. The exam is closed-book and
  word-limited; a block paragraph of statutory text is dead weight on exam day and
  will not be reproduced from memory. A quoted fragment of a dozen words that
  decides cases is worth more than a full subsection.
- **Where a provision opens with a cross-reference, quote it.** "Notwithstanding
  § 141(a) of this title" is the entire significance of § 122(18).
- `Elements` come from the structure of the provision: its subsections,
  conditions, and safe harbours.
- `Leading case` is the case that construes the provision, if one is assigned. If
  none is, say so plainly rather than reaching for an unassigned case.
- Where the syllabus assigns a provision in **both** a pre- and post-amendment
  form, that pairing is the point. Build one module covering the provision, with
  the two versions set against each other and the change stated explicitly: what
  the amendment added, what it removed, and which prior holdings it displaces.
  A professor who assigns the same statute twice in two versions is telling you
  what the exam is about.

## Naming

The filename is the **rule**, in plain words, not the case and not the statute
number: `Duty of care - informed decision.md`, not `Van Gorkom.md` and not
`144.md`. A reader scanning `30-doctrine` should see a list of legal propositions.

One file per rule. If a provision carries two genuinely separate rules, write two
modules and link them.

## Section order — fixed, no additions, no reordering

1. `## Rule statement` — prose. What the rule is, and what rebutting or
   satisfying it does procedurally.
2. `## Elements` — numbered. Where an element needs explaining, explain it under
   that element with a bolded lead-in and bullets beneath. State what falls
   **outside** an element and where such a case routes instead; the boundaries
   are where exam questions live.
3. `## Standard of review / burden` — a table. Presumption, who carries the
   burden, the standard, what happens if the burden is carried, and what is never
   reviewed.
4. `## Exceptions` — bulleted, each with its statutory or case source, and the
   practical consequence of the exception rather than only its text.
5. `## Leading case` — wikilink plus one or two lines on the facts that made the
   case the leading one.
6. `## Best counter-case` — wikilink, plus the **distinguishing line** stated as a
   single sentence a reader can apply to a new fact pattern. This sentence is the
   raw material for line-drawing drills and is the most valuable line in the file.
7. `## Professor gloss` — **empty**. No placeholder, no comment. Written only by
   `session-reconcile`, from the class debrief.
8. `## Common trap` — numbered. What gets written that earns nothing, what gets
   confused with what, and which follow-on question a fact pattern forces.

## Frontmatter and who owns it

```yaml
topic:               # string
sub_topic:           # string
professor_emphasis:  # 1-3, first pass at creation
exam_likelihood:     # high | medium | low, first pass at creation
confidence: 1        # initialise to 1; never write this field again
last_drilled:        # leave empty
```

- `professor_emphasis` and `exam_likelihood` get a **first pass** at creation,
  from the syllabus and the professor file. After creation only
  `session-reconcile` may revise them. Do not revise them from this skill.
- `confidence` is a self-rating. Write the initial `1`, meaning "not yet rated,"
  and never touch the field again.
- `last_drilled` belongs to `exam-drill`.

## Updating an existing module

Modules are long-lived and get edited far more often than they get created.

- **Add, do not replace.** A new case that refines an element goes into that
  element. A new case that cuts against the rule goes to `Best counter-case` or
  `Exceptions`.
- **Never overwrite `Professor gloss`.** That section belongs to
  `session-reconcile` and holds accumulated class evidence.
- **Never revise `confidence`**, and never revise the two prediction fields.
- Where a new source **contradicts** what the module already says, do not
  silently pick a winner. Keep both, mark the tension, and flag it for the human.
  A contradiction between a reading and what the professor said in class is
  signal, not noise, and resolving it quietly destroys the signal.

## House style

- **No meta-commentary.** A section never narrates its own purpose.
- Bullets for Elements, Exceptions, and Common trap. Prose for Rule statement.
- One idea per bullet. MECE.
- Name the antecedent rather than writing "it," "this," or "that."
- **Wikilink every case name and every module name**, with a display alias for
  long names: `[[In re Caremark International Inc. Derivative Litigation|Caremark]]`.
  Backlinks are how the graph connects doctrine to cases, and that graph is the
  point of keeping these files in Obsidian.
- **Never let a wikilink wrap across a line break.** Obsidian silently fails to
  resolve a link containing a newline.

## Readings marked {skim}

The syllabus marks some readings to skim. Do not summarise the document. Identify
the provisions that **do work for this course** and say what to notice about each,
then stop. A governance document is mostly machinery; the exam-relevant content is
usually a handful of provisions and one or two asymmetries between them.

For a charter or bylaws, read for **elections and variances**, not for content: at
each provision ask what the statutory default is and what this document does
instead. The gap is the fact worth recording. Vestigial or stale text is worth a
line — instruments drift, and noticing the drift is the skill.

## Refusals

- The rule is not actually in the source — say so rather than supplying it from
  background knowledge. A module that states law the assigned reading does not
  contain is worse than a missing module, because nothing marks it as unverified.
- Two rules are fighting for one file — write two modules and say so.
- A statute's operative language is ambiguous and the assigned reading does not
  resolve it — state the ambiguity in the module rather than choosing a reading.

## Before finishing, check

1. All eight sections present, in order.
2. `Professor gloss` empty — no placeholder, no comment.
3. `confidence: 1` and `last_drilled` empty.
4. Filename names the rule, not the case and not the statute number.
5. `Best counter-case` contains one applicable distinguishing sentence.
6. Every case mentioned anywhere in the file is a wikilink.
7. No wikilink wraps across a line.
8. For a pre/post statute pair: the change is stated explicitly — added, removed,
   and displaced.
9. Statutory language is quoted, not paraphrased.
