# CLAUDE.md — JMCO Business Case Documents

This repo holds project business cases and supporting material for JMCO (James Moore & Co.). Its main purpose is to help draft **new business-case documents** (for the CEO / Operations Board) that follow the same layout, format and persuasion approach as the reference example below.

## Layout

- `docs/` — source material. Reference PDFs and their Markdown conversions.
- `aiusage/` — AI usage material (not covered by this guide).
- `aigateway/` — Project 1: comparing AI gateways for JMCO (leading candidate: Cloudflare AI Gateway, for its enterprise controls). Holds the Word business case and, later, research MD files.
- `tools/` — `make-business-case-docx.js`, the script that generates the Word business-case template (see "Generating the Word document").

## Reference document

`docs/2026-06-03 CCH Document to SharePoint with Intapp Business Case - Ops Board.md` (converted from the PDF of the same name, 15 pages). **Treat it as the template.** Read it before drafting any new business case. Its numbers and names are specific to that project; do not copy them into new documents.

Voice, tone and a fuller checklist of points to cover (including candidate additions for the AI gateway document) are in `docs/steering-business-case.md`. Read it before drafting.

## Standard document structure

Follow this section order. Skip a section only if it truly doesn't apply, and say so.

1. **Title block** — `<Initiative> — JMCO Business Case`; prepared for, date (month + year), prepared by (names and roles).
2. **Request for Approval** — a numbered list of the exact decisions the Board is asked to make: (1) the change/scope, (2) vendor or partner selection, (3) authorization of total investment (one-time + recurring), (4) the go-live date and why that date.
3. **Executive Summary** — where the firm is today, what this initiative extends, the problem in plain terms, the proposed solution, what it enables (bullet list of 4–5 benefits), and a closing recommendation sentence. Define any jargon in parentheses on first use. State how the investment should be judged (Day-1 value) and defer speculative upside to separate future business cases.
4. **Why This Decision Matters Now** — sub-sections: *Infrastructure Readiness*, *Governance and Operational Efficiency*, *Cost of Delay* (quantify the cost of doing nothing).
5. **Financial Considerations** — list vs negotiated pricing, discount conditions and deadlines, negotiation status (what is still being pushed for; treat figures as a conservative ceiling), annual recurring tables (Year 1–3), one-time cost ranges, **Total Year 1 Investment** table, note on years 2+, and how the overspend vs current cost is funded (e.g. innovation budget).
6. **About the Vendor** — what it is, why its approach lowers cost/complexity, experience and partnerships, and a financial position summary (revenue growth, profitability, cash, customer base/retention) with a one-line plain-English interpretation under each metric group.
7. **Current Workflow / Current State** — table by service line or team (primary use, what goes in, organization method, metadata, automation, what stays outside) followed by **Current Challenges** (bold lead-in + explanation).
8. **Crawl, Walk, Run Approach** — (1) Day 1 future state with key capabilities, (2) Year 1 outcomes (6–12 months, where ROI is realised), (3) long-term vision (18–24+ months), explicitly "enabled by, not required for" the initial implementation.
9. **Governance and Implementation Structure** — success team, internal IT (named lead, hours per week reserved), vendor responsibilities.
10. **Implementation Plan** — phased (Foundation & Design → Build/Migration/Validation → Deployment & Training → Go-Live → Post-Go-Live Stabilization). Each phase has **Objective**, key activities, **Outputs**. Include a **Communication & Change Management** plan with channels and a month-by-month timeline.
11. **Key Success Factors** — 4–6 short bullets.
12. **Risk Assessment and Considerations** — table with columns Risk | Description | Impact | Mitigation; typically six risks (adoption, data quality, migration/integration, workflow disruption, go-live execution, governance/sustainability).
13. **Alternative Products Evaluated** — state the evaluation criteria first, then one short paragraph per alternative: its strength, then why it was not chosen.
14. **Reference Calls** — comparable clients contacted.
15. **Appendix** — supporting tables (e.g. support tiers) with a note on open negotiation items.

## How to motivate a project (the persuasion pattern)

