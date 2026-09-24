# Con Law doctrine modules — build guide

You are writing doctrine modules for a UChicago Law 2L's Con Law I vault (Prof. William Baude, Autumn 2026). The reading files are at `/mnt/user-data/uploads/2L law-vault/conlaw/10-cases/` — 96 files, one per assigned reading, each with a brief or a note. **Build each module from those files.** Read every reading file assigned to your module before writing it. Do not invent doctrine, cases or quotations: everything must trace to a reading file (quotations in the reading files are already verified against the casebook).

The exam is in-class and closed-book, with cold-calling; devices are banned in class. The syllabus says Baude tests both "what the Supreme Court has said the Constitution means — i.e., the doctrine" and "what the Constitution actually requires — i.e., places the doctrine may be off track." A module that gives only doctrine is half-built.

## Schema — FIXED. Eight body sections, this order, no additions, no reordering.

```
## Rule statement
## Elements
## Standard of review / burden
## Exceptions
## Leading case
## Best counter-case
## Professor gloss
## Common trap
```

- **Rule statement** — prose, 2–5 sentences. The rule as you would state it in the first line of an exam answer. Where a field has competing formulations (doctrine vs. original meaning; plurality vs. dissent), state the operative rule first, then the contest in one sentence.
- **Elements** — a numbered list. The test, broken into the steps a court actually applies, each phrased so it can be checked off against facts. Where the doctrine is a framework rather than a test (Youngstown categories, modes of argument), number the categories. Sub-bullets are allowed under a numbered element for the factors inside it.
- **Standard of review / burden** — who bears what, and how hard the review is. Where no standard exists because the question is not justiciable or is answered by practice, say so plainly and say what fills the gap. Name the political-question route where it applies.
- **Exceptions** — bulleted. Carve-outs, safe harbours, and the situations where the rule does not run. Include the "not decided" gaps that matter for a hypothetical.
- **Leading case** — start with the wikilink on its own line, then 3–8 bullets: what it holds, the fact that drove it, and the sentence worth quoting. For a module whose anchor is a document rather than a case (the Decision of 1789, the Bank debate), use that reading.
- **Best counter-case** — the wikilink, then bullets: the case or reading that cuts the other way, the distinguishing fact, and how to argue each side. This section is where the exam points are.
- **Professor gloss** — LEAVE EMPTY. Heading only, no text, no placeholder. It gets filled after class.
- **Common trap** — bulleted. The wrong answer that sounds right, the overstatement of a holding, the case students cite for more than it says, the fact pattern that flips the result. Three to six bullets, each concrete.

## Frontmatter

Return it as JSON in the `.meta.json` file (a script writes the YAML):

```json
{"topic":"Separation of powers","sub_topic":"Art. II § 1 — the Youngstown categories and presidential power",
 "authority":["U.S. Const. art. II, § 1","U.S. Const. art. II, § 3","common law"],
 "professor_emphasis":3,"exam_likelihood":"high"}
```

- `topic` — the syllabus-level bucket: Separation of powers · Legislative power · Executive power · Judicial power · Federalism · Article IV · Amendment process · Constitutional interpretation.
- `sub_topic` — **lead with the governing provision**, then the doctrine: "Art. I § 8 cl. 3 — the substantial-effects test and its limits".
- `authority` — every provision the module rests on, in citation form (`U.S. Const. art. I, § 8, cl. 18`; `50 U.S.C. §§ 1541–1548` for the War Powers Resolution; `Del.`-style statutes do not arise here). A module resting on no enacted text takes the single entry `common law` — that is a real answer, not a blank. This field is queried across the vault, so be exact.
- `professor_emphasis` — 1–3, your first-pass prediction from the syllabus's weighting (how many classes, whether Baude wrote about it).
- `exam_likelihood` — high | medium | low, same basis.

## House style

- **No meta-commentary.** Never describe the file or the section inside it.
- One idea per bullet; MECE; name the antecedent rather than "it" or "this".
- **Wikilink every case and reading name**, using the exact file names in `10-cases/`. Never break a wikilink across a line. No link target ends in a period.
- **No hard wrapping**: each paragraph and each bullet is a single line, however long.
- Quote sparingly and exactly, taking quotations only from the reading files.
- Cross-link sibling modules by name where a doctrine hands off to another (the module names are listed in your prompt).

## Output

For each module write two files into the directory named in your prompt:
`<Exact Module Name>.body` (body only, starting at `## Rule statement`) and `<Exact Module Name>.meta.json`.

Before finishing: all eight headings present in order; Professor gloss empty; no wikilink contains a newline; every case name you link exists in `10-cases/` (check with `ls`); JSON parses. Report briefly: modules written, anything you could not source from the readings, and any judgment calls.
