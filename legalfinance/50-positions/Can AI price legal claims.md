---
question: Can AI price legal claims well enough to change the economics of funding?
topic: Market structure
status: live
class: legalfinance
sessions: [9]
---

## The question

Litigation funding is expensive because underwriting is expensive and outcomes are uncertain.
If machine learning can assess claims faster and predict outcomes better, both halves of that
sentence change: diligence cost falls, required return falls, and the minimum viable deal size
falls with them.

So this is not a technology question. It is a question about whether the industry's **cost
structure and its floor** are about to move — and therefore whether the access-to-justice
defence, which currently cannot reach small claims, ever becomes true.

## The case for

- **Diligence is the fixed cost, and it is the one AI attacks.** Reviewing a case takes lawyer
  weeks regardless of claim size, which is why [[Burford - Legal Finance 101]] sets a floor at
  $3m of financing against ~$30m of damages. Compress the review and the floor falls.
- **Marra's formulation**: machine learning tools will "more quickly analyze cases," which
  should "decrease the cost of litigation funding, since machine learning input will decrease
  the risk," and let funders "profitably finance smaller cases previously overlooked due to
  review costs."
- **It is already happening at smaller sizes.** Qanlex writes **$100,000 to $3m** per case in
  Latin America and Europe using its "Case Miner" screening tool — an order of magnitude below
  Burford's floor.
- **Sourcing genuinely works.** Legalist's "truffle sniffer" sorts dockets by court, judge and
  case type; Burford runs web-scraping to build prospect databases; Parabellum automates
  portfolio management. These are in production, not pilots.
- **Screening out is the easy half and it is the half that matters.** A non-recourse funder's
  core discipline is rejecting bad cases, not valuing good ones perfectly. Apex uses predictive
  tools "primarily to reject unsuitable cases" — pointing AI at exactly the function
  [[Antill and Grenadier - Financing the Litigation Arms Race]] says the economics require.
- **Latent claims.** Marra argues AI can surface disputes nobody has identified, which expands
  the market rather than redistributing it.

## The case against

- **The dependent variable is missing.** Roughly **90% of commercial disputes settle
  confidentially**, so what a case was actually worth is unobservable in nine of ten
  observations. Perla, at the largest funder: "models are only as good as the data fed into
  them," and "if models are constructed using flawed or limited data, the predictions they
  generate will also be flawed."
- **Everyone doing it says it does not underwrite.** Eva Shang of Legalist: "It does not do
  things that an underwriter would normally do. There's still a very important human
  component." Steve Power of Apex: AI is "only as good as the data that it has available to it."
  Perla: AI "is not yet capable of making investment decisions." That is remarkable consistency
  across five firms with every incentive to claim more.
- **Proxies optimise for the wrong thing.** A model trained on judge and jurisdiction learns
  where plaintiffs win — a forum signal, not a merits signal. Swiss Re's finding that
  plaintiff-friendly counties track low income, high unemployment and inequality shows what such
  a model would actually be selecting on.
- **The training set is the tail.** The ~10% of disputes with public outcomes are the ones that
  did **not** settle — systematically harder, longer and more contested. That is the same
  adverse selection [[Slingshot Capital - Secondary investing in litigation finance]] describes
  in secondaries, appearing in the training data.
- **The claim runs the other way too.** Marra concedes that if AI lowers litigation costs
  generally, well-capitalised parties need funding **less**. Cheaper litigation could shrink
  demand faster than cheaper diligence expands supply.
- **Nothing automates the courtroom.** Chief Justice Roberts, quoted by Marra: "[m]achines
  cannot fully replace key actors in court."

## What the evidence actually shows

- **A clean split between funders, in the same year, and it is not random.** Marra — then at a
  smaller firm — argues AI lowers cost and opens the bottom of the market. Perla — at the
  largest funder, with the largest underwriting team — argues the data to do that does not
  exist. **A big incumbent benefits from underwriting being unautomatable; a smaller entrant
  benefits from the opposite.** Neither claim can be checked, because neither firm's models or
  loss rates are public.
- **The reported uses are consistently upstream of pricing.** Sourcing, screening, outreach,
  portfolio ops, issue-spotting. Every named application is origination or operations. No firm
  claims to price with it.
- **The one piece of hard evidence for the optimistic case is deal size.** Qanlex at $100k–$3m
  is a real data point, in real transactions, well below the incumbent floor. It is also one
  funder, in two non-US markets, with no reported returns.
- **This is the fourth place the confidentiality problem binds.** GAO could not size the market;
  Westfleet's data is voluntary and unaudited; secondaries have no benchmark because marks are
  unauditable; and now models cannot be trained. The opacity that protects the industry
  commercially limits its measurement, its valuation, its regulation **and** its tooling. That is
  the strongest through-line in the whole course.
- **What would settle it**: back-tested predictive accuracy against realised outcomes on a
  sample including settlements. Only the funders hold that data, and only Burford is reported to
  be testing on closed cases.

## Where the law is now

- **Nothing regulates AI use in funding specifically.** No disclosure obligation attaches to
  how a funder selected or priced a case.
- **Docket mining is lawful** — court records are public — but it sits adjacent to the claim
  **solicitation** rules. [[New York Consumer Litigation Funding Act]] bans referral fees to
  attorneys and medical providers, bans referring consumers to specific attorneys, and bans false
  or misleading advertising. AI-driven first outreach to identified claimants runs close to that
  line in consumer matters, and nobody on this syllabus discusses it.
- **The disclosure proposals do not reach it.** Neither the LCJ/ILR Rule 26 amendment nor S. 3826
  requires anything about underwriting method; both reach the agreement and the funder's
  identity.
- **Professional conduct rules bind the lawyer, not the model.** Where an MSO owns the firm's
  technology, the question of who is exercising professional judgment over AI output is
  unaddressed. [[Law firm MSOs]].

## My view
