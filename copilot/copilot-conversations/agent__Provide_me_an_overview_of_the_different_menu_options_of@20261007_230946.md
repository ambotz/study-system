---
epoch: 1791432586042
mode: agent
backendId: claude
sessionId: "edf9a1a9-16ba-4a89-b324-c85361daac16"
agentLabel: "Provide me an overview of the different menu options of how…"
usage: '{"usedTokens":36650,"contextWindow":1000000,"inputTokens":2,"outputTokens":2,"cacheReadTokens":33815,"cacheWriteTokens":2831,"updatedAt":1791433112786}'
tags:
  - copilot-conversation
---

**user**: Provide me an overview of the different menu options of how a cleansing can go. Especially, I don't understand how entire fairness is autmoatically triggered if the controlling stockholder is on both sides.
[Timestamp: 2026/10/07 23:09:46]

**ai**: # Cleansing routes and why a controller on both sides triggers entire fairness

I worked from the Corwin module you attached. The § 144(b)/(c) details below come from my own knowledge of SB 21, not from your vault. Check them against the statute text before relying on them.

## The menu

The first question is whether a controller stands on the other side of the deal. That decides which route is open.

| Situation | Cleansing route | Result |
|---|---|---|
| **No controller** (third-party merger, as in [[Corwin v. KKR Financial Holdings (2015)\|Corwin]]) | Fully informed, uncoerced vote of disinterested stockholders (Corwin, now § 144(b)(2)) | Business judgment rule (BJR) in a post-closing damages suit. Dismissal on the pleadings follows. |
| **No controller, conflicted directors or officers** | Disinterested-director approval or a disinterested stockholder vote (§ 144 safe harbour) | BJR |
| **Controller, going-private buyout** | [[Controller buyouts - the MFW dual protection structure\|MFW]]: a special committee and a majority-of-the-minority vote, both conditioned up front. Post-SB 21, § 144(c) as I recall it. | BJR |
| **Controller, other conflicted deal** | Pre-SB 21, MFW. Post-SB 21, § 144(b), which as I recall lets either a committee or a minority vote suffice. | BJR |
| **Nothing works** | None | Entire fairness (fair dealing and fair price), with the defendants carrying the burden |

Two limits apply to every route:
- Cleansing changes the standard of review. It does not ratify a breach.
- Waste and bad faith claims survive, and so do pre-closing injunction claims.

## Why a controller on both sides triggers entire fairness

The logic runs in four steps.

1. **The BJR presumes a disinterested decision-maker.** The presumption is that people with no stake in the outcome, acting on an informed basis, are better placed than a judge to decide. A controller on both sides is the conflicted party, and the presumption has nothing to rest on.
2. **The board cannot be treated as independent.** The controller can remove the directors who approve the deal. A board approval is therefore not the arm's-length judgment the BJR assumes.
3. **The minority vote is not free either.** *Kahn v. Lynch* is the usual cite: the controller's power makes the vote inherently coercive. The minority may vote yes out of fear of retribution, such as the controller starving the company or dumping its shares. This is the step that matters most for your question.
4. **That is why Corwin cannot reach this case.** Corwin works only because a vote of disinterested holders can safely be trusted. Where a controller is present, the premise fails. Your module's gateway element says this: "Entire fairness does not apply... checked first."

Entire fairness is the baseline standard whenever a fiduciary sits on both sides. The cleansing routes are the ways back to the BJR. In a controller deal, MFW or § 144(b)/(c) is how you get there, because those structures try to rebuild what the controller's presence destroyed. MFW does that with a committee that can say no plus a vote the controller cannot dictate.

## Three nuances

- **"Automatic" is a little too strong.** The plaintiff still has to plead that a controller exists and that the controller is conflicted. That means either on both sides, or taking a non-ratable benefit. A controller who sells alongside the minority for the same per-share price and gets nothing extra generally does not trigger it.
- **Entire fairness is a standard, not a finding of liability.** The controller can still win by showing fair dealing and fair price. It is just a much harder and costlier position, and it usually blocks early dismissal.
- **Corwin itself was a control case.** KKR held under 1%, had no power to appoint directors and had no veto. That is why entire fairness did not apply, and why Corwin could then cleanse. You can see this in the controller-gateway table in your module.

If it helps, I can draw this as a flowchart for the outline. I can also read [[Controlling stockholder transactions - the self-dealing trigger]] and the MFW module to check that they line up with the table above.

One unrelated note: several claude.ai connectors, such as Gmail, Google Drive and GitHub, need authorization before I can use them. They are unavailable in this session, and you can authorize them in your claude.ai connector settings.
[Timestamp: 2026/10/07 23:09:46]

**user**: So revlon is pre-closing. What exactly does it help/provide?
[Timestamp: 2026/10/07 23:18:22]

**ai**: # What Revlon provides

Revlon is an enhanced-scrutiny standard of review. It applies when the board is selling the company in a way that ends the stockholders' ongoing stake in it. Its main practical use is as a tool for getting an injunction before closing. I'm working from general knowledge here and haven't read your Revlon module.

## When it applies

Revlon applies in three situations:
- **Cash sale.** The company is sold for cash.
- **Break-up.** The company is broken up or sold in pieces.
- **Change of control.** The deal moves control from a dispersed market to a controller. This includes a stock-for-stock deal where the stockholders' stake ends up in a controlled entity.

A stock-for-stock merger into a widely held company generally does not trigger it. *Paramount v. QVC* is the main case on the control-shift trigger.

## What it does

1. **It changes the duty's focus.** The board's job becomes getting the best price reasonably available for the stockholders. In the Revlon image, the board shifts from "defenders of the corporate bastion to auctioneers."
2. **It changes the standard.** Instead of the business judgment rule (BJR), the court asks whether the board's process and decision were reasonable. The defendants carry the burden of showing reasonableness.
3. **It reaches the process.** The court looks at who ran the sale and whether the board was informed. It asks whether the board tested the market, whether anyone was conflicted, and whether deal protections shut out other bidders. For those protections, [[Deal protection devices - Unocal review of merger lock-ups]] applies in tandem.

## What it does not require

- **An auction.** There is no single blueprint. A board can sell without one if it is informed and acting reasonably, and a well-run process can rest on a market check of another kind.
- **The highest price at any cost.** The standard is price reasonably available, and it is judged on reasonableness. It does not demand a perfect result.

## Why it matters for the injunction

Before closing, stockholders can still ask for an injunction. They can seek to stop the vote or to force a better process and better disclosure. Revlon gives that request its legal hook: if the sale process was unreasonable, the court can enjoin it or require fixes. Corwin says this directly, in the language quoted in your module: Unocal and Revlon exist "to give stockholders and the Court of Chancery the tool of injunctive relief... in real time, before closing."

After closing, an injunction is no longer possible. The remedy becomes damages, and a Revlon claim for damages runs into two problems:
- **Exculpation.** Under § 102(b)(7), directors are generally exculpated for duty-of-care breaches, so a Revlon claim often fails to produce liability.
- **Cleansing.** Corwin cleansing removes the claim where a fully informed, uncoerced vote of disinterested stockholders approved the deal.

So Revlon is still fully alive before closing. After closing, it matters mostly in the exceptions your module lists, such as a conflicted fiduciary who hid information from the board (the *Mindbody* line).

## One exam point

The best statement of the relationship is the trap in your module: Revlon is not dead after Corwin. Corwin kills the post-closing Revlon damages claim against a non-controller board whose stockholders were properly informed. The pre-closing injunction claim survives.

I can also read your Revlon module and check that this matches your professor's framing.
[Timestamp: 2026/10/07 23:18:22]