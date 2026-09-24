# Con Law doctrine modules — handoff for a new session

**Vault:** `~/Documents/2L law-vault` · repo `github.com/ambotz/study-system` (private). Last commit `75b8a02`.

**Status:** 16 of 31 modules are built, validated and committed to `conlaw/30-doctrine/`. 15 remain. Everything below is what a fresh session needs to finish them — no other context required.

---

## 1. What's already in the vault

These 16 exist as `.md` files in `conlaw/30-doctrine/`. Do not rebuild them; link to them by name.

- Amendment process - Art. V
- Appointments - Art. II § 2 cl. 2 and the officer line
- Congressional control of the courts - Art. III jurisdiction and court size
- Dormant Commerce Clause - Art. I § 8 cl. 3 and state discrimination
- Enumerated powers and the Necessary and Proper Clause - Art. I § 8 cl. 18
- Judicial supremacy and departmentalism - Art. VI oath
- Nondelegation - Art. I § 1 and the intelligible principle
- Presidential immunity and privilege - Art. II
- Presidential power - Art. II and the Youngstown categories
- Privileges and immunities - Art. IV § 2 and state discrimination
- Separation of powers - vesting clauses and checks and balances
- Spending power - Art. I § 8 cl. 1 general welfare and conditional grants
- Standing - Art. III § 2 cases and controversies
- Supremacy and the oath - Art. VI
- Territories and citizenship - Art. IV § 3 and Dred Scott
- The power of the purse - Art. I § 9 cl. 7 appropriations

---

## 2. The build procedure that worked

1. Read the guide at `conlaw/99-meta/MODULE_GUIDE.md` (committed with this handoff) — it is the full spec: eight-section schema, section-by-section instructions, frontmatter contract, house style.
2. Stage the 96 reading files from `conlaw/10-cases/` so subagents can read them (or have the subagents read them on the device directly).
3. Dispatch subagents, **no more than four at a time and no more than four modules each** — larger waves hit the account session limit. Each agent gets: the guide, its module list with feeder readings (Section 3 below), and the full 31-name module list for cross-links.
4. Each agent writes `<Exact Module Name>.body` (body only, starting at `## Rule statement`) and `<Exact Module Name>.meta.json`.
5. Validate centrally before writing anything into the vault:
   - the eight headings present, in the guide's exact order
   - `## Professor gloss` has no text under it
   - no wikilink split across a newline; no link target ending in a period
   - every wikilinked case resolves to a real `.md` in `conlaw/10-cases/`, or to one of the 31 module names
   - each `.meta.json` parses and has `topic`, `sub_topic`, `authority`, `professor_emphasis`, `exam_likelihood`
6. Generate the YAML frontmatter from the JSON with a script — never hand-write it. Field order:

```
---
topic: <string>
sub_topic: <string>
authority:
  - <citation>
professor_emphasis: <1-3>
exam_likelihood: <high|medium|low>
confidence: 1
last_drilled: 
---
```

`confidence` is always `1` and `last_drilled` always empty on a fresh module — those two are Ashwin's to change, never the agent's.

7. Write the files into `conlaw/30-doctrine/`, then regenerate the derived files:

```
python3 .claude/scripts/index_to_byclass.py --class conlaw
python3 .claude/scripts/index_to_xlsx.py --class conlaw
```

8. Commit. Ashwin runs `git push` himself.

---

## 3. The 15 pending modules and their feeder readings

Each module is built from the reading files listed under it. Read every one before writing the module. A case with no `.md` file in `10-cases/` is named in plain text, never wikilinked.

### Judicial review - Art. III and the Supremacy Clause

Feeder readings (17) — read every one:

