---
epoch: 1791841919021
mode: agent
backendId: claude
sessionId: "9f55c5e1-b7a2-44d7-9aa5-7fd0f6a2e618"
agentLabel: "Is it true that there is asymmetrism in the sense that the o…"
usage: '{"usedTokens":43089,"contextWindow":1000000,"inputTokens":2,"outputTokens":6,"cacheReadTokens":42248,"cacheWriteTokens":833,"updatedAt":1792001374032}'
tags:
  - copilot-conversation
---

**user**: Is it true that there is asymmetrism in the sense that the only way to end a war is through a treaty and two thirds of the senate? Can't a bill be passed ending the war too?
[Timestamp: 2026/10/12 16:51:59]

**ai**: No. The asymmetry is real, but it applies only to ending a war by treaty. [[Terminating War]] says a war can end three ways.

- **Treaty.** The Convention rejected Madison's proposal to make peace treaties easier to approve than other treaties. A peace treaty therefore needs the President and two-thirds of the Senate, while a declaration of war needs only majorities of both Houses. That is the asymmetry the note describes.
- **Legislation.** *Ludecke v. Watkins* (1948) says the "state of war" "may be terminated by treaty or legislation or Presidential proclamation," and that termination is "a political act." So a bill can end a war. The Iraq authorizations are the note's example: the FY2026 NDAA (December 2025) repealed the 1991 and 2002 AUMFs.
- **Presidential proclamation.** *Ludecke* lists this as a third mode.

Two limits on the bill route come from the note and from general principles, not from anything *Ludecke* says.

1. **Repeal alone may not stop a President.** Congress repealed the Tonkin Resolution in 1971, but Nixon kept fighting under his Commander in Chief authority, and Congress kept funding the war. Whether repeal binds depends on whether the President has an independent Article II claim. That is the whole war-powers dispute.
2. **Defunding is the effective tool.** A funding cutoff is Youngstown category three and works through the Appropriations Clause (Art. I, § 9, cl. 7), which the President can't override. The note credits the later funding cutoff with the U.S. withdrawal from South Vietnam.

I'm adding one point not in the note. Any such bill is still subject to a presidential veto. If the President opposes ending the war, Congress needs two-thirds of both Houses to override, so the two-thirds requirement can come back in through the veto.

Separately, this session couldn't use several claude.ai connectors (Gmail, Google Drive, Github, and others) because they need authorization. You can authorize them in your claude.ai connector settings. I didn't need any of them for this question.
[Timestamp: 2026/10/12 16:51:59]

**user**: so, is presidential prclomation similar to an executive order
[Timestamp: 2026/10/12 16:53:42]

**ai**: Similar, but not the same, and the difference matters less than the shared source of authority.

**What they have in common.** Both are unilateral presidential instruments. Neither goes through Congress. Both are published in the Federal Register. Both are valid only if the President has authority from the Constitution or a statute. *Youngstown* applies to both: an executive order that seized the steel mills failed in category three, and a proclamation would fail the same way.

**How they differ.**

- **Function.** Executive orders mostly direct the executive branch. They tell agencies and officers how to run the government. Proclamations more often address the public or announce a fact or status, such as a holiday, a national emergency, or the end of hostilities.
- **Legal effect.** Neither one has legal force of its own. Each one works only through the authority behind it. A proclamation that a statute calls for does have legal effect, such as one invoking a tariff or immigration power.
- **Formality.** The distinction is largely customary, and the labels are not rigidly separate. The Emancipation Proclamation is in your vault, and it worked as an exercise of the Commander in Chief power.

**For *Ludecke*.** The proclamation there was probably the declaratory kind. It announced that the "state of war" had ended, which triggered or ended the statutory powers that depend on that status (the Alien Enemy Act of 1798, in *Ludecke*). The Court treated that as a political act, so it deferred. The President's authority came from the war-powers statute and his role in foreign affairs, not from the word "proclamation."

