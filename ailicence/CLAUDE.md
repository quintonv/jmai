# CLAUDE.md — Project 2: AI Licence Programme

Read the root `../CLAUDE.md` first. This file holds what is specific to this project, plus a **progress log** so work survives a context compaction. Update the log whenever something is decided, learned or finished.

**To resume:** read this file, then `ai-policy-research.md` (master source list and TODO list in Part 5). The detail behind each source lives in the `source-notes-*.md` files (see "File status"). Skim `AI Licence Programme - Planning.md`, but it is partly out of date.

## Progress log (last updated: October 28, 2026, later)

**Done**
- Project folder, context and decisions recorded (this file). Root `../CLAUDE.md` has the Layout line.
- Draft planning document (`AI Licence Programme - Planning.md`): levels, evidence register, rollout.
- Scope trimmed to framework and plan only. Portal research started (`portal-options-research.md`) but **parked: portal is a later phase**.
- **Policy research complete for the paper.** Every source is marked READ / SECONDARY / NOT ACCESSED. Read in full from primary texts: IRS Alert 2026-19, OWASP Agentic Top 10 2026, SANS Critical AI Security Guidelines v1.4, COSO GenAI guide, ABA Formal Opinion 512, NIST AI 600-1, CPAI guide, Oregon PLF guide, Florida CPA confidentiality rule 61H1-23.001, Florida § 501.171. Detail is in `source-notes-irs-and-jmco.md`, `source-notes-frameworks-and-firms.md` and `source-notes-florida.md`.
- **Decided the next document: a short-form framework and plan paper** (4–5 pages) plus a **separate "Research Findings" Word document** for the full tables, quotes and links. **Both first drafts are now written (October 28, 2026)** along with `delivery-ideas.md`. They are initial drafts for the user to review and hand-edit in Word; do not regenerate over a Word version.

**Key research findings (sources in `ai-policy-research.md` and the source notes)**
- **Whether JMCO already has an AI policy is unconfirmed** (the user does not know). Sources agree a policy needs a named owner, approver, review date, approved-tools list, data classes, human review, role-based training, and incident handling.
- **IRS Alert 2026-19 (June 24, 2026), READ from the official PDF:** "Firms must deploy internal policies and procedures for compliance with Circular 230 in the AI space", covering staff training, secure data handling protocols, vendor vetting and documentation; client data only in "secure, enterprise-approved AI". It is guidance, and it does not say "written policy" in so many words. Applies if JMCO has Circular 230 practitioners (very likely from the website and FICPA listings, but **unconfirmed**).
- **ABA 512 (READ):** firms must "establish clear policies regarding the law firm's permissible use of GAI"; training on GAI basics, tool limits, ethics, secure data handling; informed consent before client information goes into self-learning tools; boilerplate engagement-letter wording not enough. For lawyers, so a comparison only.
- **COSO (READ):** acceptable use policy, named owner per tool, cross-functional oversight committee, and role-appropriate training (Principle 4), which supports having levels.
- **SANS v1.4 (READ, March 2026, eight categories):** the agentic section (scoped permissions, sandboxing, allowlists, human escalation) and the monitoring/logging/access controls match what the Cloudflare AI Gateway project must provide. Source for Level 4 content and the gateway dependency.
- **OWASP Agentic Top 10 (READ):** ASI01–ASI10 confirmed; best source for Level 4 content.
- **Florida (READ):** CPA confidentiality rule 61H1-23.001 (no disclosure without client consent; no AI wording); § 501.171 breach statute makes JMCO a "covered entity" (reasonable security measures; 30-day notice; penalties to $500,000); the Florida AI Bill of Rights failed in 2026; **no Board of Accountancy AI rule found** (searches only; Board site not checked directly).
- **No source requires a knowledge test.** Training plus records is the common expectation; our register exceeds it.
- **No Big Four staff policy text is public** (checked by me and the user; PwC, Deloitte, KPMG dropped as to-dos). EY runs five-level badges but they look developer-focused, so **not** a design comparator.
- **Best peer example: Bridgewater State University "AI Olympians" badges (READ: Bronze Foundational, Silver Intermediate, Gold Advanced; Platinum page 404).** Free, curated course + videos + live session + survey; Silver covers verification, policy and disclosure; Gold covers AI agents and AI coding. No test, assessor, manager approval or evidence register, so our design is stricter. Other university programmes (Minnesota State, NC State, SFSU, FSU, Wake Forest, Hood) are SECONDARY snippets only. EY Gold (5+ hours, no test) and Platinum are specialist badges. See `source-notes-frameworks-and-firms.md`.
- AICPA Small Firm Generative AI Policy Template (April 29, 2026) exists but is members-only; **optional, do not pay**. Free sources cover the same ground.
- Not researched: HIPAA (JMCO advertises medical-practice CPA services), Florida Digital Bill of Rights, other states' breach laws, ISO 42001 text (paid; decision is borrow structure or certify).

