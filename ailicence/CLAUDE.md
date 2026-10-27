# CLAUDE.md — Project 2: AI Licence Programme

Read the root `../CLAUDE.md` first. This file holds what is specific to this project, plus a **progress log** so work survives a context compaction. Update the log whenever something is decided, learned or finished.

**To resume:** read this file, then `ai-policy-research.md` (the main research, with the TODO list in Part 5). Skim `AI Licence Programme - Planning.md` but see "File status" below, because it is partly out of date.

## Progress log (last updated: October 26, 2026)

**Done**
- Project folder created; context and decisions recorded (this file).
- Draft planning document written (`AI Licence Programme - Planning.md`): levels, evidence register, rollout.
- Portal research file started (`portal-options-research.md`); grid is empty (`[TBC]`). **Parked: portal is a later phase.**
- Scope for this phase trimmed to framework and plan only (see "Scope of this phase").
- Agreed the next document: a short **framework and plan paper** for approval, not a full business case. **Not started**, because the AI policy does not exist yet.
- **Policy research done** (`ai-policy-research.md`), by web search plus reading pages and PDFs directly. Every source is marked READ / SECONDARY / NOT ACCESSED. Part 1 is US and general frameworks (the core evidence); Part 2 is an EU/UK/Australia reference list kept separate. Part 3 design implications, Part 4 draft policy outline for JMCO (11 sections), Part 5 manual verification TODO list, Part 6 suggested structure for the Word document.
- Not accessed automatically (need a manual read): ISO/IEC 42001 (paid), PwC pages (403), OWASP agentic PDF (descriptions), SANS guidelines, the original IRS OPR Alert 2026-19, the AICPA Code text, ABA 512, COSO.

**Key research findings (details and sources in `ai-policy-research.md`)**
- No AI policy exists at JMCO. Sources agree a policy needs a named owner, approver, review date, approved-tools list, data classes, human review, training, and incident handling.
- US: IRS OPR Alert 2026-19 (June 24, 2026) is read by commentators as requiring firm procedures (training, secure data handling, vendor vetting, documentation) under Circular 230 § 10.36. That is a reading, not explicit wording, and applies only if JMCO has tax practitioners. No AI-specific AICPA standard exists.
- No source requires a knowledge test; training plus records is the common expectation. Our register exceeds it.
- No big player publishes a multi-level AI badge framework, and no Big Four staff policy text was found.
- OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) is the best source for Level 4 content.

**Next steps (in order)**
1. Work the TODO list in `ai-policy-research.md` Part 5 (the user may do the manual reads). Priority: confirm whether Circular 230 or any state/professional rule requires a written AI policy; confirm policy owner and approver.
2. Add "create or confirm the AI policy" as step one of the plan; use the outline in research Part 4.
3. Refine level definitions, pass rules and evidence rules with the AI champions.
4. Draft the framework and plan paper. Ask the user first whether it should be the short form or the full house structure with `[TBC]` markers.
5. Eventually: a Word document of the research findings (see research Part 6). The user will edit Word by hand; follow the root `CLAUDE.md` rules on `.docx` (do not regenerate over a hand-edited file).
6. Draft the question bank (`question-bank.md`) only once levels are agreed.

**Planned content of the framework and plan paper**
- Can write now: the problem (staff want agentic AI, open access risks client data); the earn-not-attend principle; the ask to the Board (approve the framework and plan); the four draft levels; the evidence register and champion assessors; manager approval and signed statement at Level 4; optional renewal suggestion; phasing; risks (box-ticking, champion workload, policy delay, people feeling locked out).
- Cannot write yet: what each level teaches (needs the policy); pass marks and practical rubrics; timeline, cost, headcount.
- Phasing: Phase 1 framework (including the policy), Phase 2 portal/content/costs, Phase 3 rollout and link Level 4 to the licensing process (agentic enabled only when the gateway is live).

## File status

| File | Status |
|---|---|
| `CLAUDE.md` | Current (this file). |
| `ai-policy-research.md` | Current, main research and TODO list. |
| `AI Licence Programme - Planning.md` | **Partly out of date.** Levels and evidence register are still the working draft. Its portal-options table and rollout order predate the "portal is a later phase" and "policy first" decisions, and it does not yet mention the gateway dependency. Update it when drafting the framework paper. |
| `portal-options-research.md` | Started, grid empty. Parked until the portal phase. |
| `question-bank.md` | Not created yet. |

