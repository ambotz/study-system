---
epoch: 1792607620853
mode: agent
backendId: claude
sessionId: "ac03a7e6-3394-47f4-91cb-9e1304fd8530"
agentLabel: "So I'm trying to undestand the demand futility requirement t…"
tags:
  - copilot-conversation
usage: '{"usedTokens":172764,"contextWindow":1000000,"inputTokens":2,"outputTokens":5,"cacheReadTokens":171463,"cacheWriteTokens":1294,"updatedAt":1792873012850}'
---

**user**: So I'm trying to undestand the demand futility requirement through the lens of (1) derivative vs. direct and (2) who the deriviative shareholder is suing. So in deriviative shareholder suits, is it correct that sometimes the suit will be against another corporation and sometimes it will be against the own corproations board of directors? And in the latter, it will be an attempt to hold the Directors individually liable?
[Timestamp: 2026/10/21 13:33:40]

**ai**: Mostly yes, but one correction first. The corporation is always a party to a derivative suit, as the nominal defendant. It is the real plaintiff in interest, because the shareholder sues on its behalf. The people the shareholder actually wants to hold liable are the other defendants, and those fall into three groups.

1. **The company's own directors and officers.** This is the most common case. The claim is a breach of fiduciary duty (loyalty, bad faith, oversight). You're right that the directors are personally liable. The damages go to the corporation, not to the shareholder. That's why a derivative suit needs demand or futility in the first place.
2. **A controlling stockholder.** This can be a person or a parent corporation, and it is often sued together with the directors who approved the deal.
3. **A third party.** This might be a counterparty, an advisor, or another corporation that aided and abetted the breach. This is what you may have meant by "another corporation."

A corporation is rarely the target on its own. When one is sued, it is usually as a controller or a counterparty to a transaction.

**Why this matters for demand futility.** Futility asks whether the demand board could impartially decide whether to sue these defendants. The identity of the defendants therefore drives the analysis under the three-part test in [[Demand futility - Rule 23.1 and the Zuckerberg test]].

| Defendant | How futility plays out |
|---|---|
| Directors on the demand board | Prongs one and two apply. Did the director get a material personal benefit, or face a substantial likelihood of liability? Only half or more of the demand board needs to answer yes. |
| Controller or a director's benefactor | Prong three does the work. A director who lacks independence from the controller can't consider the demand impartially (*Marchand*). |
| Unrelated third party | None of the prongs bite, because the board has no conflict. Demand is probably not futile, and the board can decide whether to sue. |

Futility is judged director by director. Being named as a defendant is not enough on its own ("they'd have to sue themselves" is bootstrap). Each director needs a substantial likelihood of liability. That is where § 102(b)(7) exculpation matters: an exculpated care claim can't excuse demand.

**Direct vs. derivative.** Suing the directors does not make a claim derivative. A shareholder can sue directors directly, for example over voting rights or a disclosure claim. The test asks who suffered the harm and who gets the recovery. A direct claim needs no demand, so the Rule 23.1 analysis only applies if the claim is derivative. I'm giving you the *Tooley* test from memory. Your module doesn't cover it, so check it against your class materials before you rely on it.

Do you want me to add a short "who is the defendant" section to the module? I'd need to check whether it fits the fixed schema in CLAUDE.md, since the body sections can't be added to. It might belong in Elements or Common trap instead.

Separately, several claude.ai connector MCP servers (Gmail, Google Drive, GitHub and others) need authorization. I can't run the OAuth flow in this session. Authorize them in your claude.ai connector settings if you want them. They aren't needed for this question.
[Timestamp: 2026/10/21 13:33:40]

**user**: I don't need claud ai. collectors. Seperately, are you using my Claude account to run this session?
[Timestamp: 2026/10/21 13:37:21]

**ai**: I can't tell for certain. Here is what I found.

- **API key:** `ANTHROPIC_API_KEY` is unset in the shell I can see. That matches the rule in your CLAUDE.md, so this session isn't billing per token through a Console API key, at least from that variable.
- **Login:** I couldn't check the login directly. `claude` isn't on the PATH in that shell, so `claude auth status` failed.
- **Likely account:** The claude.ai connector list suggests the session is tied to a claude.ai account login, probably yours. That is an inference, not something I verified. I can't see which account or plan it is.
- **Plugin settings:** The session runs through the Obsidian Copilot plugin, which may supply its own credentials. I didn't open `.obsidian/plugins/copilot/data.json` because it may hold API keys. You can check the auth setting in the plugin's settings pane.

I won't mention the connectors again. I can't turn them off from this session. If you want them gone, remove them in your claude.ai connector settings.
[Timestamp: 2026/10/21 13:37:21]

**user**: Going back to the question, what do you mean by: "Being named as a defendant is not enough on its own ("they'd have to sue themselves" is bootstrap)."
[Timestamp: 2026/10/21 13:38:27]

**ai**: The point is about what a plaintiff has to plead to show demand is futile.

**The argument that fails.** A plaintiff sues the directors for breach of fiduciary duty. The complaint then says demand would be futile because the directors are the defendants. They would have to decide whether to sue themselves, and no one can be expected to do that impartially. This is the "bootstrap" argument. The conflict is created by the plaintiff's own choice of defendants, and no facts about any director support it.

**Why courts reject it.**
- **It would swallow the rule.** If naming the directors excused demand, demand would be futile in every derivative suit against directors. Rule 23.1 would never apply to the most common kind of derivative suit. Your module quotes *Aronson*: accepting the argument "would effectively abrogate Rule 23.1 and weaken the managerial power of directors."
- **The plaintiff controls the label.** The plaintiff decides who gets named. If naming were enough, the plaintiff could create futility by adding defendants.

**What the court asks instead.** It looks at each director on the demand board and asks about the three prongs in the module.
- **Prong one:** Did the director get a material personal benefit from the misconduct?
- **Prong two:** Does the director face a *substantial likelihood of liability* on a claim that could actually succeed?
- **Prong three:** Is the director beholden to someone who got a benefit or faces that liability?

Being named is not the same as facing a substantial likelihood of liability. Take a complaint that names all nine directors but pleads only a duty of care breach. If the charter has a § 102(b)(7) exculpation clause, that claim can't produce personal liability. The directors are named, but none of them is exposed, so demand is not excused.

The reverse also works. If the complaint pleads facts showing a director sat on both sides of the challenged deal, that director is disqualified. The reason is what the facts show about that director. It is not that the director was named.
[Timestamp: 2026/10/21 13:38:27]

**user**: Ok, so let's focus on breach of loyalty claims. Usually, it will be that the Director did not do XYZ or did XYZ and was acting under a conflict of interest? right? Let's first establish a baseline. What does a duty of loyalty claim look like
[Timestamp: 2026/10/21 13:39:52]

**ai**: First, a correction to something I said earlier. I told you your vault didn't cover the *Tooley* test. It does: [[Direct versus derivative claims - the Tooley test]] is there.

You're close, but one half of your framing needs tightening.

**The baseline.** A loyalty claim says the director acted for a reason other than the corporation's and stockholders' best interests. It rests on a conflict or on bad faith. Your vault's business judgment rule module ([[Business judgment rule - scope of protection]]) names the three "doors" into the boardroom: fraud, illegality, and conflict of interest. Loyalty is mainly the third door, and bad faith connects it to the second.

**Your "did XYZ under a conflict" version is the core case.** The common forms:

1. **Self-dealing.** The director is on the other side of the transaction, or has a material interest or relationship that would impair their judgment. Under [[Bayer v. Beran (1944)|Bayer v. Beran]], the business judgment rule "yields to the rule of undivided loyalty." The fiduciary then has to prove the transaction was fair. See [[Interested director and officer transactions - 144(a)]].
2. **Controller transactions.** The controller gets a benefit the minority doesn't. See [[Controlling stockholder transactions - the self-dealing trigger]] and [[Sinclair Oil v. Levien (1971)|Sinclair Oil v. Levien]].
3. **Taking a corporate opportunity.** See [[Partnership loyalty - business opportunity]] and [[Agent duty of loyalty - self-dealing]].
4. **Entrenchment or interference with the franchise.** See [[Interference with the franchise - Schnell, Blasius and the Coster standard]].

**Your "did not do XYZ" version only works in one form.** An omission is not a loyalty breach just because it was a failure. Ordinary inattention is a care claim, and under a § 102(b)(7) clause it is exculpated. An omission becomes a loyalty claim only when it is **bad faith**: a conscious disregard of known duties, as in [[In re Caremark International Inc. Derivative Litigation (1996)|Caremark]]. See [[Oversight liability - Caremark and good faith]].

**Personal gain vs. personal preference.** Per your BJR module, a conflict means something flowed to the director that the stockholders generally didn't get. A director acting on conviction with nothing in it for them keeps the business judgment rule's protection, as in [[Shlensky v. Wrigley (1968)|Shlensky v. Wrigley]].

**Why this matters for demand futility.** Loyalty and bad faith claims are not exculpated under [[Charter exculpation of director liability|§ 102(b)(7)]]. That makes them the claims that can satisfy prong two (substantial likelihood of liability). The conflict facts also feed prong one (material personal benefit) and prong three (independence).

Do you want to go next to what a plaintiff has to plead for a loyalty claim against a director, or to how that maps onto the three prongs?
[Timestamp: 2026/10/21 13:39:52]

