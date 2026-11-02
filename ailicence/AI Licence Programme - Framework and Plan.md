# AI Licence Programme — Framework and Plan

**Prepared for:** `[TBC: Operations Board / CEO]`
**Date:** October 2026 (draft)
**Prepared by:** `[TBC: names and roles]`

*Draft for review. Items marked `[TBC: ...]` are unconfirmed. Evidence tags such as [IRS-1] point to the Basis section and to the separate Research Findings document.*

## Request for Approval

The Operations Board is asked to approve the following:

1. **The framework.** A four-level AI Licence in which staff earn each level by completing training, passing a short test and, at higher levels, completing a practical task reviewed by an AI champion. Only Level 4 makes a person *eligible* for agentic AI rights (AI that can act on files, run code or connect to other systems).
2. **The evidence principle.** For every badge and every Level 4 nomination, the firm can show who earned it, when, on what evidence, and who approved it.
3. **Phase 1 work.** Confirm whether the firm already has an AI policy (and create one if not), and agree the level definitions, pass rules and evidence rules with the AI champions.
4. **Ownership.** Name the programme owner and the AI policy approver: `[TBC: proposed owner is the innovations team, with risk and compliance reviewing]`.
5. **The link to the AI gateway.** Agentic AI is switched on only once the AI gateway (the firm's controlled route for AI traffic) is working. Earning Level 4 makes someone eligible, not enabled.

**Investment requested at this stage:** none for tools or platforms. Phase 1 uses internal time: `[TBC: hours per week for the programme owner and AI champions]`. Portal, content and cost are separate Phase 2 decisions and will come back to the Board with their own business case.

## Summary

Many staff want agentic AI. Used well, it saves time. Used carelessly, it can send client files and confidential data outside the firm. The firm cannot hand it to everyone, and it cannot simply run a one-off meeting that unlocks everything either.

The proposal is to let staff **earn** access. Each level has its own training (watched or read, not just attended), a short test, and a badge. Levels 3 and 4 add a practical task that an AI champion reviews. Level 4 adds manager approval and a signed acceptable-use statement. Every attempt is recorded in a SharePoint register, so the firm can answer "why does this person have access?" at any time.

This is a framework and plan, not a platform purchase. It does not use usage data or tracking to qualify anyone, and it does not need a separate badge application. Badges appear on a SharePoint page in the AI Champions section, where anyone can see who holds what.

External guidance points the same way. The IRS says firms "must deploy internal policies and procedures for compliance with Circular 230 in the AI space", including staff training and documentation [IRS-1]. Florida law requires reasonable measures to protect personal information and prohibits disclosing confidential client information without consent [FL-1, FL-2]. The programme is designed so that its records double as the evidence.

*How to judge this proposal:* by whether it gives the firm a clear, provable route to agentic AI and reduces the chance of a data leak. Cost savings and productivity gains are not claimed here and belong in later business cases.

## Why This Decision Matters Now

### Demand
Staff are asking for agentic AI. Without a clear route, requests get handled one by one, or people use unapproved tools.

### Risk
Agentic tools act on files and connect to other systems. Security guidance names the main risks: instructions hidden in documents that hijack an agent, tools used in ways the user did not intend, and people approving actions without checking them [OWASP-ASI]. Guidance for security teams says agents should have only the permissions a task needs, run in a contained environment, and pass uncertain decisions to a person [SANS-1.4].

### Expectations from regulators and professional bodies
- **IRS (tax practice).** Alert 2026-19, June 24, 2026, applies the existing Circular 230 duties to AI. It says client data should go only into "secure, enterprise-approved AI", firms should vet third-party AI tools, train staff, and document the steps taken [IRS-1]. This applies if the firm has practitioners subject to Circular 230 `[TBC: likely yes; confirm]`.
- **Florida.** A CPA "shall not disclose any confidential information obtained in the course of a professional engagement except with the consent of the client" [FL-1]. Florida's data security law requires "reasonable measures to protect and secure" personal information and sets 30-day breach notice deadlines, with penalties up to $500,000 for late notice [FL-2].
- **Professional guidance.** Neighbouring professions say much the same: firms should set clear policies, train staff on tool limits and secure data handling, and take care before client information enters AI tools [ABA-512, COSO]. Training should be "appropriate to their role and exposure" [COSO].

### Cost of delay
`[TBC: not quantified.]` Without a framework, the firm either blocks agentic AI (and loses the benefit, while staff look for workarounds) or opens it up without proof of readiness. Either is harder to fix after the fact than to design now.

## The Framework

### Four levels
*Names and content are proposals for discussion with the AI champions.*

| Level | Name | What the person can do | Earned by | Unlocks |
|---|---|---|---|---|
| 1 | Safe Foundations | Use approved tools within the firm's AI policy; protect client confidentiality; classify data; check AI output | Training + test | Badge |
| 2 | Effective User | Prompt well; work with files and projects; draft and analyse; check output | Training + test `[TBC: short practical]` | Badge |
| 3 | Advanced User | Build custom assistants and multi-step workflows; teach others; understand what agents are and how they go wrong (without running them) | Training + test + practical reviewed by a champion | Badge |
| 4 | Agent Ready | Use agentic AI safely: permissions, approved data only, connectors, human review, reporting incidents | Training + test + scenario or practical reviewed by a champion + manager approval + signed acceptable-use statement | Badge **and eligibility for agentic rights** |

Levels are taken in order. Only Level 4 leads to agentic rights. There is no agentic use at Levels 1–3.

### How a level is earned
1. **Training.** Watched or read (not just a meeting), with completion recorded.
2. **Test.** A short test with a pass mark `[TBC]`, a randomised question bank and a limit on retakes `[TBC]`.
3. **Practical (Levels 3 and 4).** A task or scenario marked by an AI champion against a written rubric.
4. **Approval (Level 4).** A manager confirms a business need, and the person signs the acceptable-use statement.
5. **Badge.** Shown on the SharePoint badge page in the AI Champions section.

### Proving why someone earned it
Each attempt becomes one row in a SharePoint list, with versioning on and edit rights limited to the programme owners:

| Field | Why it is kept |
|---|---|
| Person, level, date | Who and when |
| Training completed (items, date) | Shows the training was done, not only attended |
| Test version, score, pass or fail | Shows the result |
| Practical submission and rubric result (Levels 3–4) | Shows the skill |
| Champion assessor | Names who judged it |
| Manager approver (Level 4) | Business need and accountability |
| Acceptable-use statement version signed | Policy acknowledgement |
| Decision, expiry | Granted or denied; when it lapses |

A Level 4 nomination for agentic rights cites its register row. *The register goes further than any source we found requires: external guidance asks for training and records, not a test* [IRS-1, ABA-512, COSO].

### What the programme does not do
- It does **not** use usage data, prompt counts or gateway logs to decide who qualifies.
- It does **not** need a separate badge application or platform.
- It does **not** turn on agentic AI by itself. That waits for the AI gateway.

### Roles
- **Programme owner:** `[TBC]`.
- **AI champions:** write and mark practicals, review submissions, help staff. `[TBC: number of champions and hours per week]`.
- **Managers:** approve Level 4 nominations.
- **Risk and compliance:** review the AI policy and the acceptable-use statement `[TBC]`.
- **IT:** gateway controls and the SharePoint register `[TBC]`.

### Renewal (suggestion for discussion)
No expiry is proposed. As an option, the AI champions run a light check-in at their regular meeting, and a re-test is needed only if the policy or tools change materially, or after an incident. Nothing is tracked.

### Developers
The firm has a few small developer teams whose use of coding tools and agents differs from staff working on client files. `[TBC: ask the AI champions whether they need a separate path or different Level 4 content.]`

## What It Could Feel Like

Training should be something people want to do, not a chore. Early ideas, to be developed in Phase 2 (details in `delivery-ideas.md`):
- **Level 1:** spot the confidential data in a sample email; match data types to approved tools; find the invented citation in an AI-written memo.
- **Level 2:** a prompt makeover; fix an AI draft until it is fit to send.
- **Level 3:** build a small assistant for a real task and teach it to a colleague.
- **Level 4:** spot instructions hidden in a document; decide which agent actions to approve; run an incident drill.

Games and exercises are for learning. The test and the champion's review are the gate, and the results are recorded in the register. All examples use invented client data.

## Phasing

### Phase 1: Framework and policy (this request)
**Objective:** agree what the levels mean and what is required to earn them.
- Confirm whether an AI policy exists. If it does, align to it. If not, create one using the draft outline `[TBC: owner and approver]`.
- Agree level definitions, pass rules, practical rubrics and evidence rules with the AI champions, risk and compliance, and IT.
- Confirm Level 4 requirements (manager approval, signed statement) and the developer question.

**Outputs:** approved level definitions; AI policy confirmed or drafted; evidence register design; named owner.

### Phase 2: Portal, content and cost
**Objective:** decide where training and tests live and who writes the content.
- Choose between SharePoint-native, a custom-built app, open source, or a mix (research parked until this phase).
- Decide content: firm-written, curated external resources, or both.
- Build the question bank and rubrics; set up the register and the SharePoint badge page.
- Return to the Board with cost and a timeline: `[TBC]`.

**Outputs:** chosen approach; first content; question bank; register live.

### Phase 3: Rollout
**Objective:** run the programme and connect Level 4 to the licensing process.
- Pilot Levels 1–2 with the AI champions, then add Levels 3–4.
- Link Level 4 to the agentic rights process. **Agentic AI is enabled only once the AI gateway is working** `[TBC: gateway go-live date]`.

**Outputs:** badges awarded; first Level 4 nominations with evidence; agentic access for approved people after gateway go-live.

## Risks

| Risk | Description | Impact | Mitigation |
|---|---|---|---|
| Box-ticking | People click through training without learning | Badges lose meaning | Scenario-based tests, randomised questions, champion-marked practicals at Levels 3–4 |
| Champion workload | Reviewing practicals takes champion time | Delays, burnout, inconsistent marking | Written rubrics; limit practicals to Levels 3–4; `[TBC: hours per week and backup assessors]` |
| Policy delay | The programme depends on the AI policy | Training content cannot be finalised | Make confirming or creating the policy the first step; start level design in parallel |
| People feel locked out | Staff who want agentic AI see a long route | Frustration, workarounds with unapproved tools | Clear steps, visible badge page, fast Level 1–2 start, regular communication |
| Gateway not ready | Level 4 is earned but cannot be used | Eligible staff wait | State plainly that Level 4 means eligible, not enabled; track the gateway project |
| Records are weak | Evidence is incomplete or editable | Cannot prove why access was given | Locked-down register with versioning; one row per attempt; owners only can edit |
| Different needs | Developers and client-facing staff differ | One-size content fits neither | Ask the AI champions; consider a developer track in Phase 2 |

## Assumptions We Need to Confirm

None of these blocks Phase 1, and the wording above allows for either answer.

1. **Does an AI policy already exist, and who owns and approves it?** `[TBC]` If yes, the programme aligns to it. If no, creating it is the first Phase 1 task.
2. **Does the firm have practitioners subject to IRS Circular 230?** Public information suggests yes (tax and IRS representation services). `[TBC: confirm]` If yes, the IRS expectations in the Basis section apply directly.
3. **Does any state or professional rule require a written AI policy?** No Florida Board of Accountancy rule on AI was found in our searches, but the Board's own site has not been checked `[TBC]`.
4. **What do client contracts and engagement letters say about AI, subprocessors and disclosure?** Is IRC § 7216 data involved? Do any clients (for example medical practices) bring health-data rules `[TBC]`?
5. **Does the firm have EU or UK clients, staff or offices?** `[TBC]` See the note below.
6. **Level 4 requirements:** manager approval and a signed acceptable-use statement are assumed `[TBC]`.

## Basis for This Proposal

This proposal draws on the sources below. They were read in October 2026, and each is marked by how it was checked. Full tables, quotations and links are in the separate **Research Findings** document (`AI Licence Programme - Research Findings.md`).

| Tag | Source | What it tells us | How it was checked |
|---|---|---|---|
| IRS-1 | IRS Office of Professional Responsibility, Alert 2026-19 (June 24, 2026) | Firms must deploy AI policies and procedures under Circular 230: training, secure data handling, vendor vetting, documentation; client data only in secure, enterprise-approved AI | Read the original |
| FL-1 | Florida Administrative Code 61H1-23.001 | A CPA may not disclose confidential client information without consent | Read the rule |
| FL-2 | Florida Statutes § 501.171 | Reasonable security measures; breach notice within 30 days; penalties | Read the statute |
| ABA-512 | American Bar Association Formal Opinion 512 (July 29, 2024) | Firms need clear AI use policies; staff training on limits and secure data handling; informed consent before client data goes into self-learning tools. For lawyers, so used as a comparison | Read the original |
| COSO | COSO, *Achieving Effective Internal Control Over Generative AI* (2026) | Acceptable use policy, named tool owners, oversight group, role-based training | Read the original |
| OWASP-ASI | OWASP Top 10 for Agentic Applications 2026 | Ten risks of agentic AI; basis for Level 4 content | Read the original |
| SANS-1.4 | SANS Critical AI Security Guidelines v1.4 (March 2026) | Technical controls: permissions, containment, logging, human escalation | Read the original |
| NIST-600 | NIST AI 600-1, Generative AI Profile (July 2024) | Acceptable use policies; review and incident disclosure | Read the original (governance sections) |
| CPAI | CPAI, *Drafting an AI Policy that Actually Works* | Outline of an accounting-firm AI policy | Read the original |
| BSU | Bridgewater State University, AI Olympians badges (Bronze, Silver, Gold) | A peer example of tiered AI learning for staff; no test or approver | Read the public badge pages |
| ISO-42001 | ISO/IEC 42001:2023 | AI management system standard; not yet obtained | Not yet checked (paid) |
| AICPA | AICPA Code and guidance | No AI-specific standard found; confidentiality rule applies | Read summaries only |

**What we could not confirm:** the ISO 42001 text, the AICPA's members-only policy template, and any Florida Board of Accountancy AI guidance beyond searches. No staff AI policy text was found from the Big Four firms.

**If the firm has clients or staff in the EU, UK or Australia,** the requirements and guidance in the Research Findings document (section C) may also apply. That section is included for reference until the firm's position is confirmed.

*Closing:* the aim is a clear path from using AI safely, to using it well, to using it as an agent, with proof at each step.
