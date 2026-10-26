# AI Gateway Project: Decisions and Reasoning

Internal working file (not for the Board). It records **why** we chose what we chose, so the reasoning survives a context compaction. Facts and status live in `CLAUDE.md`; this file holds the logic behind them. Add an entry whenever a decision is made or changed.

Last updated: October 12, 2026.

## 1. Scope and recommendation

**Cloudflare One bundle, with AI Gateway as the headline.**
- *Why:* the firm leans towards Cloudflare for its enterprise controls (governance, DLP, logging, cost controls). The bundle also includes firewall and secure-access services, so it could replace the existing corporate firewall. One purchase would add AI governance and consolidate vendors, which gives the Board a stronger motivator than AI governance alone.
- *Why bundle, not gateway-only:* Cloudflare only prices bundles (Options 1–4). There is no standalone AI Gateway price.
- *Trade-off we accept and state openly:* bundling concentrates more services with one vendor, so switching later is harder. This is in the Alternatives and Risks sections, with mitigations marked `[TBC]`.

**Four pricing options shown, no pick yet.**
- *Why:* the user has not decided between Essentials (1 mbps/seat) and Advantage (2 mbps/seat plus Browser Isolation), or between 13-month and 39-month terms. Options 1 and 2 share a monthly price, and so do 3 and 4; they differ only in term length. The shorter term reduces lock-in but may cost more over time.
- Totals are our own calculation (monthly price × paid months). They are flagged for confirmation with Cloudflare.

## 2. Alternatives (why each was not chosen)

**CData Connect AI Gateway: placed in Alternatives, not "for later".**
- *User's reasoning:* once the firm has Cloudflare AI Gateway plus its firewall and other services, Cloudflare becomes a core part of the ecosystem and the firm cannot easily switch. So suggesting CData as a later add-on is not realistic. Whatever CData does that Cloudflare does not (for example agentic access and CLI tooling) can likely be met with other tools (for example OpenCode) routed through Cloudflare. That claim is unverified: `[TBC]`.
- *Verified:* CData launched the gateway on September 29, 2026 as an **early-access** program, with no general availability date found. That supports the user's maturity concern.
- *Honest note:* CData's strength is enterprise data and MCP access, which the firm uses little today.

**Kong AI Gateway.**
- *User's reasoning:* peers did not like it because it has no web interface for users, and most staff work in the browser.
- *Correction from verification:* Kong has a web management console. The real gap is no employee-facing chat interface; it is an administrator and developer tool. The document says that. The user was unsure whether it is "heavily code-focused": `[TBC]`.

**Kiro.**
- *Why it was in scope:* the user heard it is used at a major bank, so the team looked at what others in financial services use and why.
- *Why not chosen:* it is AWS's spec-driven coding IDE, a developer tool and not a governance gateway. The firm's developers already use Claude and Codex, and agentic use is limited. The firm needs corporate governance.
- *Open point:* whether JMCO is classed as a financial services provider (the user used "FSP" and was unsure). Do not assert it: `[TBC]`.

## 3. Employee web interface

**Cloudflare has no employee chat interface. Two routes are listed:**
1. Existing tools routed through the gateway where technically possible.
2. A corporate-branded web portal, hosted by the firm behind Cloudflare Access, forked from an open-source frontend or built in-house.
- *User's reasoning:* building a decent portal is not daunting and could be done fairly quickly. We still do not state effort or cost in the document: `[TBC]`.
- *Why this matters:* Kong lost partly on this point, so the document must be fair about Cloudflare having the same gap and explain how it is handled.
- *Caveat kept in the document:* ChatGPT Enterprise seats and Microsoft Copilot licences have their own interfaces and may not be routable through the gateway. Day 1 should say which tools can be routed `[TBC]`.

## 4. Caching and token cost

- *User's idea:* caching could stretch AI spend. Users get about 2,000 ChatGPT credits per month and some ask for extras. Perhaps 1,200 through a gateway-fronted tool would give the same value for less.
- *Where it fits:* the firm's own web portal. Its requests go through the gateway, so caching, spend limits and DLP apply. This is the portal that could replace ChatGPT and other web tools.
- *Why it is only an upside to test:* (a) caching helps only when similar requests repeat, and most chat questions are unique, so the hit rate may be modest; (b) replacing per-seat licences with API usage changes the cost model from per seat to per token, so both must be compared; (c) no data yet. The pilot measures it, and no savings figure is claimed.

## 5. Document approach