**user**: Got it. So lets assume a duty of loyalty claim, say, under self-dealing or something else, maybe even corporate opportunity. In that case that is necessarily implying that the director did something that belongs to the corporation or, in some way, harmed the corporation itself, right? In that sense would it necessarily mean that it's a derivative claim? How can a duty of loyalty be a direct claim? Would it mean that there is some sort of special stockholder that's owed something?
[Timestamp: 2026/10/21 13:42:39]

**ai**: No on both counts. A loyalty claim is not necessarily derivative, and you don't need a special stockholder for it to be direct.

**Classification turns on Tooley, not on the duty.** Per [[Direct versus derivative claims - the Tooley test]], the two questions are who suffered the harm and who would receive the recovery. The module says the test is "not about whether the defendant owed fiduciary duties. Both kinds of claim can rest on fiduciary breach." The duty of loyalty is owed to the corporation and to the stockholders. Which kind of claim you have depends on where the injury lands.

**When a loyalty claim is derivative.** This is the pattern you described. The director took something from the corporation or caused it to overpay.
- **Corporate opportunity:** the corporation lost the opportunity, and the corporation recovers.
- **Self-dealing, such as a director selling property to the company at an inflated price:** the company's assets shrank, and the stockholders only feel that indirectly, pro rata, through share value. The recovery goes to the corporation, so Rule 23.1 applies.

**When a loyalty claim is direct.** The injury runs to the stockholders in their own right, and the recovery goes to them. The module gives two examples.
- **Voting and franchise claims.** The module says voting rights, or "rights existing independently of any corporate right," are the clearest direct claims. That is the territory of [[Interference with the franchise - Schnell, Blasius and the Coster standard]]. Entrenchment is a loyalty-type theory, but the harm is to the stockholders' vote.
- **The merger pattern, after [[In re Riverstone National (2016)|In re Riverstone National]].** A merger extinguishes the derivative claim against the approving directors. The former stockholders then argue that the board failed to price that claim into the merger consideration. That is a direct harm to them, because the price they personally received was too low. A conflicted merger where a controller or insider takes value out of the stockholders' deal price has the same shape. The plaintiffs can win without proving the corporation was hurt.

**There is no "special stockholder."** That was the old "special injury" test, which *Tooley* abolished. A wrong that hits every stockholder equally can still be direct, as long as the injury is independent of the corporation's. The question is whose injury it is, not whether the plaintiff was singled out.

**Why this matters for your original question.** Only a derivative claim needs presuit demand or a futility pleading, so classification decides whether the *Zuckerberg* analysis happens at all. A plaintiff with a loyalty claim that could be pleaded either way has a reason to frame it as direct, which is why courts apply *Tooley* strictly.

One thing from my own knowledge, not your notes: the Delaware Supreme Court has treated stock-issuance dilution claims as derivative only. I believe that is *Brookfield Asset Management v. Rosson* (2021), but your modules don't cover it, so check it before relying on it.
[Timestamp: 2026/10/21 13:42:39]

**user**: Does 220(c) mainly provide the procedural vehicle to actual ask for a book and records inspection? I'm not sure if the note itself covers what 220(c) is?
[Timestamp: 2026/10/21 14:17:57]

**ai**: Yes, roughly. Section 220(c) is the enforcement vehicle, not the way you make the request.

**The two steps**
1. **Demand.** You make the demand to the corporation under § 220(b). It must be in writing and under oath. The note covers the form and manner and the post-SB 21 gates there.
2. **Court application.** If the corporation refuses, or doesn't reply within five business days, you apply to the Court of Chancery under § 220(c) for an order compelling inspection. The court has exclusive jurisdiction. The proceeding is summary, and the court can set limits on the inspection or award other relief.

**What the note covers about (c).** The note doesn't say in one place what (c) is. It touches (c) in four spots:
- The authority list at the top mentions "§ 220(c), (d) (procedure; director inspection)."
- The Standard of review table has a "Vehicle" row: demand under oath, then on refusal or no reply within 5 business days, an application to Chancery under § 220(c). It also covers exclusive jurisdiction, the burden allocation, the court's remedial discretion, and the summary nature of the proceeding.
- Section 220(e) is described as the scope ceiling "in a § 220(c) proceeding."
- The before-and-after table notes that redaction and the incorporation condition were the court's discretion under (c) before SB 21. After SB 21 they are the corporation's right under (b)(3).

So the facts are in the note, but they're scattered across tables. A reader who wants to know what (c) is would have to piece it together.

The five-business-day detail comes from the note. The rest of how I've described (c) is my general understanding of the statute, so check it against the statutory text.

Do you want me to add a short § 220(c) bullet to the Elements section? That keeps the fixed section order and gathers the (c) points in one place.
[Timestamp: 2026/10/21 14:17:57]

**user**: Yes, are you able to do that?
[Timestamp: 2026/10/21 14:18:49]

**ai**: Yes, I added it. The new subsection, "The two steps — demand under § 220(b), enforcement under § 220(c)", sits at the top of Elements in [[Books and records inspection - 220 before and after SB 21]]. It's a subsection under the existing heading, so the eight-section order is unchanged, and I didn't touch the frontmatter.

It collects the (c) points that were scattered across the note:
- **Demand and enforcement:** the written demand under oath comes first. The § 220(c) application to Chancery follows if the corporation refuses or doesn't reply within 5 business days. Chancery's jurisdiction is exclusive.
- **Proceeding:** it is summary and expeditious, and the burden depends on the record sought.
- **Court's power:** the court can prescribe limits or conditions on the inspection or award other relief. That discretion was the source of redaction and the incorporation condition before SB 21.
- **Post-SB 21 ceiling:** the court can't order anything outside the (a)(1) list except under (f) or (g).
- **Directors:** they have a separate inspection right under § 220(d).

Everything in the subsection comes from what the note already said. I added no new statutory detail, so nothing in it depends on my memory of the statute. I'd still check the five-business-day period against the statutory text.
[Timestamp: 2026/10/21 14:18:49]

**user**: "The current text allows officer exculpation but never "in any action by or in the right of the corporation," so a potential derivative claim against an officer still survives. "
Explain this to me in the current text and what it allows
[Timestamp: 2026/10/21 14:24:55]

**ai**: **What the sentence means.** Section 102(b)(7) lets a charter wipe out personal money liability for breaches of the duty of care, which is the damages exposure at issue. The original statute covered directors only. The current text extends it to officers. But the officer version has an extra carve-out: no exculpation of an officer "in any action by or in the right of the corporation." Your charter exculpation module lists this as a fifth carve-out, on top of the four that apply to everyone.

**What the carve-out covers.** "By or in the right of the corporation" means two kinds of suit:
- a **derivative** suit, where a stockholder sues on the corporation's behalf, and
- a suit the **corporation** itself brings against the officer.

**What the current text allows.**

| Claim | Director | Officer |
|---|---|---|
| Care claim, damages, **direct** stockholder suit | Can be exculpated | Can be exculpated |
| Care claim, damages, **derivative** suit | Can be exculpated | **Cannot be exculpated** |
| Loyalty, bad faith, § 174, improper personal benefit | Never exculpated | Never exculpated |

So an officer's exculpation covers direct stockholder suits, such as a class action over a merger. It never covers a derivative claim, even for a plain care breach. Take a CEO who was grossly negligent in the same way as the board. In a derivative suit the directors are dismissed, but the CEO can still be sued for damages.

**Why the 220 note relies on it.** The note's point is that a charter exculpation clause doesn't block a § 220 demand. Even if directors are shielded, a possible derivative claim against an officer survives, so investigating it is still a proper purpose.

This also explains why the note says "when Yahoo! was decided." At that time § 102(b)(7) didn't cover officers at all, so any claim against an officer survived.

Two details come from my memory, not your notes. I believe the officer amendment took effect in August 2022. I also believe only certain officers qualify, defined by reference to § 3114(b) (for example the president, CEO, CFO and named executive officers). Check both against the statutory text. I can add them to the charter exculpation module if you want.
[Timestamp: 2026/10/21 14:24:55]

**user**: what does the 220(b)(4) savings clause actually do? is that different than for deriviative suits?
[Timestamp: 2026/10/21 14:29:27]

**ai**: I'm working from the note's summary, which is all your vault has on § 220(b)(4). I haven't seen the statutory text.

**What it does.** Section 220 governs inspection before a suit. SB 21 closed the list of reachable records to nine categories and added the (b)(2) gates. The § 220(b)(4) savings clause says the section doesn't affect two things:
- a stockholder's **discovery rights in litigation with the corporation**, and
- a court's **independent power to compel production**.

The closed list is a limit on § 220 inspection demands. It is not a ceiling on what a litigant can get through ordinary discovery once a suit is on file. Without the clause, someone could argue that SB 21's narrowing of "books and records" also narrowed discovery.

**The limit on the clause.** For (a)(1) records that a stockholder demands, the (b) requirements must still be met. The independent-power language therefore doesn't let a stockholder skip the good faith, particularity and specific-relation gates for listed records.

**Is it different for derivative suits?** The clause itself isn't. A derivative suit is litigation like any other, and ordinary discovery rules apply. The timing is what matters for derivative plaintiffs. The note says Delaware courts push plaintiffs to use the "tools at hand" before pleading demand futility, which makes a § 220 demand effectively a precondition to a well-pleaded complaint.

