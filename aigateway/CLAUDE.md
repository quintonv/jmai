# CLAUDE.md — Project 1: AI Gateway Selection

Read the root `../CLAUDE.md` first (structure, persuasion pattern, formatting, working rules) and `../docs/steering-business-case.md` (voice, tone, points to cover). This file holds what is specific to this project, plus a **progress log** so work survives a context compaction. Update the log whenever something is decided, learned or finished.

## Progress log (last updated: October 12, 2026)

**Done**
- Reference PDF converted to Markdown (`../docs/`); root `CLAUDE.md`, `../docs/steering-business-case.md` and this file created.
- Word template built by `../tools/make-business-case-docx.js` (docx-js). See root `CLAUDE.md` "Generating the Word document".
- Research files moved into this folder: `cloudflare_vs_cdata_ai_platform_comparison.md`, `Cloudflare_One_Proposal_JamesMoore.md`, `Cloudflare_Case_Studies_JamesMoore.md`.
- Light web verification of Kong, Kiro, CData and the AI tools in use (see "Verified findings").
- Plan approved (`/root/.claude/plans/memoized-enchanting-wilkinson.md`, session-local).

- First content pass of the Word document done (October 12, 2026): `../tools/make-business-case-docx.js` rewritten and `AI Gateway Business Case.docx` regenerated. It now has the four Cloudflare options with derived totals, firewall-offset table (TBC), Current State tool table (TBC), evaluation criteria, alternatives (CData, Kong, Kiro), comparison table, easier/harder table, eight-row risk table, people, sources, and a Draft Notes appendix listing open items. Checked with `unzip -tq`, XML parse and total lookups; not visually checked.
- New points added to `../docs/steering-business-case.md`.
- SASE/consolidation story added throughout the Word document (October 12, 2026): Executive Summary (SASE defined in parentheses), Request for Approval, Problems Solved, Cost of Delay, Security Consolidation Offset table, Year 1 total, About the Vendor, Day 1 and Year 1 outcomes, renamed continuity risk, and an Appendix table of Cloudflare components vs tools they could replace (all `[TBC]`).

**Still to do**
- Resolve the open questions below with the user and replace the matching `[TBC]` markers in the document.
- Regenerate after each change: `npm install docx` in the scratchpad if `node_modules` is missing, copy `../tools/make-business-case-docx.js` there as `mk.js`, run `node mk.js`.
- Decide the recommended Cloudflare option and fill Financials; add Year 2–3 view once firewall and subscription savings are known.
- Fold in further research MD files as the user adds them.
- Visual check of the .docx is not possible (LibreOffice not installed).

**Reasoning behind the decisions is in `decisions-and-reasoning.md` (this folder). Read it after this file, and add to it whenever a decision is made or changed.**

## How the Word document is produced

> **Script retired (October 12, 2026):** the user has edited the Word document directly, so Word is now the master copy. The generator was moved to `tools/archive/make-business-case-docx.js.disabled` so it cannot be run by accident. Do not regenerate `AI Gateway Business Case.docx`; any future content change is made in Word (or on a copy). To reuse the script for a new document, copy it out of `archive/`, rename it to `.js`, and change its output path first.


- Source material is the research MD files in this folder. Claude reads them and writes the content into the content array of `../tools/make-business-case-docx.js`. The script then generates `AI Gateway Business Case.docx`. The script does **not** read the MD files itself, so a changed MD only reaches the Word file after Claude updates the script and regenerates.
- Each regeneration overwrites the `.docx`. Hand edits made in Word are lost unless the user saves a copy first or says so, in which case use the edited file as the base. Once content is final, Word becomes the master and the script should not be run again. Idea offered, not yet decided: write dated file names so earlier versions are kept.
- User preference: keep answers brief when asked to.

## Project summary

- Compare AI gateways to decide which one JMCO (James Moore & Co., jmco.com) will use.
- **Recommendation direction: the Cloudflare One bundle (AI Gateway included).** It governs AI use and also brings firewall/SASE services that could replace the existing corporate firewall, consolidating vendors. Treat favourable claims as unverified until the research supports them.

