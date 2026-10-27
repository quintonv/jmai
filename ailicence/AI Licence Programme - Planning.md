# AI Licence Programme — Planning Document

Working draft, October 26, 2026. Internal, not yet for the Board. Level names and content are proposals for discussion with the AI champions.

> **Out of date in places (see `CLAUDE.md`).** Since this was written: the portal is a later phase (section 5 is parked); there is no AI policy yet, so the rollout must start with creating or confirming one (research: `ai-policy-research.md`); and agentic access is enabled only once the Cloudflare AI Gateway is working, so Level 4 means "eligible", not "enabled". Levels and the evidence register (sections 2–4) are still the working draft.

## 1. Why

Many staff want agentic AI (AI that can act on files, run code or connect to other systems). Giving it to everyone could leak files and client data. The firm wants staff to **earn** it, and to be able to **prove** afterwards why each person was given access.

## 2. How it works

For each level, the person:

1. Completes the training for that level (watch or read; tracked as completed).
2. Takes a short test and passes.
3. Where required, completes a practical task that an AI champion reviews.
4. Earns the badge, which appears on the AI Champions SharePoint page.

Levels are taken in order. **Only Level 4 makes a person eligible for agentic rights.** No usage data or tracking is used to decide who qualifies.

## 3. Proposed levels

| Level | Name | Focus | Earned by | Unlocks |
|---|---|---|---|---|
| 1 | Safe Foundations | Approved tools, firm AI policy, client confidentiality, data classification, checking AI output | Training + test | Badge |
| 2 | Effective User | Prompting, working with files and projects, drafting and analysis | Training + test (+ short practical `[TBC]`) | Badge |
| 3 | Advanced User | Custom assistants, multi-step workflows, teaching others; knows what agents are and their risks (prompt injection, data leaving the firm) but does not run them | Training + test + practical reviewed by a champion | Badge |
| 4 | Agent Ready | Safe agentic use: permissions, approved data only, connectors, human review, reporting incidents | Training + test + scenario/practical reviewed by a champion + manager approval + signed acceptable-use statement | Badge **and eligibility for agentic rights** |

Open design points: pass marks, retake limits, whether Level 2 needs a practical, expiry/renewal by re-test `[TBC]`.

## 4. Proving why someone earned a level

One **register** row per attempt, kept in a SharePoint list with versioning on and edit rights limited to the programme owners:

| Field | Purpose |
|---|---|
| Person, level, date | Who and when |
| Training completed (items, date) | Shows the training was done, not just attended |
| Test version, score, pass/fail | Shows the test result |
| Practical submission and rubric result | Shows the skill (Levels 3–4) |
| Champion assessor | Names who judged it |
| Manager approver (Level 4) | Business need and accountability |
| Acceptable-use statement version signed | Policy acknowledgement |
| Decision, expiry | Granted or denied; when it lapses |

The AI Champions badge page reads from this list. A licence nomination cites the Level 4 row.

## 5. Portal options (to be researched)

| Option | Idea | Likely strengths | Likely concerns |
|---|---|---|---|
| A. SharePoint-native | SharePoint page + list + Microsoft Forms quizzes + Power Automate approvals | No new vendor; stays in the firm's tenant; easy badge display | Quizzes basic; gamification is DIY; licensing `[TBC]` |
| B. Custom web app | Firm-hosted app (possibly behind Cloudflare Access) | Best interactivity and gamification; tailored scenarios | Build and upkeep effort `[TBC]` |
| C. Open source | e.g. Moodle, Open edX, Frappe LMS; H5P for interactive content; Open Badges standard | No licence fee; badges and quizzes built in | Hosting and admin; sign-in integration `[TBC]` |
| D. Hybrid | SharePoint badge board, with training and tests in whichever tool wins | Keeps the badge page simple | Two places to maintain |

Details and sources go in `portal-options-research.md`.

## 6. Rollout (high level)

1. Agree levels, policy link and evidence rules with the AI champions, ITS and risk/compliance.
2. Choose the portal approach from the research; pilot Levels 1–2 with the champions.
3. Add Levels 3–4, assessor rubrics and the manager approval step.
4. Publish the badge page; link Level 4 to the agentic licence process (and, later, gateway controls from the AI Gateway project).

## 7. Gaps

See "Open questions" in `CLAUDE.md`.
