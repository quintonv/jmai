# CLAUDE.md — Project 2: AI Licence Programme

Read the root `../CLAUDE.md` first. This file holds what is specific to this project, plus a **progress log** so work survives a context compaction. Update the log whenever something is decided, learned or finished.

## Progress log (last updated: October 26, 2026)

**Done**
- Project folder created. Context, decisions and a draft planning document written (`AI Licence Programme - Planning.md`).
- Portal research file started (`portal-options-research.md`); options listed, vendor claims not yet verified. **Parked: portal is a later phase.**
- Open questions trimmed to framework-phase items only (see "Scope of this phase").
- Agreed with the user what the next document is: a short **framework and plan paper** for approval, not a full business case. Not started, because the AI policy is not yet known.

**Next steps (in order)**
1. TODO: find out whether a firm AI policy exists, who owns it (likely the innovations team, with risk and compliance giving input, unconfirmed) and who reviews it. Level 1 content and the Level 4 acceptable-use statement depend on it. If none exists, add a "create or confirm the policy" step at the start of the plan.
2. Refine level definitions, pass rules and evidence rules with the AI champions.
3. Draft the framework and plan paper. Ask the user first whether it should be the short form or the full house structure with `[TBC]` markers.
4. Draft the question bank (`question-bank.md`) only once levels are agreed.

**Planned content of the framework and plan paper**
- Can write now: the problem (staff want agentic AI, open access risks client data); the earn-not-attend principle; the ask to the Board (approve the framework and plan); the four draft levels; the evidence register and champion assessors; manager approval and signed statement at Level 4; optional renewal suggestion; phasing; risks (box-ticking, champion workload, policy delay, people feeling locked out).
- Cannot write yet: what each level teaches (needs the policy); pass marks and practical rubrics; timeline, cost, headcount.
- Phasing: Phase 1 framework, Phase 2 portal/content/costs, Phase 3 rollout and link Level 4 to the licensing process.

## Purpose

Staff want agentic AI (tools that act on files, run code, call connectors). Giving it to everyone risks data leaking out of the firm. So staff **earn** it: they work through Levels 1–4, and only Level 4 makes a person eligible for agentic rights. At every step the firm must be able to show **why** someone earned a badge and why they were given (or put forward for) a licence. AI champions, who already use AI well, help assess.

## Decisions made (user, October 2026)

- **Earned, not attended.** Each level = complete the training (watch or read it, not a meeting) + a short test + the badge. Higher levels add a practical task. Not a one-off meeting that unlocks everything.
- **Only Level 4 unlocks agentic rights.** Levels 1–3 are non-agentic skill levels. No sandboxed agentic use at Level 3.
- **No usage data or tracking is used to qualify anyone** for any level. Do not propose usage reports, gateway logs or prompt counts as evidence.
- **No separate badge app or vendor platform just for an internal badge.** Badges are shown on a **SharePoint page in the AI Champions section**: a list of people and their badges that anyone can view and display.
- **Delivery portal is undecided and is a later phase.** Options: a SharePoint page, a custom-built hosted web app, or open source. Research is needed to choose. Training, tests and any gamification may live there.
- Evidence must be provable: see the register in the planning document.

## Draft levels (proposals, not agreed)

See `AI Licence Programme - Planning.md`. Working names: 1 Safe Foundations, 2 Effective User, 3 Advanced User, 4 Agent Ready.

## Scope of this phase

Framework and plan only, enough to get approval. Portal, content source (firm-made or external), cost and funding, headcount, which agentic tools Level 4 unlocks, and Microsoft licensing (Power Automate, Entra) are **later phases** and are deliberately not being resolved now.

## Open questions

- [ ] TODO: AI policy owner and status. Likely the innovations team with risk and compliance reviewing or giving input, but unconfirmed. Level 1 training and the Level 4 acceptable-use statement depend on it. Does a written policy exist yet, or does the framework need a step to create one?
- [ ] Agree level definitions, pass rules and evidence rules with the AI champions.
- [ ] Level 4: confirm manager approval and signed acceptable-use statement (assumed yes).
- [ ] Renewal (user leaning: not required, but include as a suggestion): suggest, as an optional item in the plan, a light check-in at the AI champions meeting with a re-test only if the policy or tools change materially or after an incident. No expiry is the alternative. Nothing is tracked.

## Working rules

- Never invent figures, vendor claims or names. Unverified items go in as `[TBC: ...]`.
- Cite source and date for every vendor or feature claim.
- Link to related work: `../aigateway/` (gateway controls could later enforce Level 4 access) and `../aiusage/` (usage reporting; **not** used for qualification here).
