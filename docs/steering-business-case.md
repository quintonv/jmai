# Steering: Voice, Tone and Points to Cover

Derived from the one reference business case (`2026-06-03 CCH Document to SharePoint with Intapp Business Case - Ops Board.md`). It is the only sample, so it may reflect one author's habits as much as a house style. Revise this file when more samples or Board feedback arrive.

Use with the root `CLAUDE.md` (structure, formatting, working rules). This file adds **how it should sound** and **which points to try to cover**.

## Voice and tone (observed in the sample)

- **Firm's own voice.** "The firm", "our", "James Moore"/"JMCO". Never an outside-adviser voice ("we recommend that you").
- **The ask is formal and exact.** "The Operations Board is asked to approve the following:" then numbered decisions.
- **Plain business English for non-technical readers.** Short paragraphs, short declarative sentences, bullets that start with a verb or noun phrase.
- **Define jargon in parentheses at first use.** e.g. "(SharePoint is the Microsoft 365 platform we already own for storing and managing files.)"
- **Interpret every number in a sentence.** After metrics: "This indicates that…", "A 120% retention rate means…". Never leave figures for the reader to decode.
- **Scope the claim honestly with a "not X, but Y" line.** "This is fundamentally a document-system replacement… not a full AI transformation on day one." Upside is "enabled by, not required for" the initial work.
- **Honest hedging on money.** "Conservative ceiling", "somewhere between $50K and $100K", "most likely offset by…", "final terms will be confirmed at contracting". Say what is contingent and what is still being negotiated.
- **Alternatives: strength first, then why not.** "Strong for X. However, Y." Fair, never dismissive.
- **Lead with an overall assessment, then evidence, then interpretation** (vendor financials).
- **Closing line that sums up the direction of travel.** e.g. "from managing documents, to leveraging knowledge, to driving insight and automation."
- **Specifics over adjectives.** Dates with reasons, named owners, hours per week, named champions, concrete deadlines.
- **Calm and confident.** No hype, no superlatives, no fear-mongering. Risk is stated plainly with a mitigation.

**Do not copy the sample's inconsistencies:** it mixes "$50K" and "$50,000", "Nov 1st" and "November 1", and "Document" for "CCH Document". Use whole dollars with commas, "Month D, YYYY", and full product names.

## Points to try to cover (use as many as apply; mark the rest "Not applicable" or `[TBC]`)

**Title block and ask**
- Title, audience, date, named authors with roles.
- Numbered decisions: scope, vendor/partner choice, total investment (one-time plus recurring), go-live date with the reason for that date.

**Executive Summary**
- Where the firm is today, and what this extends ("first time we…").
- The problem in plain terms, then the solution.
- 4–5 benefit bullets, one recommendation sentence.
- How to judge the investment (Day-1 value), and what is deferred to later business cases.

**Why now**
- Readiness: what is already in place that this builds on.
- A "How the pieces fit together" list showing each component's role.
- Governance drivers (retention, offboarding, access, permissions).
- Cost of delay with the current annual cost and any announced increase.

**Financials**
- List vs negotiated price, each discount, the deadline and term length it depends on.
- Fate of the existing contract (not renewed, and when).
- Negotiation status: each item still being pursued, and a statement that current figures are a conservative ceiling.
- Year 1–3 recurring tables, three-year savings vs list, one-time cost ranges, what is included (e.g. training).
- Total Year 1 range; years 2+; excess over current spend and where it is funded from (e.g. innovation budget); offsetting savings.

**Vendor**
- What it is, why the approach cuts cost and complexity, experience and partner credentials.
- Financial position: overall assessment, revenue growth, profitability, cash, customers and retention, each with a plain-English reading.

**Current state**
- Table by team or service line (use, inputs, organisation, automation, what stays outside).
- Current challenges as bold lead-in plus explanation.

**Crawl, Walk, Run**
- Day 1 capabilities (and "AI at Day 1" in its own short list).
- Year 1 outcomes (6–12 months), including AI value.
- Long-term (18–24+ months) vision.

**Governance and delivery**
- Success team with responsibilities, internal IT lead with reserved hours, vendor responsibilities.
- Phased plan: Objective, activities, Outputs per phase; a Day-1 outcomes line at go-live; a Year-1 outcomes line after stabilisation.
- Named champions per team, role-based training, manager adoption KPIs.
- Communication plan: channels plus month-by-month timeline, including post-launch.

**Close-out**
- 4–6 success factors, incl. "adoption, not just technical deployment".
- Six-row risk table (Risk | Description | Impact | Mitigation).
- Evaluation criteria listed first, then alternatives.
- Reference calls with firm names and size where known.
- Appendix tables plus a note on what is still being negotiated.

## Candidate new points for the AI gateway document

Not in the sample. Add them where they fit and mark each `[TBC]` until the research supports it.

- **Current AI usage baseline:** which tools staff use now, how many users, and visibility into it today (ties to `../aiusage/`).
- **Shadow AI and data-leakage risk** as part of the cost of delay.
- **Client-data and confidentiality requirements:** which rules apply, and how each gateway meets them.
- **Data handling:** logging, retention, residency, whether prompts or responses are stored or used for training.
- **Identity and access:** SSO, role-based access, per-team policies.
- **Cost controls:** spend caps, rate limits, caching, per-team usage reporting.
- **Guardrails and policy enforcement:** content filtering, PII redaction, prompt controls.
- **Observability and audit trail:** what the firm can report on to partners or auditors.
- **Provider and model coverage, and lock-in:** how easily the firm can switch models or exit the gateway.
- **Reliability:** uptime commitments, failover, support tiers.
- **Pilot or proof of concept:** a small trial before firm-wide rollout, with success measures.
- **Total cost of ownership:** gateway fees plus AI provider costs plus internal admin time.
- **Acceptable-use policy:** the gateway as a means of enforcing a firm AI policy.
- **Fit with the existing stack:** Microsoft 365, Entra, Purview, Intune and Copilot (confirm what the firm uses).
- **Problems this solves:** a short list of the business problems, placed under Why Now.
- **What gets easier and what gets harder:** a pros-and-cons table, placed after the comparison.
- **Replacement offset:** when a purchase replaces an existing product (e.g. a firewall), show the current product's vendor, annual cost and contract end date, and the net difference.
- **Bundle pricing and terms:** show every option offered, the paid months versus free months, the contract total versus per-year equivalent, and the signature deadline. State derived totals as our calculation.
- **Log allowance and retention:** whether limits are rolling, what happens on overage, and export to firm-owned storage.
- **Caching and credits:** treat savings as an upside to test in a pilot, never a claim; state that caching applies only to traffic through the gateway.
- **Two audiences:** write for the business owner (continuity, adoption, cost) and the technical lead (implementation, cutover, rollback).
- **Vendor marketing:** attribute vendor claims (ROI, case studies) to the vendor or omit.
