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
  10-cases/       one file per assigned READING — cases and documents alike
  20-sessions/    one file per class meeting, raw capture, date-named
  30-doctrine/    rule modules — the master DB
  40-professor/   instructor profile, past exams, hypo bank
  50-outline/     master -> attack -> one-pager/scaffold (generated)
  60-drills/      question bank, error log, timed attempts
  99-meta/        class-specific schema overrides and prompts
```

Classes: `busorg/` (Buccola), `conlaw/` (Baude), `legalfinance/` (Kelley).
Legal Finance is deliberately deferred — scaffolded, not populated.

Repo-wide utilities that no single skill owns live in `.claude/scripts/`. A
script that is one skill's deterministic sub-step lives in that skill's own
`scripts/` folder instead.

Skills are repo-scoped and live in `.claude/skills/<name>/SKILL.md`. Professor-
specific behavior lives in the **data** (`40-professor/`), never in forked skill
code. If you find yourself writing `if professor == "Baude"` into a skill, the
thing you are encoding belongs in a professor file instead.

## 3. Frontmatter keys — underscores, always

**Every frontmatter key in this vault uses `snake_case`. No hyphens. Ever.**

This is not style. In Dataview, a bare hyphen in an expression parses as
subtraction: `professor_emphasis >= 2` works, `professor-emphasis >= 2` silently
returns nothing — and an empty table looks exactly like a passing one. A query
that fails loudly is recoverable; one that returns zero rows in November is not.

## 4. Doctrine module schema — FIXED

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
sub_topic:           # string — lead with the governing provision where one exists
authority:           # list — every provision this module is built on
  - 8 Del. C. § 141(a)
professor_emphasis:  # integer 1-3
exam_likelihood:     # high | medium | low
confidence:          # integer 1-5, self-rated, human-set only
last_drilled:        # YYYY-MM-DD or null
```

**`authority` is required on every module.** It carries the section numbers the
module is built on, so the governing provision is visible the moment the file opens
and is queryable across the whole vault. A module resting on no statute takes the
single entry `common law`; that is a real answer, not a blank. `sub_topic` leads
with the provision as well, so the pairing is visible in a file listing.

Never let a section number live only in the body. Remembering which statute goes
with which doctrine is itself exam content.

This frontmatter is the study queue. Dataview reads it. If it drifts, the queue
breaks silently.

### Who owns which field

Three of these fields describe things no one can know when the module is
created. The rule is who is allowed to *revise* them, not who types them first.

| Field | Set at creation by | Revised by |
|---|---|---|
| `topic`, `sub_topic` | whoever creates the module | anyone, on correction |
| `professor_emphasis` | first pass, from the syllabus and the professor file | **`session-reconcile` only**, from what was actually said in class |
| `exam_likelihood` | first pass, same basis | **`session-reconcile` only** |
| `confidence` | initialized to `1` | **the human only** |
| `last_drilled` | empty | `exam-drill`, on a completed attempt |

`professor_emphasis` and `exam_likelihood` are predictions before the class
happens and evidence afterwards. A first pass at creation is fine and keeps the
module inside the Dataview queue from day one. What is not fine is any skill
other than `session-reconcile` quietly revising them later — the whole value of
those numbers is that they track what the professor did, and a second writer
with a different basis destroys that.

`confidence` is a **self-rating**. An agent may write the initial `1`, meaning
"not yet rated," and may never touch it again. An agent inferring how well you
know something defeats the entire purpose of the field, and it is the field the
drill queue leans on hardest.

### Statutes and rules

A reading that is a statute, a rule, or a governance document has no opinion to
brief and therefore never produces a case file. It produces a **doctrine module**
instead, created directly from the text of the provision.

Such a module is created with its body populated from the provision itself and
its `professor_emphasis` and `exam_likelihood` set on a first pass. Class
treatment of the provision arrives later, through `session-reconcile`, which
polishes the module the same way it polishes any other. A statute with no module
is a silent gap in the doctrine layer — 22 of the 70 BusOrg readings are
statutes, rules, or governance documents.