## Purpose

Staff want agentic AI (tools that act on files, run code, call connectors). Giving it to everyone risks data leaking out of the firm. So staff **earn** it: they work through Levels 1–4, and only Level 4 makes a person eligible for agentic rights. At every step the firm must be able to show **why** someone earned a badge and why they were given (or put forward for) a licence. AI champions, who already use AI well, help assess.

## Decisions made (user, October 2026)

- **Earned, not attended.** Each level = complete the training (watch or read it, not a meeting) + a short test + the badge. Higher levels add a practical task. Not a one-off meeting that unlocks everything.
- **Only Level 4 unlocks agentic rights.** Levels 1–3 are non-agentic skill levels. No sandboxed agentic use at Level 3.
- **No usage data or tracking is used to qualify anyone** for any level. Do not propose usage reports, gateway logs or prompt counts as evidence.
- **No separate badge app or vendor platform just for an internal badge.** Badges are shown on a **SharePoint page in the AI Champions section**: a list of people and their badges that anyone can view and display.
- **Delivery portal is undecided and is a later phase.** Options: a SharePoint page, a custom-built hosted web app, or open source. Research is needed to choose. Training, tests and any gamification may live there.
- Evidence must be provable: see the register in the planning document.
- **Agentic access is a reward, but switched on only once the Cloudflare AI Gateway is working correctly** (user, October 26, 2026). Earning Level 4 makes someone eligible; actual enablement waits on the gateway (`../aigateway/`). The plan should say so.
- **No AI policy exists yet** (user, October 26, 2026).
- **JMCO is in the USA. Keep US sources separate from EU, UK and Australian ones** (user, October 26, 2026). US material is the core evidence; the non-US list is optional reference or an appendix. **Internal instruction only: do not mention the reason or this separation in any firm document.** Present the non-US items without commentary.
- Research should list where each finding came from and whether it is verified, because the user will build a Word document from it and do manual checks.

## Draft levels (proposals, not agreed)

See `AI Licence Programme - Planning.md`. Working names: 1 Safe Foundations, 2 Effective User, 3 Advanced User, 4 Agent Ready.

## Scope of this phase

Framework and plan only, enough to get approval. Portal, content source (firm-made or external), cost and funding, headcount, which agentic tools Level 4 unlocks, and Microsoft licensing (Power Automate, Entra) are **later phases** and are deliberately not being resolved now.

## Open questions

- [ ] AI policy owner and status. Likely the innovations team with risk and compliance reviewing or giving input, but unconfirmed. There is no written policy, so the plan needs a step to create one. Who approves it?
- [ ] Does Circular 230 or any state/professional rule require a written AI policy at JMCO? (compliance)
- [ ] Do client contracts or engagement letters cover AI, subprocessors or disclosure? Is § 7216 data in scope?
- [ ] Does JMCO have any EU or UK clients, staff or offices? (decides whether the non-US list matters)
- [ ] Agree level definitions, pass rules and evidence rules with the AI champions.
- [ ] Level 4: confirm manager approval and signed acceptable-use statement (assumed yes).
- [ ] Renewal (user leaning: not required, but include as a suggestion): suggest, as an optional item in the plan, a light check-in at the AI champions meeting with a re-test only if the policy or tools change materially or after an incident. No expiry is the alternative. Nothing is tracked.

## Working rules

- Never invent figures, vendor claims or names. Unverified items go in as `[TBC: ...]`.
- Cite source and date for every vendor, standard or feature claim, and mark it READ / SECONDARY / NOT ACCESSED as in the research file.
- Link to related work: `../aigateway/` (gateway controls could later enforce Level 4 access) and `../aiusage/` (usage reporting; **not** used for qualification here).
- WebFetch gotchas seen: iso.org, pwc.com and some PDFs return 403 or HTML; PDFs can be saved by WebFetch and read with `pdftotext`. Secondary summaries are often wrong on details (section numbers, versions), so check before quoting.
