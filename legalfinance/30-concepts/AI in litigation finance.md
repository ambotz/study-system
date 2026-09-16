---
concept: AI in litigation finance
topic: Market structure
kind: market
class: legalfinance
sessions: [9]
---

## What it is

What machine learning is actually doing in this market as of 2024–26, and — more usefully —
what it cannot do and why. The gap between the two is a data problem, not a technology problem.

## How it works

Four functions, in descending order of how well AI performs them:

| Function | What it does | Maturity |
|---|---|---|
| **Sourcing** | Mines dockets to surface cases matching investment criteria, by court, judge and case type; identifies specialised lawyers; automates first outreach | **In production.** Legalist's "truffle sniffer," Qanlex's "Case Miner," Burford's web-scraping project |
| **Screening out** | Rejects clearly unfundable matters | **In production**, and the most honest use — Apex uses predictive tools "primarily to reject unsuitable cases" |
| **Early assessment** | Issue-spotting and identifying elements of the cause of action | Partial. Perla: "most effective in early-stage issue-spotting" |
| **Pricing and the investment decision** | Valuing the claim and setting terms | **Not achieved.** Perla: AI "is not yet capable of making investment decisions"; Shang: "It does not do things that an underwriter would normally do" |

**The binding constraint is the missing dependent variable.** Roughly **90% of commercial
disputes settle confidentially**, so the outcome a pricing model needs — what the case was
actually worth — is unobservable in nine cases out of ten. Models train on **proxies**:
jurisdiction, judge, case type, docket behaviour. "[M]odels are only as good as the data fed
into them."

## Why it exists

Because diligence is the funder's real cost structure. Underwriting a claim means lawyers
reading a case for weeks, and that cost is roughly **fixed per matter** regardless of size —
which is why [[Burford - Legal Finance 101]] sets a floor at $3m of financing against ~$30m of
expected damages. Anything smaller does not repay the review.

That is the whole economic significance of AI here, and it is Marra's argument: if machine
learning compresses diligence cost, the floor drops and funders can profitably write **smaller
cheques**. Qanlex writing **$100,000 to $3m** per case is what that looks like in practice.
Whether it generalises is the open question.

## Variants

- **Docket mining** — supply-side origination from public filings.
- **Portfolio management tools** — Parabellum's proprietary system; operations rather than
  underwriting.
- **Rejection screens** — the Apex approach, and the easiest problem in the set.
- **Back-testing on closed cases** — Burford testing models where outcomes are known, which is
  the only place the data exists.
- **AI as the reason firms need capital** — the demand-side mirror. Technology and AI lead
  Holland & Knight's list of MSO drivers. See [[Law firm MSOs]].

## What can go wrong

- **Proxy variables encode the wrong thing.** A model trained on judge and jurisdiction learns
  where plaintiffs win, which is a forum-shopping signal, not a merits signal. Swiss Re's own
  finding that plaintiff-friendly counties correlate with low income, unemployment and
  inequality is a warning about what such a model would optimise for.
- **Survivorship in the training set.** The ~10% of disputes with public outcomes are the ones
  that did not settle — systematically the harder, more contested, longer cases. Training on
  them is training on the tail, the same adverse-selection problem
  [[Syndication, secondaries and securitisation]] describes for secondaries.
- **Overclaiming to investors.** A funder's predictive edge is unauditable for the same reason
  its marks are: the underlying is confidential.
- **Automating origination without automating underwriting** raises deal flow without raising
  screening capacity, which is a good way to lower average quality.
- **The confidentiality trap.** The industry's opacity is commercially useful and is now the
  binding limit on its own tooling, its measurement, its valuation and its regulation.

## Where it shows up

- [[Perla - The current and future state of AI in legal finance]] — the three uses and the
  90/10 data problem.
- [[Siegel - AI Helps Litigation Funders Mine Court Dockets]] — the named tools, deal sizes and
  the limits stated by five funders.
- [[Marra - AI and the Future of Litigation Funding]] — the claim that AI lowers risk and
  therefore the cost of funding, and opens smaller cases.
- [[Furlong - The Identity Opportunity for Lawyers]] — the demand side.
- [[Can AI price legal claims]] — the contested question.