That is also why the note's variation on the facts hedges. A proclamation likely ends the "state of war" for statutory purposes, but Congress could legislate otherwise. Under *Youngstown*, a proclamation that conflicts with a statute puts the President in category three, where his power is at its lowest.

I'm answering from general knowledge of the distinction, not from anything in the vault. The note doesn't discuss how proclamations differ from executive orders.
[Timestamp: 2026/10/12 16:53:42]

**user**: what does it mean that NY enacted remedies adn rejeced at the same time ?
[Timestamp: 2026/10/14 13:08:31]

**ai**: It means New York's Consumer Litigation Funding Act did what the authors recommended and also did what they warned against, in one statute. This comes from the seminar hooks in your note on Skiba and Xiao.

**What the authors recommended**
- Plain disclosure of an approximate repayment amount and date, not an APR.
- Attorney acknowledgment that the costs were disclosed.

**What they rejected**
- Caps on rates, fees, or terms, which they said "hurt low-income borrowers and are easily evaded."
- They also rejected outright bans, as premature.

**What New York did (Chapter 645, per your note)**
- It requires disclosure of the funded amount, itemised charges, the maximum owed, and the payment schedule, all in 12-point bold. That's close to what they proposed.
- It requires the attorney acknowledgment they proposed.
- It also caps the funder's take at 25% of gross proceeds. That is a characteristic restriction, the kind of remedy the authors said would backfire.

**Why it matters**
- The paper's case against caps is asserted, not demonstrated. Your note says no litigation-funding-specific evidence is offered, and no state had evaluable experience with caps in 2017.
- New York now gives a test. If low-income plaintiffs end up worse off, or funders restructure around the cap, the authors were right. If not, they were wrong. Your note flags this as a good final-paper subject.
- The paper is from 2017, so it couldn't have anticipated the Act. The note says to read it as an analytical frame, not as a current statement of the law.

I'm relying on your note's account of Chapter 645, not on the statute's text. Check the 25% cap and the disclosure details against the Act before you cite them.

Several claude.ai connectors still need authorization in your claude.ai connector settings. I didn't need any of them for this.
[Timestamp: 2026/10/14 13:08:31]

**user**: how do the caps hurt low-income borrowers?
[Timestamp: 2026/10/14 13:09:25]

**ai**: Your note doesn't say. It records only that the authors assert caps hurt low-income borrowers, and it calls this "the standard consumer-credit finding" with no evidence specific to litigation funding. The mechanism below is the general consumer-credit argument, from my own knowledge and not from the paper.

**Rationing.** A funder prices the risk of losing its whole advance, because the advance is non-recourse. If a cap pushes the allowed return below what that risk requires, funders stop making the riskiest advances. The plaintiffs with weak or uncertain cases, who are often the most cash-constrained, can't get funded at all. They keep the need and lose the option.

**Worse substitutes.** A plaintiff who is turned down still needs money for rent or medical bills. They may turn to payday loans, title loans, or credit cards, or settle early for less. Those can cost more than the capped funding would have, and unlike non-recourse funding they are recourse debt, so the debt-trap risk returns.

**Evasion.** Funders can restructure to get around a cap. They might add fees outside the capped category, shift to a different instrument, or relabel the deal. The cost of those workarounds can fall on borrowers, who also get less transparent terms. That is the "easily evaded" half of the authors' claim.

**Applying it to New York.** The cap is 25% of gross proceeds (per your note). Whether it bites depends on whether funders can still make acceptable returns on risky cases under it. A funder whose pricing assumed a larger share on weak cases has to drop them or find a workaround. That is the empirical question your note flags.

**Counterpoint for the paper.** The rationing story assumes the foregone loans were good for the borrowers. If the pricing is as extreme as the paper says (200%+ APR), one could argue some of the lost deals were ones the borrower shouldn't have taken. The authors' own point that plaintiffs can't predict settlement size or date supports that view, because borrowers may not know what they're agreeing to. That tension is worth raising in seminar, since the authors assume rationing is a harm without testing it.
[Timestamp: 2026/10/14 13:09:25]