- **Structure:** follows the single reference business case (the CCH Document to SharePoint with Intapp case, June 2026). See root `CLAUDE.md` and `../docs/steering-business-case.md`. Its numbers and names are not reused.
- **Voice:** the firm's own, plain business English for a non-technical board, parenthetical jargon definitions, a plain-English reading after each set of numbers, honest hedging on money.
- **Two audiences:** the business owner (continuity, adoption, cost) and the technical lead (implementation, firewall cutover, rollback).
- **Vendor marketing:** the Cloudflare case-study claims (227% ROI, $21.4M NPV from a Forrester study) are Cloudflare's. They are attributed or omitted, never presented as JMCO results.
- **Prepared by:** Quinton Viljoen, AI & Innovation Support. His contractor status is private context only and must not appear in any document.
- **Placeholders (user decision):** unknown facts stay as `[TBC: ...]` placeholders, and the placeholder itself is the reminder to update. Do not stop work to chase them. The Draft Notes appendix lists them. This applies to Larry Neal's role, firewall vendor/cost/end date, the 100k log question, the $300k breakdown, ChatGPT credit allocation and the "Interna" vs "Cloudflare One" name.
- **Seats:** about 250 ChatGPT Enterprise seats today (user confirmed), with a few users on other tools. 300 seats gives headroom for AI users, but the same seats cover the firewall and other security services, so they may need to cover all staff. `[TBC]` for total headcount.
- **SASE/consolidation (October 12, 2026):** the user asked for the SASE angle to be added. Cloudflare One is a SASE platform; the document defines SASE in parentheses at first use and says costs "may" fall, because firewall and other tool costs are unknown. It appears in the Executive Summary, Request for Approval, Problems Solved, Cost of Delay, Financials, About the Vendor, Day 1/Year 1 outcomes, risks and an Appendix replacement table. Cloudflare's marketing claims (e.g. no bandwidth charges, 227% ROI) stay out.
- **Logs:** 100k logs may be a rolling or fixed allowance, and the firm may need longer retention, possibly by exporting to firm-owned storage. To ask Cloudflare.

## 6. How the files fit together

- Research MD files in this folder are the source material. Claude copies content into `../tools/make-business-case-docx.js`; the script generates the Word file. The script does not read the MDs itself, and each regeneration overwrites the `.docx` (hand edits in Word are lost unless saved separately).
- Word generation gotchas (docx not preinstalled, no LibreOffice, `python3`) are in root `CLAUDE.md`.

## 7. Things we learned or corrected along the way

- The reference document was prepared by a business-side Project Leader and Project Assistant, with a separate IT lead. It does not mention contractors.
- "CoCounsel" is one word (Thomson Reuters). "Gamma" is a web-based AI presentation/document maker.
- The Cloudflare proposal calls the bundles "Interna Essentials/Advantage"; the case-study deck calls the product "Cloudflare One". Quote the proposal and flag the name.
- The comparison research file is unsourced notes. Its claim of avoiding lock-in applies at the gateway layer only, not to the Cloudflare bundle as a whole.

## 8. Implementation partner (October 12, 2026)

- Presidio, Cloudflare's preferred partner, would assist with setup. A verbal estimate of about $12,000–$14,000 USD was mentioned on a call, with the caveat not to hold them to it. *Reasoning for how it is shown:* it is included as a labelled estimate (not a quote) so the Board sees a realistic one-time cost, and a written quote is flagged as a to-do. The Year 1 subtotal adds it to the subscription range and excludes portal, training and internal time.

## 9. Kong research (October 12, 2026, light web check)

Purpose: fill the Kong column of the Comparison Summary table (the user pastes it into Word by hand; the generator script is retired).
- **Governance:** AI proxy with multi-provider routing, authentication, token-aware rate limiting and analytics, delivered mostly as plugins; some features are Enterprise-only (sources: developer.konghq.com/ai-manager, docs on license tiers).
- **DLP/privacy:** PII sanitization plugin and prompt guards. Kong cites 30+ PII categories in 12 languages; a third party says 20 in 9, so figures are unsettled. Some guardrail plugins need Enterprise.
- **Web interface:** Konnect admin console only; no employee chat interface.
- **Maturity:** Kong's API gateway is long established. Kong AI Gateway went GA with Kong Gateway 3.7 in 2024 (TDWI, May 2024). One source reports AI Gateway 2.2 announced September 30, 2026 (single source).
- **MCP:** AI MCP Proxy plugin (Enterprise, Kong Gateway 3.12+) bridges MCP and APIs, plus an OAuth2 plugin and MCP logging.
- **Consolidation:** an API/AI gateway, not a firewall or SASE product (from general knowledge, not searched).
- **Cost:** Enterprise price not published (custom). Konnect Plus lists about $105 per gateway service per month (sources disagree: $100 per model-month elsewhere). A third-party estimate puts Enterprise at roughly $30,000–$50,000 a year or more; unverified. Kong is priced by services/requests, not seats, and must be hosted (self-managed or Konnect dedicated).
- **Fit with peers' view:** "heavily code-focused" is fair: it is plugin- and configuration-driven, built for platform and API teams.
