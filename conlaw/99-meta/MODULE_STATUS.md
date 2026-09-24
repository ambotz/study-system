# Con Law doctrine modules — status

**Complete.** All 31 modules are built, validated and committed to `conlaw/30-doctrine/`. Last commit `4db3f07`.

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

**Executive power (7)**
| Module | Emphasis | Exam |
|---|---|---|
| Enforcement discretion - Art. II § 3 Take Care | 3 | high |
| Presidential immunity and privilege - Art. II | 3 | high |
| Presidential power - Art. II and the Youngstown categories | 3 | high |
| Removal - Art. II § 1 and the Humphrey's exception | 3 | high |
| Appointments - Art. II § 2 cl. 2 and the officer line | 2 | medium |
| Impeachment - Art. II § 4 high crimes and misdemeanors | 2 | medium |
| Suspension of habeas corpus - Art. I § 9 cl. 2 | 2 | medium |

**Legislative power (5)**
| Module | Emphasis | Exam |
|---|---|---|
| Bicameralism and presentment - Art. I § 7 | 3 | high |
| Nondelegation - Art. I § 1 and the intelligible principle | 2 | high |
| Taxing power - Art. I § 8 cl. 1 and direct taxes | 2 | high |
| The power of the purse - Art. I § 9 cl. 7 appropriations | 2 | high |
| Bills of attainder - Art. I § 9 cl. 3 | 1 | low |

**Federalism (7)**
| Module | Emphasis | Exam |
|---|---|---|
| Commerce power - Art. I § 8 cl. 3 | 3 | high |
| Enumerated powers and the Necessary and Proper Clause - Art. I § 8 cl. 18 | 3 | high |
| Nature of the Union - compact theory, nationalism and secession | 3 | high |
| State sovereignty and anti-commandeering - Tenth Amendment | 3 | high |
| Spending power - Art. I § 8 cl. 1 general welfare and conditional grants | 2 | high |
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

## Three things to look at when you read these

**1. Two topic buckets are inconsistent across the set.** Independent agents built these in parallel, and two boundary calls came out differently than their neighbours:

- *Taxing power* sits under **Legislative power** while *Spending power* sits under **Federalism** — same clause, Art. I § 8 cl. 1, split across two buckets.
- *Suspension of habeas corpus* (Art. I § 9 cl. 2) sits under **Executive power** — the agent chose the bucket to match its anchor case, Ex parte Merryman — while *Bills of attainder*, the very next clause (Art. I § 9 cl. 3), sits under **Legislative power**.

Both are defensible; neither is consistent. Worth one decision from you, since `topic` is what any cross-module query will group on.

**2. One module has no inbound cross-link.** *Territories and citizenship - Art. IV § 3 and Dred Scott* is linked from no other module, even though Dred Scott feeds the departmentalism and modes-of-argument modules. Not an error, but the cross-link web has a hole there.

**3. Unlinkable authority.** Roughly 60 cases the readings discuss have no file in `10-cases/` — Myers, Morrison, Seila Law, Klein, Yerger, Gibbons, Martin v. Hunter's Lessee, Luther v. Borden and others. The guide forbids wikilinks to nonexistent files, so these are named in plain text throughout. Myers in particular carries real weight in the Removal module and appears unlinked every time. If you want any of them as brief-only stubs, that is its own small job.

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
- **Repo housekeeping** — `J. W. Hampton, Jr., & Co. v. United States.md` is a 0-byte stray at the repo root, safe to delete; `.obsidian/plugins/xlsx-viewer/` is untracked, commit or gitignore.