## People

- **Prepared by:** Quinton Viljoen, AI & Innovation Support (Innovation Team). Contractor: private context only, never mention it in documents.
- **Business owner / sponsor:** Lucia Valenzuela, Chief Innovation Officer. Not technical; cares about business users carrying on day to day after Cloudflare and the gateway go live. Cloudflare's proposal is addressed to her.
- **Technical lead:** Larry Neal, Senior ITS Manager. Infrastructure lead, owns the firewall side, leads the Cloudflare conversations. User said "likely": `[TBC: confirm his role on this project]`.
- Write for both: Lucia (continuity, adoption, cost) and Larry (technical implementation, cutover, firewall, rollback).
- Audience: CEO & Operations Board. Voice: the firm's own.

## Decisions made

- **Scope:** Cloudflare One bundle. AI governance is the headline; firewall/SASE replacement is part of the same purchase and offsets the current firewall cost.
- **Pricing:** present all four Cloudflare options; no recommended option yet.
- **Employee web UI:** list two routes: (1) existing tools routed through the gateway where technically possible, (2) a corporate-branded web portal behind Cloudflare Access, forked from an open-source frontend or custom-built. User believes this is quick and not daunting; do not state effort or cost: `[TBC: build effort]`.
- **CData:** goes in Alternatives (what was tried and why not). User does not want it pitched "for later": choosing Cloudflare's bundle makes switching later hard, and agentic needs can likely be met with other tools (e.g. OpenCode) routed through Cloudflare (`[TBC]`, unverified).
- **Placeholder policy (user decision):** unknown facts (Larry's role, firewall vendor/cost/end date, log allowance, $300k breakdown, ChatGPT credits, product name) stay as `[TBC: ...]` placeholders in the document. The placeholder is the reminder to update; no need to block on them. They are listed in the Draft Notes appendix.
- **Kiro scope reason:** heard it was used at a major bank, so reviewed to see what other financial-services organizations use and why. `[TBC: confirm source and whether JMCO is classed as a financial services provider]`.
- **Caching belongs to the firm's own web portal** (a portal that could replace ChatGPT and other web tools): its requests go through the gateway, so caching, limits and DLP apply. Caveats kept in the document: hit rate depends on repeated requests; moving from per-seat to usage-based pricing changes the cost model; measure in a pilot.
- **Caching:** present as an upside to test in a pilot, never a savings claim. Caveat to state honestly: caching only applies to requests that pass through the gateway via API. ChatGPT Enterprise seats and Copilot licences use their own interfaces/credits. User's idea: users get ~2,000 ChatGPT credits per month and some request extra; maybe 1,200 could give the same value through a gateway-fronted tool (`[TBC]`).
- **Breakdown of the ~$300k spend:** needed. Current State table with `[TBC]` cells (tool, purpose, users, annual cost). Usage counts (not costs) may be seeded from `../aiusage/`.
- **Pros and cons:** include a "problems this solves" section and a "what gets easier / harder" table.

## Facts

**Current AI use:** about $300,000 USD a year across ChatGPT Enterprise, Microsoft Copilot, Gamma, CoCounsel (Thomson Reuters) and some Claude. About 250 ChatGPT Enterprise seats (user confirmed), with a few users on other tools. Developers already use Claude and Codex; agentic use is limited. `[TBC: source and breakdown]`.

**Cloudflare proposal (dated October 7, 2026, prepared by a Cloudflare account contact for Lucia Valenzuela).** Pricing holds only with signature by 11/25.

| Option | Bundle | Term | Monthly | Paid months | Contract total | Per year |
|---|---|---|---:|---:|---:|---:|
| 1 | Essentials + AI Gateway | 13 months (1 free) | $4,600 | 12 | $55,200 | $55,200 |
| 2 | Essentials + AI Gateway | 39 months (3 free) | $4,600 | 36 | $165,600 | $55,200 |
| 3 | Advantage + AI Gateway | 13 months (1 free) | $6,031 | 12 | $72,372 | $72,372 |
| 4 | Advantage + AI Gateway | 39 months (3 free) | $6,031 | 36 | $217,116 | $72,372 |

(Totals are derived by us: monthly price × paid months. `[TBC: confirm with Cloudflare]`.) Inputs for all: AI Gateway 100k logs; Access (ZTNA), Gateway (SWG), DLP and CASB at 300 seats; Premium Success included. Essentials has 1 mbps/seat network security; Advantage has 2 mbps/seat plus Browser Isolation (300 seats). The proposal calls the bundles "Interna Essentials/Advantage"; the case-study deck calls the product "Cloudflare One". Quote the proposal and flag the name.

**Implementation partner:** Presidio (user's spelling; `[TBC: confirm legal name]`), Cloudflare's preferred partner for onboarding. On a call, the contact mentioned roughly $12,000–$14,000 USD to implement (user unsure which), but said not to hold them to it. Treat as a verbal, non-binding estimate; the document says so and asks for a written quote.

**Vendor marketing:** the case-study deck's claims (e.g. 227% ROI, $21.4M NPV, Forrester study) are Cloudflare's. Attribute them or omit; never present as JMCO results.

## Verified findings (web check, October 2026; mark sources in the document appendix)

- **Kong AI Gateway:** has a web management console (Konnect AI Gateway editor and dashboards), so "no web UI" is wrong. The real gap is no employee-facing chat interface; it is an administrator and developer tool built on plugins and declarative config. Source: developer.konghq.com/ai-manager.
- **Kiro:** AWS's spec-driven agentic coding IDE (built on Code OSS), a developer tool, not an AI gateway. Availability described as preview in sources. "Very good for banks" is unverified. Sources: smile.eu, yourstory.com.
- **CData Connect AI Gateway:** launched September 29, 2026 as an early-access program; no general availability date found. This supports the maturity argument. Source: cdata.com press release.
- **Gamma:** web-based AI presentation/document maker.
- **CoCounsel:** one word; Thomson Reuters' AI assistant; agentic version for tax, audit and accounting launched June 2025.

## Open questions (move answers up when resolved)

**Firm facts**
- [ ] Current firewall: vendor, annual cost, contract end date (a key motivator: one product replaces one and adds AI governance).
- [ ] Is 100k AI Gateway logs enough? Is it rolling? Can logs be exported to firm-owned storage? What is the firm's retention requirement?
- [ ] Breakdown of the ~$300k by tool; who pays; renewal dates; which subscriptions could be reduced.
- [ ] Seat count: the 300 seats cover the security services too, so they may need to cover **all staff** if the firewall is replaced, not just the ~250 ChatGPT users. Confirm total headcount.
- [ ] Other tools the Cloudflare One bundle could replace (VPN, web filter, remote access) and their costs.
- [ ] ChatGPT credit allocation (~2,000/user/month?) and how often extra credits are requested.
- [ ] Compliance and client-confidentiality obligations; identity platform (assumed Microsoft Entra).
- [ ] Which current tools can actually be pointed at the gateway.

**Project**
- [ ] Larry Neal's role on this project; ITS hours per week; any named champions.
- [ ] Written quote and scope from Presidio (verbal estimate only); portal build and training costs; internal ITS time.
- [ ] Funding source (e.g. innovation budget), go-live date and timing constraints.
- [ ] What "Premium Success" covers; confirm the "Interna" vs "Cloudflare One" name.
- [ ] Reference calls (Cloudflare customers of similar size/sector).
- [ ] Why Kiro was in scope; peers' view on Kong; confirm CData notes and the agentic workaround.

**Tone and sharing**
- [ ] Is the Board expecting the same length and formality as the reference (15 pages)? Anything that must not appear?

## Evidence rules for research files

- Cite a source and date for every vendor fact, price and feature claim.
- Separate verified facts from vendor marketing claims.
- Anything unverified goes in as `[TBC: ...]` and into the gap list for the user.
- Apply the agreed criteria to every gateway the same way, including the leading candidate.