That gap is why the closed list hurts derivative plaintiffs. Discovery rights are preserved, but they only matter after the plaintiff has a complaint that survives. My understanding is that Delaware generally doesn't allow discovery to help plead demand futility, and that discovery waits until the complaint survives the Rule 23.1 motion. That comes from my memory, not your notes, so check it. If it's right, a derivative plaintiff can't use (b)(4) to avoid the narrower § 220 before filing, and the closed list controls what the plaintiff gets for the complaint.

I can add a short line on this to the Exceptions section of the 220 module if you want.
[Timestamp: 2026/10/21 14:29:27]

**user**: What is the incorporation Condition? What does it mean for something to be deemed incorporated? I understand the logic of witholding information. Is that it?
[Timestamp: 2026/10/21 14:52:18]

**ai**: It isn't about withholding information. It works the other way. The stockholder gets the documents, and the court is then allowed to read all of them against the complaint.

**What it is.** The Incorporation Condition is a condition on production. [[Amalgamated Bank v. Yahoo! (2016)|Yahoo!]] imposed it for the first time. The court orders the corporation to hand over the records only if the whole production is **incorporated by reference** in any derivative complaint the stockholder later files on the subject of the demand.

**What "deemed incorporated" means.** A document that is incorporated by reference is treated as part of the complaint, even though the plaintiff didn't attach or quote it. The court can read it when deciding a motion to dismiss. Your case note says the condition is built on the existing incorporation-by-reference doctrine: that doctrine "already stops a plaintiff from quoting a document and preventing the court from reading it," and the condition extends it to the rest of the production.

My understanding is that on a motion to dismiss a court normally stays inside the complaint. Documents the complaint relies on are an exception, and that exception is why this doctrine works. That's from my general knowledge, not your notes.

**The purpose is to stop cherry-picking.** Without the condition, a plaintiff could pull the helpful lines from 677 pages, plead them, and leave out the context. The defendants would then have to argue about documents that aren't in the complaint. With the condition, the whole production counts as part of the pleading, so the court sees the related documents too. The note puts it this way: a complaint "will not be based on cherry-picked documents."

**What it does not change.** The court was careful to say the pleading standards stay the same:
- Well-pleaded facts are still taken as true under Rule 12(b)(6).
- Particularized allegations are still taken as true under Rule 23.1.
- The plaintiff still gets all reasonable inferences, including when a document supports more than one.

It only stops a plaintiff from taking a document out of context and insisting on an inference the court couldn't draw if it saw the related documents.

**Why not just use Rule 11?** The defendants argued Rule 11 already deters cherry-picking. Laster answered that "invoking Rule 11 is strong medicine." The usual problem is counsel drawing an unreasonable inference from one document, "not in bad faith but perhaps over-zealously." The condition handles that "in more measured fashion."

**After SB 21.** The condition is now § 220(b)(3). It is the corporation's right as a condition of production, not a matter for the court's discretion. As your 220 module quotes it, information in the records is "deemed incorporated by reference in any complaint filed by or at the direction of the stockholder."
[Timestamp: 2026/10/21 14:52:18]

**user**: so basically, one half of it is, if a pleading includes reference to a document, that document is 'incorporated' into the record and the whole document is referenced?
[Timestamp: 2026/10/21 14:54:20]

**ai**: Yes, that's the first half, with one refinement. The document comes into the **complaint**, not the evidentiary record. The court treats the whole document as part of the pleading when it decides a motion to dismiss. No discovery or trial record is involved.

**The ordinary doctrine.** If a complaint quotes or relies on a document, the court can read the whole document, not just the excerpt the plaintiff chose. A plaintiff can't quote a favorable sentence and keep the sentences around it out of view. Your case note describes it as stopping "a plaintiff from quoting a document and preventing the court from reading it."

**The Incorporation Condition is the second half.** It extends the same logic to documents the complaint never mentions:

| | Ordinary doctrine | Incorporation Condition |
|---|---|---|
| Triggered by | The complaint references the document | A § 220 production order |
| Reaches | That whole document | **The entire production**, referenced or not |
| Applies to | Any complaint | Any derivative complaint on the subject of the demand |

Under the ordinary doctrine the plaintiff controls which documents come in, by choosing what to cite. Under the condition the plaintiff gets no such choice, because everything produced counts.

The pleading standards stay the same either way: allegations are taken as true, and the plaintiff gets reasonable inferences. The only difference is that the court sees the context.
[Timestamp: 2026/10/21 14:54:20]

**user**: what's the difference between the 'entire production' and 'document'
[Timestamp: 2026/10/21 14:56:43]

**ai**: A **document** is a single record, such as one email, one set of committee minutes, or one board presentation. The **production** is the full set of records the corporation hands over in response to the § 220 demand. In *Yahoo!*, the note says that was 677 pages. One production contains many documents.

The difference is what the court may read alongside the part the plaintiff cited.

- **Ordinary doctrine.** The complaint cites Document A. The court reads all of Document A, not just the quoted lines. Documents B and C stay out, because the complaint never mentioned them.
- **Incorporation Condition.** The complaint cites Document A. The whole production is treated as part of the complaint, so the court may read Documents B and C too, even though the complaint never cited them.

Here is a hypothetical, which is mine and not from the case. The complaint quotes an email in which a committee member says nobody asked whether the executive could be fired for cause. Elsewhere in the production is a memo from counsel, never cited, that walks through the cause definition and explains why it didn't fit. Under the ordinary doctrine the court reads the email in full, but the memo stays out unless the complaint relies on it. Under the condition the memo is part of the complaint, and the court can weigh it when deciding which inferences are reasonable.

That's why the court calls the condition a guard against cherry-picking. Reading the cited document in full stops a plaintiff from clipping a quote. It doesn't stop a plaintiff from citing only the favorable documents out of a larger set.
[Timestamp: 2026/10/21 14:56:43]

**user**: Explain the three day discrepancy in the document dated and ownenrhip/fund thing
[Timestamp: 2026/10/21 15:08:48]

**ai**: **Why ownership evidence is required.** Amalgamated wasn't a record holder. The note says it made the demand on behalf of "the Funds," which held the Yahoo! shares beneficially. For a demand like that, § 220 (pre-SB 21) requires three things:
1. a statement of the person's status as a stockholder,
2. documentary evidence of beneficial ownership, and
3. a statement that the evidence is a true and correct copy of what it purports to be.

The second item is where the dispute arose. The note says Delaware requires "strict adherence" to these procedural requirements.

**The three-day gap.** Amalgamated attached account statements dated **three days before** the demand. Yahoo! argued that was fatal, because the statements didn't prove ownership on the day of the demand. The court rejected the argument:

- **No same-day record.** Requiring same-day documentation "would be an unreasonable reading of the statute." Statements issue periodically, and getting documentation takes time. No stockholder could comply with a same-day rule.
- **Practical reading.** Section 220 "must be applied with some appreciation of the practical considerations surrounding its use."
- **The test.** The documentation must be "sufficiently proximate in time to the date of the demand as to be consistent with and corroborate the averment of stock ownership."

**How it works.** The sworn statement of ownership is the main evidence. The attached documents only have to corroborate it, so a recent statement that fits the sworn claim is enough. There is no bright-line number of days. A statement three days old passed. The note doesn't say how old a statement could be before it failed.

**The strict-compliance rule is untouched.** The case doesn't relax the three form-and-manner requirements. It says only what "proximate in time" means for the documents.
[Timestamp: 2026/10/21 15:08:48]

**user**: and to confirm, post Sb-21, this person being a stockholder requirement is not refiend right?
[Timestamp: 2026/10/21 15:10:35]

**ai**: Your vault is consistent with that, but it doesn't confirm it. I can't verify it from what's here.

**What the vault shows.** The 220 module lists what SB 21 changed:
- the closed nine-category list of records,
- the three gates in § 220(b)(2) (good faith and proper purpose, reasonable particularity, specific relation),
- the corporation's conditions and redaction right in § 220(b)(3),
- the scope ceiling and escape hatches in § 220(e)–(h).

Nothing in the module says SB 21 touched who qualifies as a stockholder, or the proof-of-ownership requirements for a beneficial owner. The "Rule statement" still describes a "written demand under oath," and the post-SB 21 comparison table only changes the demand's contents (purpose and records, particularity). I found no statutory text for § 220(b)(1) in the vault to check against.

**Why I can't call it confirmed.** The module explains the form-and-manner requirements only in the pre-SB 21 section, so a gap in the post-SB 21 section doesn't prove nothing changed. SB 21 also added gates on the demand, so it is harder to make a successful demand even if the status requirement is untouched.

I'd check the post-SB 21 text of § 220(b)(1) directly before saying the status rule is unchanged. If you want, I can add one line to the post-SB 21 section noting that the status and form-and-manner requirements are unchanged, once you've confirmed it against the statute.
[Timestamp: 2026/10/21 15:10:35]

**user**: Ok, so what happens after credible bases is esablished? The procedure posture segment says that this is a post-trail decision, so this is not a pleading standard? Or it?
[Timestamp: 2026/10/21 15:12:26]

**ai**: Credible basis is not a pleading standard. It's a burden of proof, applied at the § 220 trial.