## 5. Case file schema — FIXED

Two layers in one file.

- The **brief layer** is the extraction that survives into `30-doctrine` and must
  still be true in December.
- The **class layer** is cold-call prep against the opinion. It is allowed to
  decay after the class meeting has passed.

The brief layer leads. If the class layer stops getting filled in by week six,
the file is still doing its job.

```yaml
case:                  # short name, matches the filename
citation:
court:
year:
class:                 # busorg | conlaw | legalfinance
topic:
feeds_module:          # wikilink(s) to the doctrine module(s) this case supports
read_for:              # YYYY-MM-DD, the class meeting it was assigned for
posture_drove_outcome: # true | false
```

### Brief layer

1. **Rule** — one sentence. What this case adds to the doctrine that was not
   already there. "Nothing — illustration of [[X]]" is a legitimate answer.
2. **Facts** — bulleted, and **pivotal facts only**. A fact earns a place here if
   it decided the case, if the issue or the ruling turns on it, or if changing it
   would change the result. That last test is the important one: these are the
   facts a hypothetical can be built on, which is what makes this section the
   input to line-drawing drills.
   A fact the court discussed and then explained away still belongs here, with
   its fate noted in italics — the premium in [[Smith v. Van Gorkom]] lost, but a
   hypothetical in which the board had both a premium and a valuation comes out
   differently, so the premium is pivotal.
   Background, narrative, and good-to-know detail go to the class layer instead.
   Do not repeat them here.
3. **Court Ruling** — bulleted, in two groups: what the court **held**, and what
   the court **rejected**. State a rejected argument at its strongest before
   giving the court's answer to that argument.
4. **Context** — prose is fine here, and wikilinks are expected. The neighboring
   cases, the distinguishing fact between this case and each neighbor, the
   statutory or legislative response, and anything else that does not fit the
   three sections above but that a reader in December would want.
5. **Professor gloss** — filled in after class, not before. Empty until then.

### Class layer

Below a `---`. In this order:

- **Posture** — light. One or two bullets.
- **Facts** — prose, and the **full narrative**: background, how the parties got
  there, procedural colour, and the good-to-know detail that did not decide
  anything. Prose beats bullets here because narrative packs more densely without
  bullet overhead. The brief layer holds the pivotal facts; this section holds
  everything else worth knowing, and does not restate the pivotal ones except
  where the story is unintelligible without them.
- **Issue** — bulleted. Multiple issues get multiple bullets.
- **Holding** — bulleted, one bullet per issue, in the same order as the issues.
  Each bullet states the disposition and what it turned on. Never a compressed
  answer like "no on both" that forces the reader back up the page.
- **Rule** — bulleted. Deliberately redundant with the brief layer's Rule; it
  belongs here so the class layer reads as a complete brief on its own.
- **Reasoning** — bulleted. Name the judge in parentheses where the judge is
  notable.
- **Dissent / concurrence** — bulleted main points, judge named in parentheses.
  Where the panel was unanimous, say so in one line and stop. Add a short sketch
  of what could have been argued **only where there is genuinely something to
  say** — a real tension the opinion papers over, not a manufactured objection.
  Two or three lines at most. Most unanimous opinions get one line and nothing
  else.
- **Cold-call notes** — what will be asked, what to be ready to be pushed on, and
  what is easy to get wrong under pressure. Elaborate; this section earns space.

### Document readings — a lighter schema

Not every assigned reading is a case. A charter, a set of bylaws, or a casebook
note has no opinion to brief, but it is still a reading, and it gets its own file in
`10-cases/` alongside the cases. One place per reading means the by-class-meeting
view is complete, progress tracking covers everything assigned, and a document
feeding two modules is not split between them.

Document notes take a **light** schema, not the two-layer case schema:

