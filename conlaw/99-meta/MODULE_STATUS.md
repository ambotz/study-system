# Con Law doctrine modules — status

**Complete, and revised 2026-09-25.** All 31 modules are built, validated and committed to `conlaw/30-doctrine/`.

## 2026-09-25 clarity and accuracy pass

- Every module was re-checked against its reading files, the 4th-ed. casebook text and the 5th-ed. print packets. Misquotations, misattributions, overstated holdings and wrong votes were fixed; missing readings, elements and original-meaning critiques were added from the sources.
- Every module was restructured for absorption: a plain-English first sentence in the Rule statement, bold-question Elements, labelled bullets in Standard of review (Presumption / Burden / Standard / Not reviewed / What fills the gap), a one-sentence **Distinguishing line** at the top of Best counter-case, and Common traps that lead with the tempting wrong answer.
- An automated check of 1,233 quoted passages across the modules found every one in the casebook, the packets or a reading file (bracket and capitalisation differences aside).
- Frontmatter untouched except the two topic moves below. `Professor gloss` is still empty in all 31; `confidence` is still `1`.
- Errors found in the *reading files* were not fixed in place; they are listed in `READING_FIXES.md` for the vault-wide pass.


This replaces `MODULE_HANDOFF.md`, which described 15 modules as pending. The build procedure and the schema spec live in `MODULE_GUIDE.md`, which stays — it is what a future module or a rewrite should follow.

## Validation run against the vault

Every one of the 31 passes:

- the eight body sections present, in the guide's exact order
- `## Professor gloss` empty in all 31 — that section is filled after class, by you
- `confidence: 1` and `last_drilled:` empty in all 31 — `confidence` is yours alone to change
- every frontmatter key present: `topic`, `sub_topic`, `authority`, `professor_emphasis`, `exam_likelihood`
- zero broken wikilinks — every linked case resolves to a real file in `10-cases/`, every module cross-link to a real module
- no wikilink split across a line, no link target ending in a period, no hard-wrapped prose

`by-class.md` and `case-index.xlsx` are regenerated and have no unresolved module references.

## The 31 modules

**Constitutional interpretation (3)**
| Module | Emphasis | Exam |
|---|---|---|
| Judicial supremacy and departmentalism - Art. VI oath | 3 | high |
| Modes of constitutional argument | 3 | high |
| Constitutional themes and the dead hand | 1 | low |

**Separation of powers (2)**
| Module | Emphasis | Exam |
|---|---|---|
| Separation of powers - vesting clauses and checks and balances | 3 | high |
| War powers - Art. I § 8 cl. 11 and the Commander in Chief | 3 | high |

**Executive power (6)**
| Module | Emphasis | Exam |
|---|---|---|
| Enforcement discretion - Art. II § 3 Take Care | 3 | high |
| Presidential immunity and privilege - Art. II | 3 | high |
| Presidential power - Art. II and the Youngstown categories | 3 | high |
| Removal - Art. II § 1 and the Humphrey's exception | 3 | high |
| Appointments - Art. II § 2 cl. 2 and the officer line | 2 | medium |
| Impeachment - Art. II § 4 high crimes and misdemeanors | 2 | medium |

**Legislative power (5)**
| Module | Emphasis | Exam |
|---|---|---|
| Bicameralism and presentment - Art. I § 7 | 3 | high |
| Nondelegation - Art. I § 1 and the intelligible principle | 2 | high |
| The power of the purse - Art. I § 9 cl. 7 appropriations | 2 | high |
| Suspension of habeas corpus - Art. I § 9 cl. 2 | 2 | medium |
| Bills of attainder - Art. I § 9 cl. 3 | 1 | low |

**Federalism (8)**
| Module | Emphasis | Exam |
|---|---|---|
| Commerce power - Art. I § 8 cl. 3 | 3 | high |
| Enumerated powers and the Necessary and Proper Clause - Art. I § 8 cl. 18 | 3 | high |
| Nature of the Union - compact theory, nationalism and secession | 3 | high |
| State sovereignty and anti-commandeering - Tenth Amendment | 3 | high |
| Spending power - Art. I § 8 cl. 1 general welfare and conditional grants | 2 | high |
| Taxing power - Art. I § 8 cl. 1 and direct taxes | 2 | high |
| Dormant Commerce Clause - Art. I § 8 cl. 3 and state discrimination | 2 | medium |
| Supremacy and the oath - Art. VI | 2 | medium |