**Why the posture matters.** Your case note says *Yahoo!* is a post-trial decision in a summary proceeding under § 220(c). The stockholder had to prove the credible basis with evidence, by a **preponderance of the evidence**. The court weighed the evidence and made findings about what the Committee did and didn't receive. That is why the opinion can describe those events as facts. A pleading standard like Rule 12(b)(6) or Rule 23.1 assumes the allegations are true and tests whether they're enough. Nothing like that happens here.

The standard is still the lowest possible burden of proof. It asks only whether the evidence supports an inference of *possible* mismanagement that warrants further investigation. Proof is required, but the bar is low.

**What happens after the credible basis is established.**
1. **Proper purpose is satisfied** for that investigation. Form and manner and the stockholder status requirements are separate questions, and the *Yahoo!* court resolved them too.
2. **The court decides scope.** It orders the records that are essential and sufficient for the purpose, with "rifled precision," and it can impose conditions. In *Yahoo!* the court ordered a tailored production within thirty days, subject to the Incorporation Condition.
3. **The § 220 action ends.** It is summary, and nothing is decided on the merits. The note says the credible basis finding "decides nothing about liability." Even where a case gets past the early stages, the defendants can still win later. The note mentions *Disney* as an example.
4. **The stockholder uses the records.** If the stockholder files a derivative complaint, that is where **Rule 23.1** comes in, a real pleading standard requiring particularized facts. The § 220 production supplies those facts, and the Incorporation Condition makes the whole production part of the complaint. The stockholder could instead use the records for other purposes: seeking an audience with the board, a stockholder resolution, or a proxy fight.

**The standards in order**
| Stage | Standard | What it is |
|---|---|---|
| § 220 trial | Credible basis, preponderance | Evidentiary |
| Derivative complaint | Rule 23.1 particularity, Rule 12(b)(6) | Pleading |

The first gets the stockholder documents. The second is what the complaint built from those documents has to satisfy.
[Timestamp: 2026/10/21 15:12:26]

**user**: Do we need to clarify the incorporation condition in b3 in the Books and Records doctrien md file?
[Timestamp: 2026/10/21 15:17:31]

**ai**: Yes. The module's § 220(b)(3) paragraph gives the incorporation condition as a quoted phrase and never says what it means. The explanation is only in the *Yahoo!* case file and the Leading case section, so a reader looking at (b)(3) has to go find it.

Here is the text I'd add to the (b)(3) paragraph in Elements:

> The incorporation condition makes the produced information part of the complaint. The court may read the produced records against the complaint's allegations, so a plaintiff cannot plead from selected excerpts. It changes no pleading standard: allegations are still taken as true and the plaintiff keeps all reasonable inferences. See [[Amalgamated Bank v. Yahoo! (2016)|Amalgamated Bank v. Yahoo!]].

**A wording difference to check.** The module quotes the statute as covering "any information in the records" and "any complaint filed by or at the direction of the stockholder." The *Yahoo!* condition, as your case note describes it, covered the entire production and any derivative complaint on the subject matter of the demand. The statute may be broader than the case in two ways: the type of complaint, and whether the subject matter has to match. I can't tell from the module whether that is deliberate. Check the statutory text before I write the scope into the module, and I'll leave the sentence above neutral on it.

Do you want me to add the sentence?
[Timestamp: 2026/10/21 15:17:31]

**user**: So to be clear, demand futility was successfully pleaded in this case? because 102(b)(7) meant no likelihood of liability and the independent committee was found to be sufficinetly indepedent? What about material personal benefit? 

Also, are these three factors against the entire board or just Zuckerberg in this case?
[Timestamp: 2026/10/22 10:24:28]

**ai**: No. Demand futility was **not** successfully pleaded. The Supreme Court affirmed the dismissal under Rule 23.1, so Tri-State lost. Two points in your reasoning need fixing.

**1. The result and why.** Per your case note, the holding was that "the complaint failed to plead with particularity that a majority of the demand board lacked independence." Two separate rulings fed into that:
- **Exculpation (prong two).** Claims exculpated under § 102(b)(7) can't create a substantial likelihood of liability, so they can't excuse demand. That is a rule of law the court stated, and the note doesn't say it was the reason for the outcome.
- **Independence (prong three).** The one director the note discusses is **Bowles**. The complaint's allegations were the retirement-age waiver and ties to the deal's advisors, and the court found them insufficient. It also found collegiality ("proud to be a small part of [his] life") insufficient.

**2. The "independent committee" point.** The court did not hold that the special committee was independent. It held that the complaint didn't plead *non*-independence with particularity for enough directors. Futility is also assessed against the **demand board** at filing, which was nine directors, not the 2016 special committee. Chenault and Zients weren't even on the board in 2016.

**Material personal benefit (prong one).** The note records no holding on this prong. I can tell you where it would sit. The reclassification existed for Zuckerberg's benefit, so he is the director who received the benefit. For the other directors, prong three asks whether they lack independence from him. The vault doesn't say how the court treated Zuckerberg under prong one. Check the opinion before relying on it, or tell me and I'll look for it in your sources.

**Is it the whole board or just Zuckerberg?** Neither exactly. The three questions apply to each director individually, and then you count. Demand is excused if half or more of the demand board answers yes to any one of the three, per your demand futility module. Zuckerberg is one of nine. Disqualifying him, or even a few directors, doesn't excuse demand unless the count reaches half. The note doesn't say how many directors the court treated as disqualified, so I can't tell you how close the count was.
[Timestamp: 2026/10/22 10:24:28]

**user**: So for prong one, the assessment if whether each director individually recieved material benefit, even if in this case, it was only Zuckerberg's stocks that were reclassified?
[Timestamp: 2026/10/22 10:34:12]

**ai**: Yes. Prong one asks about each director separately, and it asks whether that director personally received a material benefit from the misconduct. If Zuckerberg is the only director who got one, prong one can disqualify only him. It doesn't spread to the other eight.

A refinement on the facts. Your case note says the new non-voting class would be distributed as a dividend, so the stock reclassification itself reached stockholders generally. What was personal to Zuckerberg was the ability to sell non-voting shares while keeping voting control. That unique benefit is the "material personal benefit." Your module says it has to come from "the misconduct itself, not from being a director generally."

**How one person's conflict reaches other directors.** That is prong three. It asks whether a director lacks independence from someone who received the benefit (or faces liability). So the analysis goes like this:
- **Zuckerberg:** prong one, and probably prong two if he faced a substantial likelihood of liability.
- **The other directors:** each is tested for independence from Zuckerberg under prong three. A director who is beholden to him counts toward the half. That is why the plaintiffs went after Bowles's independence.
- **Prong two** separately asks whether each director would face a substantial likelihood of liability on the claims.

This is also why the independence fight mattered so much. The benefit was one person's, so the plaintiffs needed to show enough other directors were beholden to him to reach half of the nine-member demand board.
[Timestamp: 2026/10/22 10:34:12]