```yaml
reading:        # name, matching case-index.json
kind:           # document | note
source:         # the file in 00-source, or where it came from
class:          # busorg | conlaw | legalfinance
topic:
feeds_module:   # wikilink(s)
read_for:       # YYYY-MM-DD
```

Body, three sections only:

1. **What it is** — a few lines. Enough that a reader in December knows what the
   document is and why it was assigned.
2. **What to notice** — bulleted. The provisions that do work for this course, each
   with the statutory default it varies where there is one. This is the section that
   earns its keep; everything else in a governance document is machinery.
3. **Where it goes** — the modules this reading feeds, as wikilinks.

A reading marked `{skim}` on the syllabus gets the same treatment. Skim means
**notice selectively**, not summarise briefly.

## 6. Session file schema — FIXED

One file per class meeting, named `YYYY-MM-DD.md`, in `<class>/20-sessions/`.
Captured within ~20 minutes of class, by dictation, against the same six prompts
every time:

1. What doctrine was on the table
2. What hypo he posed, and what he was fishing for
3. Where he pushed back on a student
4. What he called the hard case
5. What he said doesn't matter
6. Any exam signal

The six prompts are fixed so that capture is comparable across weeks and
machine-readable without parsing prose. Session files are **raw capture**. They
are never cleaned up in place, never rewritten to read better, and never deleted
after reconciliation — they are the audit trail behind every doctrine module.

## 7. Format law

- **Never freehand frontmatter.** A deterministic transform (OCR, tagging, an
  API call) asks a model for JSON against a schema, validates that JSON in a
  script, and lets the *script* write the YAML. A model writing YAML directly
  will eventually invent a key, and nothing will error.
- **Plain markdown is the source of truth.** Obsidian is a viewer. Gemini and
  NotebookLM are compute pointed at this vault. Neither is a second vault.
- **Generated files are never hand-edited.** Outlines and PDFs are regenerated
  from source. Editing a generated file means the next regeneration silently
  discards the edit.
- **Wikilinks over paths.** `[[Meinhard v. Salmon]]`, not a relative path. Every
  case name and every module name mentioned in any file is a wikilink. The graph
  view is how doctrine connects to cases, and an unlinked mention is invisible
  to the graph.
- **Statutes and rules get doctrine modules, not case files.** A reading with no
  opinion to brief still states law. See section 4.
- One file per case. One file per class meeting. One file per rule.

### House style

These are not preferences. A file that violates them is wrong and gets rewritten.

- **No meta-commentary.** Never narrate a section's own purpose inside that
  section — no "only the facts that did work," no "what follows is," no
  explaining the template back to the reader. The heading already says what the
  section is. Output files are read under time pressure; a sentence about the
  file's own construction is noise.
- **Bullets by default** for Issue, Holding, Rule, Elements, and Court Ruling.
  Prose for Facts and Context, where detail flows and bullets fragment it.
- **MECE.** Bullets in one list do not overlap and together cover the ground.
- **One idea per bullet.** No compression that has to be read twice.
- **Name the antecedent.** Prefer the noun to "it," "this," or "that," even when
  the noun is longer. A pronoun three clauses from its referent costs the reader
  more than the extra words cost.
- **Name the judge** in parentheses for reasoning and dissent where the judge is
  notable — more often relevant in Con Law than in BusOrg.

## 8. Guardrails

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

## 9. Open — do not silently resolve

These are unsettled. An agent that picks a default here and proceeds has made a
decision that was the human's to make. Ask.

- Scheduling mechanism for the nightly job: local cron/launchd (needs a `pmset`
  wake schedule) vs. cloud Routines (needs the private remote, restricted to
  `claude/`-prefixed branches).
- Whether Harvey gives clean-enough Delaware corporate authority to shortcut the
  BusOrg case layer — test on three cases before designing around it.
- Legal Finance's exam-day tool (Exam4 kills the network; local Ollama was the
  sketch). Out of scope until the seminar's needs are clearer.
- Per-skill prompts. The charter is the spec, not the implementation.