- `A Map of Article III`
- `Article VI - other materials`
- `Brutus No. 11`
- `Cooper v. Aaron`
- `Dred Scott v. Sandford`
- `Ex parte Levitt`
- `Hylton v. United States`
- `Marbury v. Madison`
- `Massachusetts v. Mellon; Frothingham v. Mellon`
- `McCulloch v. Maryland`
- `Stuart v. Laird`
- `Texas v. White`
- `The Correspondence of the Justices`
- `The Federalist No. 78`
- `The Lincoln-Douglas Debates`
- `Tocqueville on the American Judiciary`
- `United States v. Nixon`

### Modes of constitutional argument

Feeder readings (17) — read every one:

- `Campbell, Four Views on the Nature of the Union`
- `Corfield v. Coryell`
- `Dred Scott v. Sandford`
- `Jackson, Veto Message on the Bank`
- `Madison's Notes on the War Power`
- `Madison, Letter to Lafayette`
- `Marbury v. Madison`
- `McCulloch v. Maryland`
- `Stuart v. Laird`
- `The Bank Debate`
- `The Congressional Pay Amendment`
- `The Death of the Second Bank`
- `The Decision of 1789`
- `The Riddles of Article V`
- `Trump v. Cook`
- `Trump v. Slaughter`
- `Types of Constitutional Argument`

### War powers - Art. I § 8 cl. 11 and the Commander in Chief

Feeder readings (13) — read every one:

- `Bates, Opinion on the Suspension of Habeas Corpus`
- `Buchanan, Address to Congress`
- `Declarations of War`
- `Ex parte Merryman`
- `Jefferson Davis, Farewell Address to the Senate`
- `Lincoln, First Inaugural Address`
- `Lincoln, Order of Retaliation`
- `Madison's Notes on the War Power`
- `Modern Applications of the War Power`
- `Nixon, Veto of the War Powers Resolution`
- `Terminating War`
- `The Emancipation Proclamation`
- `The Prize Cases`

### Enforcement discretion - Art. II § 3 Take Care

Feeder readings (12) — read every one:

- `A Map of Article II`
- `Adams v. Richardson`
- `Bates, Opinion on the Suspension of Habeas Corpus`
- `Buchanan, Address to Congress`
- `In re Neagle`
- `Jefferson Davis, Farewell Address to the Senate`
- `Lincoln, First Inaugural Address`
- `Obama, Statement on H.R. 1473`
- `Printz v. United States`
- `The Thompson Memo`
- `Trump v. United States`
- `United States v. Cox`

### State sovereignty and anti-commandeering - Tenth Amendment

Feeder readings (12) — read every one:

- `A Map of the Federalism Provisions`
- `Bailey v. Drexel Furniture Co`
- `Garcia v. San Antonio Metropolitan Transit Authority`
- `Hammer v. Dagenhart`
- `Implied Limits on the Power to Tax`
- `McCulloch v. Maryland`
- `NFIB v. Sebelius`
- `National Pork Producers Council v. Ross`
- `Printz v. United States`
- `South Dakota v. Dole`
- `Texas v. White`
- `United States v. Darby`

### Nature of the Union - compact theory, nationalism and secession

Feeder readings (12) — read every one:

- `A Map of the Federalism Provisions`
- `Buchanan, Address to Congress`
- `Campbell, Four Views on the Nature of the Union`
- `Corfield v. Coryell`
- `Jackson, Veto Message on the Bank`
- `Jefferson Davis, Farewell Address to the Senate`
- `Lincoln, First Inaugural Address`
- `McCulloch v. Maryland`
- `National Pork Producers Council v. Ross`
- `Texas v. White`
- `The Bank Debate`
- `The Federalist No. 10`

### Commerce power - Art. I § 8 cl. 3

Feeder readings (12) — read every one:

- `Bailey v. Drexel Furniture Co`
- `Corfield v. Coryell`
- `Garcia v. San Antonio Metropolitan Transit Authority`
- `Gonzales v. Raich`
- `Hammer v. Dagenhart`
- `Implied Limits on the Power to Tax`
- `NFIB v. Sebelius`
- `National Pork Producers Council v. Ross`
- `The Bank Debate`
- `United States v. Darby`
- `United States v. Lopez`
- `Wickard v. Filburn`