**user**: So Unocal is responding to take over proportionately and Revlon is making sure the price (after proportionate response can't happen/is determined uninevitable) is the best possible price?
[Timestamp: 2026/10/23 12:10:26]

**ai**: You have the sequence right, but I'd change three things.

**Unocal** is the standard of review for a defensive measure the board adopts against a perceived threat to control. The directors carry the burden on two prongs:
- **Threat:** they had reasonable grounds to believe a danger to the corporation existed, shown by good faith and reasonable investigation, and they articulated a legitimate threat.
- **Proportionality:** the response was reasonable in relation to that threat. A response that is preclusive or coercive fails outright.

So "responding proportionately" is the second prong. The first prong is the threat, and without a legitimate one the response never gets to proportionality.

**Revlon** is not a separate standard that takes over once proportionate responses stop being possible. Your Revlon module says it is "Unocal enhanced scrutiny applied where the only cognisable corporate objective left is price." What changes is the board's objective. It goes from preserving the corporate entity to getting "the best value reasonably available" for stockholders. After that, a defensive measure justified by anything other than price is disproportionate by definition.

**The trigger.** The test isn't that proportionate responses become impossible. Per [[Paramount v. QVC (1994)|Paramount v. QVC]], the duty attaches when the transaction causes a **change in control** or a **break-up** of the company. A break-up is not required. In *Revlon* itself the board's escalating bids made the break-up inevitable and the board was negotiating with third parties, which showed it had embraced a sale.

**"Best price."** The duty is the best value reasonably available, not a guarantee of the highest number. Your module says there is no required auction, no mandatory market check, and no perfect decision, only a reasonable one. For non-cash consideration the board should try to quantify its value if feasible.

*Revlon* itself shows the sequence you describe. The rights plan and the self-tender were upheld as proportionate responses to a grossly inadequate $45 bid. The lock-up, no-shop and cancellation fee failed once the $50 and $53 bids made the break-up inevitable.
[Timestamp: 2026/10/23 12:10:26]

**user**: So the case itself calls the claim in revlon a duty of care claim. Has that since been rebranded into a duty of loyalty or caremark claim? My understanding is it still exists that Revlon claims can be brought. If so, how are they brought?
[Timestamp: 2026/10/23 12:27:50]

**ai**: There is no clean rebranding. The label has always been unstable, and the modern answer is to plead the claim by the kind of breach and the remedy you want.

**What *Revlon* itself says.** Your Revlon module notes that Chancery found a **loyalty** breach and the Supreme Court says the directors "breached their primary duty of loyalty." The conclusion then speaks of the "fundamental duty of **care**." The substance was a conflict: the directors spent stockholder value to extinguish their own noteholder exposure. That is also why § 102(b)(7) exculpation would not have saved them.

**It has not become a *Caremark* claim.** *Caremark* is about oversight failures and good faith, a different theory. The nearest bad faith route for sale claims is *Lyondell Chemical v. Ryan*, which the module describes this way: the question is not whether the directors did everything they should have, but whether they **utterly failed to attempt** to get the best price. That is a loyalty-flavored claim that exculpation does not reach.

**Revlon claims still exist, and are brought in these ways:**

| Route | How it works |
|---|---|
| **Pre-closing injunction (the main remedy)** | The module says *Revlon* and *Unocal* are "primarily designed to give stockholders and the Court of Chancery the tool of injunctive relief... in real time, before closing." Exculpation covers damages only, so it doesn't block this. Post-SB 21, § 144(d)(6)(b) preserves it. |
| **Damages, pleaded as loyalty** | The paradigm claim is "a conflicted fiduciary who is insufficiently checked by the board and who tilts the sale process toward his own personal interests." Loyalty claims aren't exculpated. |
| **Damages, pleaded as bad faith** | The *Lyondell* theory above. |
| **Aiding and abetting** | A claim against a third party that knowingly participated in a fiduciary breach. See [[Aiding and abetting a fiduciary breach - knowing participation]]. |

**What is largely gone.** A post-closing damages claim framed as plain care is hard. Exculpation eliminates care damages for directors, and a fully informed, uncoerced vote of the disinterested stockholders restores business judgment review under [[Cleansing by stockholder vote - Corwin and the fully informed vote]]. A conflicted-fiduciary claim generally defeats *Corwin* cleansing, because the board couldn't disclose the officer's machinations and so the vote wasn't fully informed.

**Direct, not derivative.** This is my application of *Tooley*, not something in the module. A claim that the sale price was too low is an injury to the stockholders' recovery, and the stockholders would receive any remedy. That points to a direct class claim, so no demand futility analysis would apply. Check that against your *Tooley* module before relying on it.
[Timestamp: 2026/10/23 12:27:50]

**user**: Can you explain the two measuers and the lock up? Like what exactly was Fortsmann given that made the 'win' the bid and therefore be able to takeover Revlon (if that's the right understanding)?
[Timestamp: 2026/10/23 13:10:40]

**ai**: Your understanding needs one correction. **Forstmann never took over Revlon.** Forstmann Little was the board's chosen white knight, and Pantry Pride was the hostile bidder. The Supreme Court affirmed the injunction against the lock-up, no-shop and cancellation fee. Your case file doesn't say who ended up owning Revlon.

**The two measures.** These were Revlon's early defenses against Pantry Pride, and the court upheld both under Unocal.

1. **Note Purchase Rights Plan (the poison pill).**
   - Each share carried a right to exchange a common share for a $65 one-year note at 12%.
   - The trigger was 20% beneficial ownership, and the acquiror couldn't use the right.
   - The board could redeem the rights for ten cents before the trigger.
   - It worked: it drove the bidding from $42 to $58, which the court called the proper result of a pill. The board's later decision to redeem the rights mooted it.
2. **Self-tender exchange offer.**
   - Revlon offered to swap each tendered share for a $47.50 Senior Subordinated Note at 11.75%, plus a tenth of a share of $9 preferred stock.
   - 87% of shares were tendered, and Revlon took 10 million pro rata.
   - The Notes' covenants limited new debt, asset sales and dividends unless the independent directors waived them. Those covenants stood in Pantry Pride's way, and later became the noteholder problem.
   - Authority was § 160(a), and the court held it a proper Unocal response to a grossly inadequate bid.

**What Forstmann was given.** On October 12 Forstmann offered $57.25 in return for these terms:

| Term | What it did |
|---|---|
| **Lock-up option** | Forstmann could buy the Vision Care and National Health Laboratories divisions for $525 million, which was $100–175 million below Lazard's valuation. It was exercisable if any other acquiror got 40% of Revlon's shares. |
| **No-shop** | Revlon agreed to negotiate only with Forstmann. |
| **$25 million cancellation fee** | A cost to Revlon if the deal fell through. |
| **Preferred treatment** | Forstmann had twice received Revlon financial data that Pantry Pride was denied, plus management cooperation and exclusive access to the board. |

**Why the lock-up ended the auction.** If Pantry Pride reached 40%, Forstmann could buy two valuable divisions cheaply, and Revlon would be worth much less to Pantry Pride. No rival could profitably bid once that option existed. The court held a lock-up is lawful when it draws a bidder into a contest and unlawful when it ends one. This one ended the auction, because Forstmann was already in the contest on a preferred basis and the price was well below value.

**What the board got.** The $57.25 bid was only $1 above Pantry Pride's $56.25 on its face, and less once discounted for the delay in closing. In return, Forstmann agreed to support the Notes at par. That protected the directors from noteholder claims, which the court identified as the main benefit of the deal, and that is why it was a loyalty problem.
[Timestamp: 2026/10/23 13:10:40]

**user**: So i guess in reality, what drove Revlon to not want to sell to Pantry but instead Fortsmann ? Outside of personal vendetta of the Board or the like, I would assume BJR could potentially justify other reasons?
[Timestamp: 2026/10/23 13:20:04]

**ai**: The board gave three reasons on October 12, and the court rejected each on the facts. No honest account of why Revlon preferred Forstmann is complete, but here is what the file shows.

**Stated reasons, and why they failed**
| Stated reason | Court's answer |
|---|---|
| Firmer financing | Any distinction was "nominal at best." About $400 million of Forstmann's money still rested on a best-efforts syndication, and Drexel had a firm commitment for Pantry Pride's balance by October 18. |
| Higher price | $57.25 beat $56.25 by $1 on its face and by less once discounted for the delay in closing. The auction ended for "very little real improvement." |
| Noteholder protection | The covenants contemplated a waiver for a fair-price sale, so there was nothing left to protect. Stockholders got no rationally related benefit. |

**Other drivers in the file.** The file's facts add these:
- Bergerac had a strong personal antipathy to Perelman.
- Early on, Pantry Pride's plan looked like a junk-bond bust-up. Lazard said it could return $60–70 a share to Pantry Pride, while a whole-company sale would land in the mid-fifties.
- The directors faced exposure to the noteholders. The court called avoiding that exposure the principal benefit of the deal.

**Could the business judgment rule justify other reasons?** The rule doesn't apply at this stage. The directors bear the burden under enhanced scrutiny, and the business judgment rule attaches only if they satisfy it.

Once the sale is underway, only price-related reasons count. But reasons that bear on the value of the bids are still legitimate:
- financing and its consequences,
- risk of non-consummation,
- the bidder's identity and plans,
- legality,
- fairness and feasibility.

The board can also weigh non-cash consideration, though it should try to quantify it. The module says a court won't second-guess a choice among reasonable alternatives, because the test is "a reasonable decision, not a perfect decision."

So Revlon's board could have preferred Forstmann if it had a genuine value-based reason. The constraints:
- **Favoritism** toward a white knight is justifiable only where the hostile bid adversely affects stockholder interests. It isn't justifiable when the bids are relatively similar.
- **Other constituencies** count only where rationally related benefits accrue to stockholders, and not at all during an active auction.
- **Personal dislike** isn't a legitimate objective. That's my inference from the module's framing, not a holding in the file.
[Timestamp: 2026/10/23 13:20:04]

**user**: so when does the standard of review move from EBJ to enhanced scrutiny in these cases?
[Timestamp: 2026/10/23 13:22:45]

**ai**: The standard doesn't start at business judgment and then move to enhanced scrutiny later. Enhanced scrutiny applies at the threshold, once certain facts are present. Business judgment review is where the board ends up if it passes. Your Unocal module says the board's action is "entitled to be measured by the standards of the business judgment rule" only after the directors satisfy both prongs.

**Why the threshold exists.** The "omnipresent specter" that a board is acting primarily in its own interests, here to keep control of the company. That is why the burden flips to the directors.

**What triggers each level**
| Situation | Standard |
|---|---|
| Ordinary board decision | Business judgment rule, if no fraud, illegality or conflict |
| Board action in response to a perceived threat to control, or any device protecting a transaction | **Unocal** enhanced scrutiny |
| Change of control, break-up, or active sale process | **Revlon**, meaning Unocal with price as the only legitimate objective |
| Conflicted transaction | Entire fairness unless a safe harbor applies |

**The Revlon trigger.** The module says it is objective, and the test is disjunctive. It applies when the transaction causes:
- a change in corporate control, or
- a break-up of the company.

It also applies where the company starts an active bidding process to sell itself. A board can't avoid the duty by declining to announce a sale.

**What doesn't trigger Revlon.**
- A stock-for-stock merger among dispersed holders ([[Paramount v. Time (1990)|Paramount v. Time]]).
- Deal protection devices alone. These get Unocal, not Revlon.

**Inside *Revlon* itself.** The same case applied different levels of Unocal to different measures:
- The rights plan and the self-tender were reviewed while the board was still defending the company, and they passed on a broad set of legitimate concerns.
- The lock-up, no-shop and cancellation fee were reviewed after the duty attached, so only price counted. The duty attached at the $50 and $53 bids, and the September 24 authorization to negotiate with third parties confirmed it.

The test for the trigger is where control sits before and after the transaction. Dispersed to dispersed is not a trigger. Dispersed to a single holder is.

**Afterward.** A fully informed, uncoerced disinterested stockholder vote after closing restores business judgment review under *Corwin*, whether or not *Revlon* applied. That's why enhanced scrutiny works mainly as an injunction standard.
[Timestamp: 2026/10/23 13:22:45]

**user**: What's a junk bond bust up that Lazard said Pantry Pride was doing initially?
[Timestamp: 2026/10/23 13:28:48]

**ai**: It's a type of leveraged takeover. The vault doesn't explain it, so the general mechanics below are from my own knowledge. The Lazard figures are from your case file.

**How a junk-bond-financed bust-up works**
1. The acquirer borrows heavily to buy the target, mostly by issuing high-yield ("junk") bonds. Those bonds are riskier, so they pay high interest.
2. The acquirer buys the target's shares.
3. It sells the target's divisions piece by piece. The proceeds pay down the debt.
4. Whatever the divisions sold for above the debt and the purchase price is the acquirer's profit.

Your file says Pantry Pride's bids were conditioned on financing. It also says Drexel had a firm commitment for Pantry Pride's balance by October 18. My understanding is that Drexel was the best-known junk-bond house of the period, but the file doesn't say so.

**Why Lazard cared.** Per your file, Lazard told the board that $45 was grossly inadequate. It said Pantry Pride's plan, properly timed, could return **$60–70 per share** to Pantry Pride, while a sale of the whole company would land in the **mid-fifties**. The gap shows what the divisions were worth in pieces. The acquirer would keep that difference, and Revlon's stockholders would not.

**Why that matters legally.** That analysis is the "threat" under Unocal prong one. A grossly inadequate price, plus the bust-up intention, gave the board reasonable grounds to adopt the rights plan and the self-tender. As the bids climbed to $50 and $53, they approached the whole-company sale value, and that is part of why the break-up became inevitable.
[Timestamp: 2026/10/23 13:28:48]

**user**: "The Notes covenants contemplated waiver for a sale at a fair price, so the noteholders were not wronged and there was nothing left to protect."

If this is true, why is there a problem with the notes convenant?
[Timestamp: 2026/10/23 13:40:19]

**ai**: The covenant isn't the problem. The problem is what the board did about the noteholders.

**The reasoning step.** The noteholders had no remaining claim. The covenants allowed a waiver for a sale at a fair price, and the holders accepted the market risk when they took the Notes. So when the board bargained to protect them, it was protecting something nobody was owed.

**Why that is a legal problem.** Once the duty is to get the best price for stockholders, protecting another group is allowed only if it brings stockholders a **rationally related benefit**. Here it brought them none. The board's actions:
- gave Forstmann the lock-up, no-shop and cancellation fee, which ended the auction for a $1 improvement, and
- in return, Forstmann agreed to support the Notes at par.

Stockholders paid for something that gave them nothing.

**Why it points to a conflict.** The announced waiver dropped the Notes from roughly par to 87.50. A "deluge" of angry calls followed, along with reported threats of litigation. The court identified the principal benefit of the deal as the directors extinguishing **their own exposure** to noteholders. Those claims were weak, because the Notes' terms contemplated the waiver. So the directors were using stockholder value to buy off a threat that had little merit, and the threat was to themselves. That is why the case reads as a loyalty case in substance.

Without the point, the board's rationale is at least coherent, since a board can think about creditors in some circumstances. Take away the creditors' claim and nothing connects the noteholder protection to stockholder value.
[Timestamp: 2026/10/23 13:40:19]

**user**: So who were the notes holder in this cae?
[Timestamp: 2026/10/23 13:41:31]

**ai**: The file doesn't name any individual noteholders, but it shows who they were as a group.

**Where the Notes came from.** The Notes were created by Revlon's own self-tender. For each share tendered, a holder received a $47.50 Senior Subordinated Note at 11.75% due 1995, plus a tenth of a share of $9 preferred stock. Stockholders tendered 87% of the outstanding shares, and Revlon took 10 million pro rata.

**Who held them.** The initial noteholders were former Revlon stockholders who swapped their equity for debt in that exchange. The numbers fit: 10 million shares at $47.50 is $475 million, which matches the $475 million of Note debt Forstmann agreed to assume in the October 3 deal.

**Caveats**
- Notes can be sold, and the file shows the Notes' price falling to 87.50 after the waiver was announced. By then some holders may have been investors who bought the Notes on the market. The file doesn't say who held them at the time of the dispute.
- Having been stockholders earlier did not give the holders stockholder rights. Once they exchanged their shares for Notes, they were creditors with fixed contractual rights.

That explains the court's logic about risk. Holders who took Notes with covenants allowing a waiver for a fair-price sale accepted the chance of an adverse market effect when they made the exchange.
[Timestamp: 2026/10/23 13:41:31]

**user**: I don't understand the notesholder point, if they are indeed stockholders, then what's the 'other group' besides the stockholders being protected?
[Timestamp: 2026/10/23 13:42:28]

**ai**: The group is the same people in a different role. The duty runs to people **as stockholders**, and the noteholders were being protected **as creditors**.

**What changed in the exchange.** A stockholder who tendered shares and had them accepted gave up that stock and received Notes. For those shares, that person stopped being an owner of Revlon and became a creditor of Revlon. The shares not taken were about 20 million. That figure is my arithmetic, from the roughly 30 million outstanding shares in the file minus the 10 million Revlon took.

**Why the roles pull in opposite directions in a sale.**
- **A stockholder** wants the highest price for the shares in the sale. That is what the directors owe in the sale.
- **A noteholder** is a creditor. What matters is that the debt is repaid and the covenants hold. A leveraged buyout that loads Revlon with new debt hurts creditors. That is why waiving the covenants dropped the Notes from roughly par to 87.50.

A person could hold both, for example by tendering some shares and keeping others. The law looks at which role the interest is in, and the sale price protects the stockholder role.

**What the board did.** Supporting the Notes at par was a benefit to creditors. It was paid for by giving Forstmann the lock-up, no-shop and cancellation fee, which ended the auction for a $1 improvement. The cost fell on the people who still held common stock and would have gotten a better price. The directors also got relief from the threatened noteholder litigation.

The court's point is that the noteholders were owed nothing more, since the covenants contemplated the waiver. Protecting them gave stockholders no benefit. It only benefited the creditors and, through them, the directors.
[Timestamp: 2026/10/23 13:42:28]

**user**: What are the two unocal standards again?
[Timestamp: 2026/10/23 14:15:36]

**ai**: Unocal has two prongs. The directors carry the burden on both.

**Prong one: a legally cognizable threat.** The directors must show they had reasonable grounds to believe a danger to corporate policy and effectiveness existed. They do that by showing good faith and reasonable investigation. A good process isn't enough on its own, because the board must also articulate a legitimate threat. Your module lists the three kinds of threat: structural coercion, opportunity loss, and substantive coercion.

**Prong two: the response is reasonable in relation to the threat.** It runs in two steps, in this order:
1. **The draconian screen.** Is the measure preclusive or coercive? Either one alone makes it impermissible, and the analysis stops. Delay is not preclusion.
2. **The range of reasonableness.** The specific nature of the threat sets the range of permissible responses.

If both prongs are satisfied, the board's action gets business judgment review.

**Omnicare.** Your module calls [[Omnicare v. NCS Healthcare (2003)|Omnicare v. NCS Healthcare]] the rare case where prong one is satisfied and the board still loses. The response was preclusive or coercive, so it failed the draconian screen. A well-founded threat and an exemplary process don't rescue a draconian response.

**Under *Revlon*.** Once the sale duty attaches, prong two's content changes: price is the only legitimate objective, so a measure justified on any other ground is disproportionate by definition.
[Timestamp: 2026/10/23 14:15:36]

**user**: so a 'threat' is still valid even if the board signed off on it? This doesn't seem like a hostile takeover?
[Timestamp: 2026/10/23 14:17:29]

**ai**: You're right that *Omnicare* isn't a hostile takeover, and Unocal doesn't need one. The module's trigger is any board action taken in response to a perceived threat to control, and any defensive device protecting a transaction.

**What the board signed.** The NCS board approved a friendly merger with Genesis, and the deal protections came with it. Those were the force-the-vote provision, the irrevocable voting agreements, and no effective fiduciary out. Omnicare was the outsider: a competing bidder whose later offer was worth more than twice the Genesis consideration.

**What the "threat" was.** The danger to NCS and its stockholders if the Genesis merger were not consummated. NCS was insolvent and in default on roughly $350 million of debt. The Genesis deal paid the senior debt in full, paid the Notes at par, and gave equity holders $24 million in stock. Without it they faced zero. Genesis also said it wanted a "bulletproof deal or they were not going to go forward." So the threat was losing the only value-creating deal, not an unwanted bidder.

**Does the board's sign-off validate the threat?** No, the sign-off is what triggers review. A board that adopts devices to protect its own deal is acting in a setting where the court worries the board is serving its own interests, so the burden is on the directors. They have to show a real threat and a proportionate response.

**How the case turned out.** The board passed stage one: good faith, reasonable investigation, and a real threat of losing the only deal. The Supreme Court said so. It lost at stage two. The combined devices guaranteed the merger's approval before any vote, so they were coercive and preclusive, and the case ended at the draconian screen. The board's own withdrawal of its recommendation shows the point: the devices still carried the deal through.
[Timestamp: 2026/10/23 14:17:29]

**user**: so when does a company actually change control? What's the key line where Revlon comes into effect?
[Timestamp: 2026/10/23 14:29:32]

**ai**: The line is where control sits before and after the transaction. Your Revlon module gives the working test: the duty attaches when the public stockholders lose the ability to obtain a control premium in a later transaction.

**The trigger.** Per [[Paramount v. QVC (1994)|Paramount v. QVC]], it is disjunctive. Revlon applies when a transaction causes:
- **a change in corporate control**, or
- **a break-up** of the corporate entity.

The module lists three routes in:
1. Break-up is inevitable and the board has embraced it, as in *Revlon*.
2. The company starts an active bidding process to sell itself.
3. A change of control, meaning the public stockholders are cashed out, or control passes to a controlling stockholder or group.

**The control-premium rationale.** Control is an asset of the public stockholders that can be sold only once. While it sits with "the fluid aggregation of unaffiliated stockholders," every holder keeps leverage to demand a premium later. Once it passes to one person or a cohesive group, the stockholders will have "no leverage in the future."

**Applying it**
| Transaction | Revlon? |
|---|---|
| Cash-out of the public stockholders | Yes |
| Control passes to a controlling stockholder or group (*QVC*) | Yes |
| Stock-for-stock merger among dispersed holders (*Paramount v. Time*) | No, because control stays in a fluid, unaffiliated market |
| Deal protection devices alone | No, these get Unocal only |

**What the module doesn't cover.** It gives no ownership percentage that counts as control. It also doesn't address mixed cash-and-stock deals, where the answer turns on how much of the consideration is cash and where control ends up. Check both against your class materials, because I'd be going from memory on any numbers.

**One caution.** The trigger is objective. Declining to announce a sale doesn't avoid the duty, and in *Revlon* the duty attached at the $50 and $53 bids, well before the Forstmann signing.
[Timestamp: 2026/10/23 14:29:32]

**user**: so isn't the first prong to Unocal a threat to control? So if there is no threat here, then how is unocal in play?
[Timestamp: 2026/10/23 14:31:43]

**ai**: Prong one isn't limited to a threat to control. Two things in your modules explain why Unocal applies here.

**1. The trigger is broader than control contests.** Your Unocal module's standard of review table gives two triggers: "Any board action taken in response to a perceived threat to control, **and any defensive device protecting a transaction**." Deal protections fall into the second.

**2. Prong one's wording in this setting.** In the original Unocal formulation, the danger is to "corporate policy and effectiveness" from another person's stock ownership. For deal protections, your deal protection module restates prong one as reasonable grounds to believe "a danger to the corporation and its stockholders existed if the merger were not consummated." In *Omnicare* that was the risk of losing the only value-creating deal. Unocal's own list of cognizable concerns also includes "the risk of nonconsummation."

**Why Unocal applies when control isn't changing.** Your deal protection module gives two reasons.
- *Paramount v. Time* settled that structural safety devices don't trigger Revlon but are properly subject to Unocal. That was the premise in *Omnicare*.
- A merger becomes final only on a stockholder vote, so the module says it is "a shared enterprise and ownership decision." A device that neutralizes the stockholders' half of that decision is reviewed with the board's burden on both prongs.

**Where your instinct is right.** *Omnicare* isn't a classic control fight, and the Unocal frame is stretched to fit it. Nothing was hostile except Omnicare's later competing bid, and that bid wasn't a threat to the board's control. The vault doesn't spell out why defensive devices attached to a friendly merger belong under Unocal beyond *Time* and the "shared decision" rationale above. If your professor gives a fuller account, that is where it would go in the module.
[Timestamp: 2026/10/23 14:31:43]

**user**: So I see the point that NCS stockholders tried to bring the same claim/did so. Would that be a direct claim, since the remedy would flow the stockholders themselves (their stock)?
[Timestamp: 2026/10/23 14:38:55]

**ai**: Yes, it's most likely direct. Your case file says only that "NCS stockholders brought parallel fiduciary claims," and I didn't see it classify them. This is my application of *Tooley*, not something in the file.

**Applying the two *Tooley* questions**
1. **Whose harm?** The injury is to the stockholders as stockholders. The devices made the merger approval a foregone conclusion, so the vote was emptied and a superior proposal was foreclosed. That injury exists independent of any injury to NCS. Your *Tooley* module says to ask whether the plaintiff "can prevail without showing an injury to the corporation." The stockholders can.
2. **Who gets the remedy?** The relief was an injunction against the Genesis deal. It doesn't pay anyone, but the benefit goes to the stockholders, who get a chance at the better proposal. A remedy that benefits the corporation would indicate a derivative claim, and this doesn't.

A small wording point: the test isn't whether the remedy flows to "their stock." It's whether the stockholders, not the corporation, are the ones who suffered and who benefit. In *Omnicare* that is the stockholders' vote and the price they would receive.

**Voting.** Your *Tooley* module says voting rights are among the clearest direct claims, and the *Omnicare* devices attacked the franchise directly.

**Demand futility.** A direct claim needs no demand or futility pleading. That matches your note on *Revlon* claims being direct.

**Omnicare the company** was a disappointed bidder, not suing as a stockholder, so *Tooley* doesn't classify its claim the same way. Check how the opinion handled the two sets of plaintiffs.
[Timestamp: 2026/10/23 14:38:55]

**user**: what is a mootness fee application?
[Timestamp: 2026/10/23 15:11:11]

**ai**: A mootness fee application is how plaintiffs' lawyers get paid when a deal lawsuit ends without a settlement. Your disclosure settlements module (it covers the *Trulia* decision) lists it as one of two adversarial channels, and the *Trulia* case file covers it too.

**How it works**
1. Stockholders sue over a pending deal, usually alleging that the proxy statement omitted or misstated something material.
2. The defendants voluntarily supplement the disclosures before the vote.
3. The claim is then **moot**, since the plaintiffs got the relief they sought.
4. Plaintiffs' counsel applies to the court for a fee for having caused the benefit.

**Why *Trulia* cares.** Before *Trulia*, these cases often ended in a disclosure-only class settlement. The defendants paid and the class gave a broad release in return. Your module says the court's fairness hearing for such a settlement is non-adversarial, since "both sides of the caption want approval." *Trulia* tightened approval to "plainly material" disclosures and a narrowly circumscribed release, and said disclosure claims "optimally should be adjudicated outside of the context of a proposed settlement."

**Why the fee channel works as an alternative.** Per the module, "defendants are incentivised to oppose a fee they view as excessive." That restores an opponent to the proceeding. The other channel is the contested preliminary injunction motion, where the plaintiff must show a reasonable likelihood of proving materiality.

**The unresolved tension.** The *Trulia* case file notes that this channel still pays counsel for disclosures the defendants chose to make, without any judicial finding of materiality. There is no class release, so there is nothing to scrutinize beyond the size of the fee. The adversary exists only over the fee.

**What the vault doesn't say.** It doesn't explain the standard a court uses to set the fee or how large fees tend to be. My understanding is that the doctrine ties the fee to a causal link between the lawsuit and the benefit conferred, but that's from memory, so check it against your class materials.
[Timestamp: 2026/10/23 15:11:11]

**user**: so MFW is largely superseded by 144(b) specifically, because that is what covers controller transactions?
[Timestamp: 2026/10/23 16:46:12]

**ai**: Largely yes, but it is § 144(b) and (c) together, and MFW survives in one place. Here is how your two modules put it.

| Transaction | Before SB 21 (MFW) | After SB 21 |
|---|---|---|
| Ordinary controller deal | Both protections, from the outset | § 144(b): **any one** of committee, disinterested vote, or fairness |
| Going private | Both, from the outset | § 144(c): committee **and** vote, or fairness (MFW codified) |

**So MFW is superseded for ordinary controller deals.** *Tesla 2* is the example. A disinterested vote with no special committee couldn't restore business judgment review under MFW and led to a trial. Under § 144(b) the vote alone suffices.

**MFW is codified for going private, not replaced.** Your safe harbors module describes § 144(c) as "MFW, codified — and confined to going private." The first step in any fact pattern is whether the deal is going private under § 144(e)(6).

**Differences from MFW even in the codified version.** These come from the modules and are worth checking against the statute:
- **Timing of the vote condition.** Under § 144(b)(2) it must be in the deal's terms "as in effect at the time it is submitted to stockholders," which is looser than MFW's ab initio requirement. Since § 144(c) points back to (b)(1) and (b)(2), the same looser timing may apply to going private, but the modules don't say so directly.
- **Committee mandate.** § 144(b)(1) requires the power to negotiate (or oversee negotiation) and to reject. MFW also required the committee to select its own advisors and to say no definitively. The safe harbors module doesn't list the advisor power as a statutory requirement.
- **What compliance buys.** MFW restored business judgment review. The statute goes further: the transaction "may not be the subject of equitable relief, or give rise to an award of damages" against directors, officers, or the controller.

**Not in the vault.** Neither module says whether SB 21 applies to deals closed before the amendment. It took effect March 25, 2025, according to your 220 and § 144 modules. Check that point before applying § 144 to an older transaction.
[Timestamp: 2026/10/23 16:46:12]

**user**: For a transaction that is not subject to entire fairness, is that goverened by 144(a)?
[Timestamp: 2026/10/23 16:48:10]

**ai**: No. Those two categories don't line up, and § 144(a) points the other way.

**§ 144(a) covers conflicted transactions.** Per your [[Interested director and officer transactions - 144(a)]] module, it supplies routes out of the common-law default for director and officer conflicts. That default is entire fairness, with the burden on the fiduciary ([[Bayer v. Beran (1944)|Bayer v. Beran]]). So § 144(a) is for transactions that *would otherwise* face entire fairness. Controller transactions are carved out of § 144(a) and go to § 144(b) and (c).

**"Not subject to entire fairness" is a category of review, not a statute.** The transactions that fall into it:

| Transaction | Standard | Statute or doctrine that matters |
|---|---|---|
| Ordinary board decision, no conflict | Business judgment rule | Usually none |
| Defensive measures, sale of control, deal protections | Enhanced scrutiny (Unocal, Revlon) | Common law |
| Any of the above, after closing, with a fully informed, uncoerced disinterested stockholder vote | Business judgment rule restored | *Corwin* |

**Corwin is the cleansing route here.** Your modules say Corwin "cleanses only transactions not subject to entire fairness." A controller on both sides takes the deal out of it, and the vote route there is § 144(b)(2).

**Order of analysis**
1. Is a director or officer conflicted? § 144(a) is relevant.
2. Is a controller on the other side? § 144(b) or (c), not § 144(a).
3. Neither, and the deal is an enhanced-scrutiny deal closed after a fully informed disinterested vote? *Corwin*.
4. Otherwise, business judgment rule.
[Timestamp: 2026/10/23 16:48:10]

**user**: So Corwin is mainly for post closing suits? Becuase I would think, beforehand, there would be no reason to cleanse if BJR is presumed to apply?
[Timestamp: 2026/10/23 16:49:17]

**ai**: Yes, it's a post-closing damages doctrine, but the reason is different from the one you gave. The business judgment rule is not presumed to apply in these deals, so there is something to cleanse.

**Why there's something to cleanse.** In the transactions Corwin covers, the board's conduct is reviewed under enhanced scrutiny (Unocal or Revlon), not the business judgment rule. The directors carry the burden of showing a reasonable decision-making process and a reasonable action. Your Corwin module's rule statement says an informed, uncoerced, disinterested vote "invokes the business judgment rule" even where Revlon would otherwise apply. So the vote moves the case from enhanced scrutiny to business judgment review.

A transaction already under the business judgment rule needs no cleansing. An ordinary decision with no conflict needs neither Corwin nor § 144.

**Why Corwin is post-closing only.** The module says "Reach: Damages only. Pre-closing injunctive relief is untouched." The rationale in the module is that Unocal and Revlon exist to give stockholders and the court "the tool of injunctive relief... in real time, before closing." The damages claims were never what those standards were built for. Corwin's reasoning also leans on cost and mismatch: due care liability is "rarely even available" given exculpation, and informed stockholders "can easily protect themselves at the ballot box by simply voting no."

**What cleansing does.** The module says the vote does not ratify the breach. It changes the standard of review. The plaintiff must then plead waste or bad faith, and most such suits end on the pleadings.

**Timing.** The stockholder vote comes before closing, but its effect is in the later damages suit. A pre-closing plaintiff can still seek an injunction under Unocal or Revlon. If the deal closes, a damages claim runs into Corwin if the vote was informed and uncoerced.
[Timestamp: 2026/10/23 16:49:17]

**user**: So it would ordinarily be under enhanced scrutiny? And when does enhances scrutiny apply again?
[Timestamp: 2026/10/23 16:51:02]

**ai**: Not ordinarily. Enhanced scrutiny applies only in particular settings. The default is the business judgment rule. Your Unocal module's standard of review table gives the trigger as "any board action taken in response to a perceived threat to control, and any defensive device protecting a transaction." Other modules add two more settings.

| Setting | Why enhanced scrutiny |
|---|---|
| **Defensive measures** against a perceived threat to control (pills, self-tenders) | The board may be acting in its own interest, so the directors carry the burden under Unocal. |
| **Deal protection devices** (lock-ups, no-shops, voting agreements) | Reviewed under Unocal even with no change of control (*Omnicare*). |
| **Sale of control** (a change of control, a break-up, or an active sale process) | Revlon, which is Unocal with price as the only legitimate objective. |
| **Interference with the stockholder franchise** | Per your Unocal module, historically this drew Blasius review. *Coster* appears to fold it into a Unocal-shaped inquiry. |

**Settings that don't get it**
- An ordinary decision with no conflict: business judgment rule.
- A conflicted director or officer transaction, or a controller transaction: entire fairness by default, with § 144 safe harbors. Enhanced scrutiny is the intermediate standard between the two.
- Stock-for-stock mergers among dispersed holders: no Revlon duty (*Paramount v. Time*), though devices attached to them still get Unocal.

**The standard.** Enhanced scrutiny is an intermediate standard. It examines the reasonableness of the process and of the action, and the directors bear the burden. The test is "a reasonable decision, not a perfect decision."

**How it ties to Corwin.** If the transaction falls in one of these settings, enhanced scrutiny governs the board's conduct in a pre-closing injunction suit. After closing, an informed, uncoerced disinterested vote under *Corwin* resets the standard to business judgment review for the damages claim.
[Timestamp: 2026/10/23 16:51:02]

**user**: So in Corwin, why was there even a question on if Revlon applied? Was it a merger/change of control case?
[Timestamp: 2026/10/24 14:57:00]

**ai**: Yes, it was a merger. The file calls it "a stock-for-stock merger with KKR," and the plaintiffs sued after the merger closed.

**Why Revlon came up.** It was the plaintiffs' fallback. Their main argument was that KKR was a controlling stockholder, which would make entire fairness the standard and keep the case alive. The court rejected that: KKR held under 1%, appointed no directors, and had no veto. The plaintiffs then argued that if entire fairness didn't apply, Revlon did, and that they had pleaded a Revlon claim that should survive dismissal.

**Whether it was a change of control.** The file doesn't say. The court expressly declined to decide whether Revlon governed the merger: "it does not matter." The vote was fully informed, uncoerced and cast by disinterested stockholders, so business judgment review applied either way. The file also says the Revlon argument "was not fairly presented below" and failed on the merits in any event.

**Whether the argument was plausible.** I'd treat this as my own reading of the facts, not the court's. A merger that leaves a company under one acquirer's ownership resembles the change of control in your Revlon module, where control passes to a single holder and the public stockholders lose a future control premium. Your Revlon module also says stock-for-stock mergers among dispersed holders usually aren't triggers. The file doesn't analyze which description fits KKR and Financial Holdings, and the court avoided the question.

**Why this is useful for your outline.** *Corwin* is where the courts show that you can skip the Revlon trigger question altogether in a post-closing damages case against a non-controller board. If the vote was informed and uncoerced, the trigger doesn't matter.
[Timestamp: 2026/10/24 14:57:00]

**user**: So post Sb 21, the safe harbor applies for both controller and non-controller transactions (144(a) and 144(b)), so Corwin is basically now statourily explicit?
[Timestamp: 2026/10/24 15:16:42]

**ai**: Partly, but the statute reaches different transactions than *Corwin* does.

**Where the statute applies.**
- **§ 144(a)** covers director and officer conflicts. Route 2 is approval by an "informed, uncoerced, affirmative vote of a majority of the votes cast by the disinterested stockholders."
- **§ 144(b)** covers controller transactions. Route (b)(2) is the same kind of vote.

Both are vote-based safe harbors, and your Corwin module says § 144(b)(2) is "cleansing by vote, promoted from common law to statute and extended into the controller context."

**Where *Corwin* applies.** Only to transactions **not subject to entire fairness**: no controller and no conflicted director or officer. Your Corwin module's analysis order says that when there is no conflict or controller, § 144 does not apply, and you use *Corwin*, *Revlon* and *Unocal*. So *Corwin* is not now statutory. Its core territory, a non-conflicted deal facing a post-closing Revlon or Unocal damages claim, is outside § 144 entirely.

**What the statute adds.** The safe harbors cover conflicted transactions that previously faced entire fairness. They are close relatives of *Corwin*, not a codification of it.

**Different effects**
| | *Corwin* (common law) | § 144(a)(2) and (b)(2) |
|---|---|---|
| Transaction | No conflict or controller | Conflicted director or officer, or controller |
| Effect | Business judgment review in a post-closing damages suit | No damages and no equitable relief against directors, officers, or controllers |
| Injunction | Untouched | Covered by the safe harbor, subject to the § 144(d)(6) savings clauses |

**Your conclusion.** The idea that an informed disinterested vote protects a deal is now explicit in statute for conflicted and controller transactions. *Corwin* itself remains common law, for the non-conflicted deals the statute doesn't reach.
[Timestamp: 2026/10/24 15:16:42]