- **Lead with the ask.** The Board should know the decisions requested before reading any justification.
- **Build on what's already done.** Frame the project as extending an existing, proven foundation (previous platform, security and governance investments), not as a new bet.
- **Scope the value honestly.** Justify on Day-1, measurable value (replacing an existing system, cost avoided, risk reduced). Treat AI/knowledge upside as future opportunity requiring its own business case.
- **Quantify the cost of delay.** State the current annual cost and any announced increases.
- **Show full costs and the delta.** Give one-time and recurring costs, Year 1 total as a range, the excess over current spend, and where the money comes from.
- **Be transparent about negotiation.** Say what is contingent (deadlines, term length) and what is still being negotiated; label figures as a ceiling.
- **Time the go-live around business reality.** Explain the date choice (e.g. after peak deadlines).
- **Compare alternatives fairly** against stated requirements.
- **Prove credibility.** Vendor financial health, relevant experience, and reference calls with similar firms.
- **Address risk head on.** Every risk gets an impact and a concrete mitigation.
- **Focus on adoption, not just technology.** Champions per team, role-based training, comms plan, adoption metrics.

## Formatting and style conventions

- Markdown with `#` title, `##` for major sections, `###` for sub-sections.
- Tables for pricing, workflow comparison, risks and support tiers. Right-align currency columns. Bold total rows.
- Currency in whole dollars with commas (`$93,330`); ranges as `$161,080 – $197,600`.
- Use **bold lead-ins** in bullets (`**Label:** explanation`).
- Short paragraphs, plain business English written for a non-technical board. Define acronyms and jargon in parentheses on first use.
- Use "the firm" and "James Moore" / "JMCO" consistently. Dates as "Month D, YYYY" or "Month YYYY".
- Name owners and roles specifically (project lead, IT lead, champions per service line).

## Working rules for Claude

- Never invent figures, vendor claims, names, dates or discounts. If information is missing, add a clearly marked `[TBC: ...]` placeholder and list the gaps for the user.
- Don't reuse numbers from the reference document in a new business case.
- Keep source PDFs untouched. Put new Markdown drafts in `docs/` using the naming pattern `YYYY-MM-DD <Project> Business Case - <Audience>.md`.
- When converting a PDF, use `pdftotext -layout`, then rebuild tables by hand and check the page count and totals against the source.
- Before drafting a new document, ask for: the initiative and decisions requested, the audience, current-state cost, proposed cost (one-time and recurring), timeline and go-live constraints, alternatives considered, and team and owners.

## Generating the Word document (.docx)

> The generator now lives at `tools/archive/make-business-case-docx.js.disabled` (retired for the AI gateway document, which the user edits in Word directly). Copy and rename it to `.js` to reuse it for a new document, and never regenerate over a hand-edited .docx.

The Word template `aigateway/AI Gateway Business Case.docx` was built with `tools/make-business-case-docx.js` (docx-js). Reuse and edit that script for new business cases rather than starting over. The script writes to a hardcoded path; change the output path and the content array `c` for each new document.

**How it was built**
1. Read the reference PDF visually first: `pdftoppm -r 60 -png -f 1 -l 4 <pdf> <out>` and view the images. Check fonts with `pdffonts`.
2. Write the generator in the scratchpad dir (not in the project folders), then run it with `node`.
3. `docx` is NOT preinstalled in this environment. Run `npm install docx` in the same directory as the script first, then `node make-business-case-docx.js`.
4. The script is a copy of the one used. Its `require('docx')` resolves from the folder the script is run in, so copy it to a folder where `docx` is installed before running it.

**House format (matches the reference PDF)**
- US Letter (12240 x 15840 DXA), 1" margins (1440 DXA).
- Arial throughout. Body 10pt. Title 24pt bold, colour `1F4E79`. H1 14pt bold `1F4E79`. H2 11pt bold black.
- Title block: two-line title ("<Topic>" / "JMCO Business Case"), then bold "Prepared for", plain "Date" and "Prepared by".
- Tables: full width 9360 DXA, header row fill `1F4E79` with white bold text, alternating body rows `F2F2F2`, thin `BFBFBF` borders, 9pt text. Set `columnWidths` and every cell width in DXA. Use `ShadingType.CLEAR`.
- Lists: real numbering config (bullet `•`, decimal `1.`), indent left 720 / hanging 360. Never type `•` into the text.
- Footer: page number, right-aligned, Cambria 9pt.
- Unknown content is a grey italic `[TBC: ...]` paragraph.

**Environment gotchas**
- Use `python3`, not `python`.
- LibreOffice (`soffice`) is not installed, so a rendered PDF/PNG preview of the docx is not possible; `validate.py` also needs `defusedxml`. Fallback checks: `unzip -tq file.docx` and parse `word/document.xml` with python3 `xml.dom.minidom`. Tell the user the file was not visually checked.
- Bash may fail in auto mode when the permission classifier errors; the user can switch to manual mode.