**Next steps (in order)**
1. **User reviews and edits the two Word documents by hand** (`AI Licence Programme - Framework and Plan.md`, `AI Licence Programme - Research Findings.md`) and answers the open questions; then revise. Convert to Word only when the user asks (root `CLAUDE.md` rules on `.docx`; never regenerate over a hand-edited file). If a Word version exists later, edit that, not the Markdown.
2. The Planning doc is superseded by the Framework and Plan paper for approval purposes; its stale parts (portal later phase, policy first, gateway dependency) can be fixed or the file archived.
3. User actions (do not block drafting): answer the open questions below; optionally read the remaining items in the manual follow-up table at the top of `source-notes-frameworks-and-firms.md`.
4. Refine level definitions, pass rules and evidence rules with the AI champions. Draft `question-bank.md` only once levels are agreed.

**Paper plan (agreed October 28, 2026; first draft written)**
- Body (4–5 pages, firm's plain business English, names and owners `[TBC]`): 1 Request for Approval; 2 Summary; 3 Why now; 4 The framework (levels, evidence register, assessors, Level 4 gates); 5 Phasing; 6 Risks; 7 **Assumptions we need to confirm** (the open questions, conditionally worded); 8 **Basis for this proposal**, citing evidence by tag (for example [IRS-1]).
- Evidence handled in the paper as a short summary table; the full tables, quotes and links go in the separate Research Findings document, which the paper references. Use plain status words for the Board ("Read the original", "Read a summary", "Not yet checked").
- Appendix content to carry across: A US requirements and guidance (IRS/Circular 230, AICPA, ABA, COSO, CPAI, NIST, OWASP, SANS, Florida, ISO 42001 not yet bought); B EU, UK, Australia, labelled as applying **if JMCO has clients or staff there** (EU AI Act Article 4, UK Generative AI Framework withdrawn February 2025, Australian DTA policy SECONDARY; digital omnibus amendment unconfirmed); C what could not be verified; D mapping of requirements to levels and register fields.
- Can write now: the problem; earn-not-attend; the ask; the four draft levels; the register; champions as assessors; Level 4 manager approval and signed statement; optional renewal suggestion; phasing; risks (box-ticking, champion workload, policy delay, people feeling locked out, developers' different needs).
- Cannot write yet: what each level teaches (needs the policy); pass marks and rubrics; timeline, cost, headcount.
- Phasing: Phase 1 framework (including confirming or creating the policy); Phase 2 portal, content, costs; Phase 3 rollout and link Level 4 to licensing (agentic enabled only when the gateway is live).

## File status

| File | Status |
|---|---|
| `CLAUDE.md` | Current (this file). |
| `ai-policy-research.md` | Current. Master source list (Parts 1–2), design implications, draft policy outline (Part 4), TODO list (Part 5), Word document structure (Part 6). |
| `source-notes-irs-and-jmco.md` | Current. Verbatim IRS Alert 2026-19 extract; JMCO profile from jmco.com (tax services, Florida offices). |
| `source-notes-frameworks-and-firms.md` | Current. Manual follow-up table at the top, then OWASP, SANS v1.4, COSO, AICPA, ABA 512, Big Four, EY badges. |
| `source-notes-florida.md` | Current. Florida CPA rule, § 501.171, failed AI bill, Florida Bar 24-1, and what was not researched. |
| `AI Licence Programme - Planning.md` | **Partly out of date.** Levels and evidence register are the working draft. Portal table and rollout order predate "portal later", "policy first" and the gateway dependency. |
| `portal-options-research.md` | Started, grid empty. Parked until the portal phase. |
| `question-bank.md` | Not created yet. |
| `AI Licence Programme - Framework and Plan.docx` and `AI Licence Programme - Research Findings.docx` | **Word versions created October 28, 2026 from the two Markdown drafts, in the house format. Word is now the master copy: the user edits these by hand. NEVER regenerate over them.** Further changes go in Word (or ask Claude to edit a copy). Not visually checked (no LibreOffice); structure verified (tables, links, no stray Markdown). |
| `AI Licence Programme - Framework and Plan.md` | **First draft written (October 28, 2026); now only the origin of the .docx and no longer updated.** Short form: Request for Approval, Summary, Why Now, Framework, What It Could Feel Like, Phasing, Risks, Assumptions to Confirm, Basis (evidence tags). Names, owners, hours, dates are `[TBC]`. |
| `AI Licence Programme - Research Findings.md` | **First draft written.** Sections A US, B standards, C peer programmes, D EU/UK/Australia (conditional), E design mapping, F draft policy outline, G open items. Evidence tags match the paper. |
| `delivery-ideas.md` | Written. Parked ideas for fun, interactive training per level; developer track; vibe-coding notes. |

## Purpose

Staff want agentic AI (tools that act on files, run code, call connectors). Giving it to everyone risks data leaking out of the firm. So staff **earn** it: they work through Levels 1–4, and only Level 4 makes a person eligible for agentic rights. At every step the firm must be able to show **why** someone earned a badge and why they were given (or put forward for) a licence. AI champions, who already use AI well, help assess.

## Decisions made (user, October 2026)

- **Earned, not attended.** Each level = complete the training (watch or read it, not a meeting) + a short test + the badge. Higher levels add a practical task. Not a one-off meeting that unlocks everything.
- **Only Level 4 unlocks agentic rights.** Levels 1–3 are non-agentic skill levels. No sandboxed agentic use at Level 3.
- **No usage data or tracking is used to qualify anyone** for any level. Do not propose usage reports, gateway logs or prompt counts as evidence. (SANS recommends logging for security; that is separate from qualification.)
- **No separate badge app or vendor platform just for an internal badge.** Badges are shown on a **SharePoint page in the AI Champions section**: a list of people and their badges that anyone can view and display.
- **Delivery portal is undecided and is a later phase.** Options: a SharePoint page, a custom-built hosted web app, or open source.
- Evidence must be provable: see the register in the planning document.
- **Agentic access is a reward, but switched on only once the Cloudflare AI Gateway is working correctly** (October 26, 2026). Earning Level 4 makes someone eligible; actual enablement waits on the gateway (`../aigateway/`). The plan should say so.
- **AI policy status is unknown** (October 28, 2026). Do not state that no policy exists. Plan wording: "confirm whether an AI policy exists; if not, create one".
- **Proceed without the open answers** (October 28, 2026). Word the paper conditionally: policy "if it exists, align; if not, create"; Circular 230 applicability "to be confirmed" (strong public evidence for yes); EU/UK section "applies if the firm has such clients"; owner and approver `[TBC]`. Put an "Assumptions we need to confirm" box near the top.
- **Short form chosen; research findings in a separate Word document** (October 28, 2026). Names and owners in the paper stay `[TBC]`.
- **JMCO is in the USA (Florida offices). Keep US sources separate from EU, UK and Australian ones** (October 26, 2026). US material is the core evidence. **Updated October 27, 2026:** JMCO may have EU or UK clients, so the document must say the non-US section (EU, UK, Australia) **could apply to such clients, if the firm has any**. Do not explain *why* the sections are separated; just label it and keep it clearly apart from the US evidence.
- Research must show where each finding came from and whether it is verified, because the user builds a Word document from it.
- **Developers:** JMCO has a few small dev teams. EY's developer-oriented badges are not a comparator for the general levels, but may be noted in the Research Findings document as an example for a possible developer track (unverified).

## Draft levels (proposals, not agreed)

See `AI Licence Programme - Planning.md`. Working names: 1 Safe Foundations, 2 Effective User, 3 Advanced User, 4 Agent Ready.

## Scope of this phase

Framework and plan only, enough to get approval. Portal, content source (firm-made or external), cost and funding, headcount, which agentic tools Level 4 unlocks, and Microsoft licensing (Power Automate, Entra) are **later phases** and are deliberately not being resolved now.

## Open questions (none block drafting)

- [ ] Does a written AI policy already exist? Who owns and approves it? (Likely the innovations team with risk and compliance, unconfirmed.) Check with compliance, risk and the AI champions.
- [ ] **Does JMCO have tax practitioners under Circular 230**, and who has principal authority under § 10.36? Website and FICPA listings suggest yes. See `source-notes-irs-and-jmco.md`.
- [ ] Does any state or professional rule require a written AI policy? (No Florida Board of Accountancy AI rule found; check the Board's site and FICPA.)
- [ ] Do client contracts or engagement letters cover AI, subprocessors or disclosure? Is § 7216 data in scope? Does HIPAA apply to medical-practice clients?
- [ ] Does JMCO have any EU or UK clients, staff or offices? (Unknown; the paper says "if".)
- [ ] Agree level definitions, pass rules and evidence rules with the AI champions.
- [ ] Developers: do the few dev teams need a separate path or different Level 4 content (coding tools, running code)? Ask the AI champions. Possible reference for a developer track: EY's domain badge families (AI Engineering, Applied AI, Cybersecurity AI); see `source-notes-frameworks-and-firms.md`. Mention in the Research Findings document, marked unverified.
- [ ] Level 4: confirm manager approval and signed acceptable-use statement (assumed yes).
- [ ] Renewal (user leaning: not required, but include as a suggestion): optional light check-in at the AI champions meeting with a re-test only if the policy or tools change materially or after an incident. No expiry is the alternative. Nothing is tracked.
- [ ] ISO 42001: decide whether the firm borrows the structure or aims for certification before buying the standard.

## Working rules

- Never invent figures, vendor claims or names. Unverified items go in as `[TBC: ...]`.
- Cite source and date for every vendor, standard or feature claim, and mark it READ / SECONDARY / NOT ACCESSED as in the research file.
- Link to related work: `../aigateway/` (gateway controls could later enforce Level 4 access; its `CLAUDE.md` has a note to review this project's research) and `../aiusage/` (usage reporting; **not** used for qualification here).
- WebFetch gotchas: iso.org, pwc.com, americanbar.org, floridabar.org and aicpa-cima.com return 403 to automated fetches; the Internet Archive (`web.archive.org/web/2025/<url>`) often serves a readable copy; PDFs can be saved and read with `pdftotext`; secondary summaries are often wrong on details (section numbers, versions), so check before quoting. Credly pages returned 404.