### Removal - Art. II § 1 and the Humphrey's exception

Feeder readings (11) — read every one:

- `A Map of Article II`
- `Humphrey's Executor v. United States`
- `Introduction to Article II`
- `The Decision of 1789`
- `The Federalist No. 70`
- `The Federalist No. 76`
- `The Impeachment of Andrew Johnson`
- `Trump v. Cook`
- `Trump v. Slaughter`
- `Trump v. United States`
- `United States v. Lovett`

### Taxing power - Art. I § 8 cl. 1 and direct taxes

Feeder readings (6) — read every one:

- `Bailey v. Drexel Furniture Co`
- `Express Limits on the Power to Tax`
- `Hylton v. United States`
- `Implied Limits on the Power to Tax`
- `McCulloch v. Maryland`
- `NFIB v. Sebelius`

### Constitutional themes and the dead hand

Feeder readings (5) — read every one:

- `A Map of the Constitution`
- `Before the Constitution`
- `Constitutional Themes`
- `The Constitution of the United States`
- `The Dead-Hand Problem`

### Impeachment - Art. II § 4 high crimes and misdemeanors

Feeder readings (4) — read every one:

- `The Impeachment of Andrew Johnson`
- `The Impeachment of Justice Chase`
- `Trump v. United States`
- `United States v. Nixon`

### Suspension of habeas corpus - Art. I § 9 cl. 2

Feeder readings (3) — read every one:

- `Bates, Opinion on the Suspension of Habeas Corpus`
- `Ex parte McCardle`
- `Ex parte Merryman`

### Republican government - Art. IV § 4 Guarantee Clause

Feeder readings (3) — read every one:

- `Buchanan, Address to Congress`
- `Lincoln, First Inaugural Address`
- `Texas v. White`

### Bicameralism and presentment - Art. I § 7

Feeder readings (3) — read every one:

- `Clinton v. City of New York`
- `INS v. Chadha`
- `Nixon, Veto of the War Powers Resolution`

### Bills of attainder - Art. I § 9 cl. 3

Feeder readings (1) — read every one:

- `United States v. Lovett`

---

## 4. Known issues to carry forward

- **`The War Powers Resolution`** is a statute entry in the index with no reading file; `by-class.md` currently renders it as "doctrine module, no reading file." It resolves once the War powers module exists.
- **Pork Producers' Kavanaugh opinion** was never retrieved — his Privileges and Immunities discussion is missing from the reading file. It matters most for the already-built Art. IV module; re-check against Canvas.
- **Trump v. Slaughter / Trump v. Cook dissents** (Sotomayor, Alito, Barrett) were not retrievable. Modules touching Removal and Separation of powers attribute dissent positions only as the majority characterizes them.
- **Senate Report on Court Packing** quotations come from reproductions pending a Canvas check.
- **Class 7 dissents and Trump v. United States separate opinions** are flagged in-file, pending Canvas.
- **Class 5 "Additional Materials"** and the **Class 27 Canvas packet** have no files; contents unknown.
- A stray empty file `J. W. Hampton, Jr., & Co. v. United States.md` sits at the repo root, untracked. It is 0 bytes and safe to delete — it was never part of the reading set.
- `.obsidian/plugins/xlsx-viewer/` is untracked. Decide whether to commit or gitignore it.

---

## 5. Standing constraints

- Abrams Clinic material never enters this repo — not in any folder, not as a quotation, not as an anonymized example.
- Ashwin runs `git push` himself from Terminal.
- `ANTHROPIC_API_KEY` stays unset in any shell that runs this vault's jobs.
- The nightly job writes a proposed diff, never a direct commit.
- Agent write permissions are allowlisted to the vault directory only.
- No cloud folder sync over this directory; a one-way OneDrive mirror must exclude `.git/`.