**Judicial power (3)**
| Module | Emphasis | Exam |
|---|---|---|
| Judicial review - Art. III and the Supremacy Clause | 3 | high |
| Congressional control of the courts - Art. III jurisdiction and court size | 2 | medium |
| Standing - Art. III § 2 cases and controversies | 2 | medium |

**Article IV (3)**
| Module | Emphasis | Exam |
|---|---|---|
| Privileges and immunities - Art. IV § 2 and state discrimination | 2 | low |
| Republican government - Art. IV § 4 Guarantee Clause | 2 | medium |
| Territories and citizenship - Art. IV § 3 and Dred Scott | 2 | medium |

**Amendment process (1)**
| Module | Emphasis | Exam |
|---|---|---|
| Amendment process - Art. V | 2 | medium |

`professor_emphasis` and `exam_likelihood` are first-pass predictions from syllabus weighting. They are `session-reconcile`'s to revise once you've been in class, not something to trust cold.

## The three follow-ups from the first build — resolved 2026-09-25

1. **Topic buckets.** *Taxing power* moved to **Federalism**, beside Spending and Commerce (syllabus Part II). *Suspension of habeas corpus* moved to **Legislative power**, beside Bills of attainder (§ 9 limits Congress).
2. **Territories and citizenship** now has inbound links from Nature of the Union, Judicial review, Judicial supremacy and Modes of constitutional argument.
3. **Unlinked authority.** Twenty brief-only stub files were added to `10-cases/`, each marked `> [!note] Not assigned` with `read_for: null` and built only from the casebook: Myers, Morrison, Seila Law, Free Enterprise Fund, Heckler v. Chaney, Gibbons, E.C. Knight, Jones & Laughlin, Schechter Poultry, J. W. Hampton, McCray, Kahriger, Butler, Steward Machine, Helvering v. Davis, New York v. United States, Comstock, Luther v. Borden, Coleman v. Miller, Martin v. Hunter's Lessee. The modules now wikilink them. *United States v. Klein* and *Ex parte Yerger* got no stub because neither is in the casebook or packets; the Congressional control module labels them as outside the assigned readings. The 0-byte stray `J. W. Hampton…md` at the repo root was deleted.

## Still open, unchanged

- **Class 5 "Additional Materials"** — index entry with no file.
- **Class 27 Canvas packet** ("and other materials") — contents unknown.
- **Power of the Purse — additional materials** — the one index entry the xlsx still reports as missing a file.
- **Pork Producers' Kavanaugh opinion** — never retrieved; his Privileges and Immunities discussion is the passage that would most help the Art. IV module.
- **Trump v. Slaughter / Trump v. Cook dissents** (Sotomayor, Alito, Barrett) — not retrievable; Removal and Separation of powers attribute dissent positions only as the majority characterizes them.
- **Class 7 dissents and Trump v. United States separate opinions** — flagged in-file, pending Canvas.
- **Senate Report on Court Packing** — quotations from reproductions, pending a Canvas check.
- **Print packets vs. library scanning** — recommendation still open: EPUB-derived per-class packets with dual page labels (4th ed. p. N · 5th ed. ≈ p. M).
- **Past exams and prior outlines** — you have them; prior outlines go in `conlaw/_prior/`, not `00-source/`. Now is the natural moment, since the modules are the thing an outline compresses.
- **Confirm whether a one-page outline is allowed** — the draft syllabus says closed-book.
- **Project docs** — `claude/legalfinance.md` needs the Classes 8–9 Marra/Certum correction, and there is still no Con Law section.
- **Repo housekeeping** — `.obsidian/plugins/xlsx-viewer/` is untracked, commit or gitignore; `Untitled.md` at the root is 0 bytes.
