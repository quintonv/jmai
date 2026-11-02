# AI Policy Research

Researched October 26–28, 2026 (web search plus reading pages and PDFs directly). **Detail for each source is in `source-notes-irs-and-jmco.md`, `source-notes-frameworks-and-firms.md` and `source-notes-florida.md`; this file is the master list and status.** Context: whether JMCO already has an AI policy is unconfirmed (to be checked). Level 1 training and the Level 4 acceptable-use statement depend on one. This file is the source list for the eventual Word document: what exists, where, what we read ourselves, and what still needs checking.

**Layout:** Part 1 is the core evidence base (US regulators, US professional bodies, US standards, and general frameworks). Part 2 is a separate reference list (EU, UK, Australia) for an appendix; the document should say it could apply to EU/UK clients if the firm has any. Part 3 onward applies to both.

**Verification key**
- **READ**: the primary source (or the official page) was opened and read in this session.
- **SECONDARY**: only seen through commentary (law-firm blogs, vendors, news). Treat as a lead, not a fact.
- **NOT ACCESSED**: source exists but could not be opened (paywall, bot block, 403). Needs a manual check.

---

# Part 1. US and general frameworks (core evidence)

## 1A. US regulators and professional bodies

| # | Source | Key content for JMCO | Status |
|---|---|---|---|
| U1 | **IRS Office of Professional Responsibility, Alert 2026-19**, "Introductory Guidelines for Responsible AI Use in Federal Tax Practice" (June 24, 2026). [Official PDF](https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf); also the [IRS govdelivery bulletin](https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70?reqfrom=share) | Cites §§ 10.22, 10.27(a), 10.35, 10.36, 10.37, 10.51(a)(15) and IRC §§ 6713, 7216(a). On § 10.36 it quotes the rule ("must take reasonable steps to ensure that the firm has adequate procedures in effect") and then says verbatim: "Firms must deploy internal policies and procedures for compliance with Circular 230 in the AI space", covering staff (comprehensive training on AI risks and requirements), internal rules (protocols for secure data handling, AI accuracy monitoring), and external providers ("Outsourced or third-party AI tools should be vetted"), "And all steps and processes documented to show adherence to section 10.36." Taxpayer data: practitioners "must strictly handle all client data using only secure, enterprise-approved AI". Disclosure to clients: "should", not "must". Best-practice recap: document AI usage and verification, breach/error procedures, staff training, vet vendors, never upload sensitive data to unsecured sites, treat AI text as drafts. Alert is guidance, not a new rule. | **READ** (official IRS PDF, text extracted and checked October 27, 2026). Applies if JMCO has practitioners under Circular 230: likely yes (website, FICPA listings) but **confirm internally**. Full extract and JMCO profile: `source-notes-irs-and-jmco.md`. Note: the alert does not say "written" policy in so many words; "deploy internal policies and procedures" plus "documented" is the closest wording. |
| U2 | **AICPA Code of Professional Conduct**: Confidential Client Information Rule (ET 1.700.001) and SSTS § 1.3 data protection | Confidentiality and competence apply to AI. There is **no AI-specific AICPA standard**; a lack of one will not defend a negligence claim (CNA article). No law or CPA standard found that requires disclosure to clients; voluntary disclosure and specific (not boilerplate) consent suggested, especially where § 7216 data is involved. | **SECONDARY**: [Journal of Accountancy, April 2025](https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/) (read; CNA risk article, not official AICPA). Code text not read. **Optional lead: AICPA Small Firm Generative AI Policy Template (April 29, 2026), members-only; only use if someone at JMCO already has access. Free sources (CPAI, Oregon PLF, COSO, NIST) cover the same ground.** See `source-notes-frameworks-and-firms.md`. |
| U3 | **CPA firm AI policy guide**, [CPAI "Drafting an AI Policy that Actually Works"](https://www.cpai.com/Education-Resources/My-Firm/Data-Security-Risk-Management/Drafting-an-AI-Policy-that-Actually-Works) | Best accounting-specific outline: scope/purpose; governance (approved tools list, request process, firm devices, no sharing access); data privacy (how each tool stores data, whether it trains the model, redaction examples); quality and liability (human review, verify against primary sources, signing CPA stays responsible); documentation (record prompts, verification and reviewer in the client file); bias; transparency (disclosure language in engagement letters); acceptable use; training with signed acknowledgements; maintenance. Owner: an AI lead or committee. Attorney review of privacy and disclosure parts. Blaming the tool is not an option. | **READ.** Industry guide, not a regulator. |
| U4 | **ABA Formal Opinion 512** (July 29, 2024): competence, confidentiality, communication, supervision, fees, candor | Reasonable understanding of tool capabilities and limits; informed consent before inputting confidential information; supervisors need policies and training; boilerplate engagement-letter wording is not enough. Persuasive, not binding; legal rather than accounting. | **READ** (full text via Internet Archive copy of the official PDF, October 28, 2026). Managerial lawyers "must establish clear policies regarding the law firm's permissible use of GAI"; training should cover GAI basics, tool capabilities and limitations, ethical issues, and secure data handling, privacy and confidentiality; informed consent before inputting client information into self-learning tools, and boilerplate engagement-letter wording is not sufficient. Legal profession, persuasive only. Summary: `source-notes-frameworks-and-firms.md`. |
| U5 | **Oregon PLF, Generative AI Policy Development Guidelines for Law Firms** (rev. January 2026). [PDF](https://assets.osbplf.org/forms/practice_forms/generative-ai-policy-development-guidelines-for-law-firms.pdf) | Section list: scope and applicability; tool capabilities and limitations; confidentiality; acceptable use with examples; prohibited/high-risk uses (don't generate citations or authorities with general tools); review, verification and human oversight (secondary review for client-facing work); data security and incident procedure; ethics. Good model for structure; pairs with a sample policy on osbplf.org. | **READ** (first three pages). |
| U6 | Other US samples: [Oklahoma Bar article](https://www.okbar.org/cm_articles/ai-policies-do-not-wait-until-something-goes-wrong/), NJ State Library template | Approved tools list; no confidential data in unapproved tools; human review before anything leaves the firm; client consent. | **NOT ACCESSED / SECONDARY** (Oklahoma link 404). `[TBC]` |
| U7 | **COSO** guidance on internal control over generative AI (reported February 2026) | Finance-sector control framework, possibly relevant. | **READ** (free 32-page PDF, 2026, downloaded October 28, 2026): [coso.org](https://www.coso.org/generative-ai). Supports an Acceptable Use Policy, named tool owners, a cross-functional oversight committee, and role-appropriate training (Principle 4). Summary: `source-notes-frameworks-and-firms.md`. |

## 1B. US standards and widely used frameworks

| # | Source | Key content for JMCO | Status |
|---|---|---|---|
| F1 | **NIST AI 600-1**, Generative AI Profile (July 2024, approved July 25, 2024). [doi.org/10.6028/NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1) | Voluntary US companion to the NIST AI RMF; 12 generative-AI risks with suggested actions. GOVERN 1.4 / GV-1.4-002: "Establish transparent acceptable use policies for GAI". GOVERN 1.5: define who does periodic review and incident monitoring; after-action reviews and incident disclosure processes (GV-1.5-002). Also GOVERN 1.2, 3.2 (human-AI roles), 4.1 (safety-first culture). No employee-policy template. | **READ** (PDF downloaded and text-searched; Govern sections read in detail; the 12 risk descriptions and Map/Measure/Manage actions were not). |
| F2 | **ISO/IEC 42001:2023**, AI management system. [iso.org/standard/81230](https://www.iso.org/standard/81230.html) | International standard widely referenced by US firms (certifiable). Clause 5.2: top management sets a documented AI policy, communicated and available to interested parties, committed to meeting requirements and continual improvement. Annex A: about 38 controls. Clauses 7.2 competence and 7.3 awareness cover training. Control numbering differs between summaries. | **NOT ACCESSED** (iso.org 403; paid, third-party prices about USD 215–260). Content is SECONDARY: [Cyberday](https://www.cyberday.ai/requirement/iso-42001-5-2-ai-policy), [SureCloud](https://www.surecloud.com/resource-hub/iso-42001-annex-a-controls) |
| F3 | **OWASP Top 10 for Agentic Applications 2026** (December 9, 2025, OWASP GenAI Security Project, 100+ contributors). [Page](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026) | ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution (RCE); ASI06 Memory & Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents. Mitigations (Cycode table): least privilege per tool, own identity per agent, sandboxed execution with no network egress by default, human confirmation of sensitive actions, show raw actions at approval time, kill switch. | **READ** (official PDF, December 2025, CC BY-SA 4.0, checked October 27, 2026): ten names and official descriptions confirmed. Only ASI01 mitigations read in detail. Details: `source-notes-frameworks-and-firms.md`. |
| F4 | **SANS Critical AI Security Guidelines v1.4** (March 2026, CC BY 4.0, 17 pages). [Whitepaper PDF](https://assets.contentstack.io/v3/assets/bltabe50a4554f8e97f/blte964a6eef293d57e/whitepaper-critical-ai-security-guidelines); [page](https://www.sans.org/mlp/critical-ai-security-guidelines) | Technical controls for security teams, aligned with OWASP AI Exchange. **Eight** categories: conventional security controls; data minimization; AI supply chain; data/model engineering; limit model behavior (guardrails not infallible, access control outside the model, human oversight); model I/O handling; monitoring; GRC (includes secure agentic systems: function scope, sandboxing, allowlists, human escalation; and incident response with audit trails). Relevant to ITS, the gateway work and Level 4. | **READ** (whitepaper downloaded and read October 28, 2026). Summary: `source-notes-frameworks-and-firms.md`. |

## 1C. What big players do (US-based or global)

| # | Source | Finding | Status |
|---|---|---|---|
| P1 | **PwC** [US generative AI policy](https://www.pwc.com/us/en/tech-effect/ai-analytics/generative-ai-policy.html) and [global responsible AI commitment](https://www.pwc.com/gx/en/legal-notices/our-commitment-to-responsible-ai.html) | A "Network AI Policy" sets principles firm-wide; member firms adapt it to local law. Principles include compliance with data protection, IP and anti-discrimination law. Reported (2023): no client data given to public models. Reported: upskilling about 65,000 US staff. | Both pages returned 403: **NOT ACCESSED.** Facts above are SECONDARY (search snippets). **Read both by hand.** |
| P2 | **Deloitte, KPMG, EY** | Rollouts only: Deloitte PairD and Claude for a large workforce, KPMG Workbench and AI use effectively mandatory, EY.ai (reported 2026 industry article). No staff policy texts found. | **SECONDARY**, rollout news only. `[TBC: each firm's responsible-AI or transparency report]` |
| P3 | Generic AI acceptable-use templates | Tiered data classes; risk tiers (low risk no approval, moderate needs manager approval); mandatory training; human review; exceptions; review cycle. Agentic rules missing from nearly all. [SentinelOne](https://www.sentinelone.com/cybersecurity-101/data-and-ai/ai-acceptable-use-policy/), [DataGrail](https://www.datagrail.io/blog/ai-governance/ai-agent-policy/), [WitnessAI](https://witness.ai/blog/ai-acceptable-use-policy/), [Kite sample (Feb 2026)](https://www.kitetechgroup.com/wp-content/uploads/2026/02/KiteTechnology-Sample_AI_Acceptable_Use_Policy.pdf) | **SECONDARY** (vendor content, snippets). Kite PDF not read. |
| P4 | Multi-level AI badge frameworks | **EY Badges: five levels (Learning, Bronze, Silver, Gold, Platinum), AI is one domain** (READ, EY careers article); criteria per level are unverified, and the courses appear developer-focused (user, October 28, 2026), so EY is **not** used as a design comparator; mention only that EY has a tiered programme. **Bridgewater State University "AI Olympians" (READ): Bronze Foundational, Silver Intermediate, Gold Advanced, free, no test or approver; best peer example** (`source-notes-frameworks-and-firms.md`). Others: SK AX Level 1/2, ICAgile AILIT, Carleton AI literacy certificate. | See `portal-options-research.md` |

---

# Part 2. Reference list: EU, UK and Australia (keep separate; optional appendix)

| # | Source | Key content | Status |
|---|---|---|---|
| R1 | **EU AI Act, Article 4** (AI literacy). [Text](https://artificialintelligenceact.eu/article/4/); [Commission AI literacy Q&A](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers) | Providers and deployers must take measures for staff AI literacy. Applied from February 2, 2025; supervision and enforcement from August 2, 2026 by national authorities. Commission: no certificate, no specific training format, relying on instructions alone is "usually ineffective", organisations "can keep an internal record", no requirement to measure knowledge. Digital Omnibus (proposed November 19, 2025) per the Q&A page entered into force mid-July 2026: the duty is to "support the development of" literacy and does not require a specific level for any individual. | **READ** (both pages). Amending act number not confirmed. Relevance to JMCO only if it has EU operations, clients or staff `[TBC with compliance]` |
| R2 | **UK Generative AI Framework for HMG** (published January 18, 2024) | Ten principles (know the tech, lawful/ethical, secure, humans in control, lifecycle, right tool, open, commercial early, build skills, align with policy). Use cases to avoid (fully automated significant decisions, high-risk use without checks). A human authorises destructive or irreversible actions such as sending emails or changing records. Five learner groups for training. | **READ** (first 100,000 characters). **Withdrawn February 10, 2025**, replaced by the AI Playbook for the UK Government (not read) `[TBC]` |
| R3 | **Australia DTA policy for responsible use of AI in government** | Reported to recommend AI fundamentals training for all staff. | **SECONDARY only** (trade press). `[TBC: digital.gov.au]` |

---

# Part 3. What the research says about our design

- **Earn, not attend works.** The US sources (IRS reading of § 10.36, CPAI guide, ABA 512) all expect training plus documentation. The EU Q&A (Part 2) agrees that records of training are enough. Our register (training, test, assessor, approver, signed statement) exceeds the minimum.
- **No source requires a knowledge test**, so the test is a firm choice. The register helps with the "prove why" aim, not with a legal duty.
- **Human review and accountability for the person** is the one rule every source agrees on (IRS § 10.22, CPAI "blaming the tool is not an option", ABA 512).
- **Agentic content is thin everywhere.** The OWASP agentic list is the best source for Level 4 training (goal hijack, tool misuse, identity/privilege, code execution, human-agent trust). The UK framework (Part 2) adds that a human authorises irreversible actions.
- **Policy before levels.** ISO 42001 clause 5.2, NIST GOVERN 1.4 and the IRS reading of § 10.36 all expect a documented policy with a named owner and review date.
- **Enabling agentic waits on the Cloudflare AI Gateway** (user decision). Several controls (least privilege, egress limits, logging, kill switch) are gateway/ITS controls; link to `../aigateway/`.

# Part 4. Suggested policy outline for JMCO (draft from sources)

1. Purpose, scope (people, tools, devices), owner, approver, review date, link to levels.
2. Approved tools and how a new tool is requested; vendor vetting (is the vendor a subprocessor of client data?).
3. Data classes: what may go into which tool (public / internal / confidential / client / prohibited), with redaction examples.
4. Human review and accountability: the person who uses AI is responsible for the output; verification of facts, citations, calculations; secondary review for client-facing work.
5. Client confidentiality, engagement-letter language and consent, § 7216 and contract terms `[TBC with compliance]`.
6. Acceptable and prohibited uses with examples.
7. Training and levels (AI Licence Programme); signed acknowledgement.
8. Agentic AI: Level 4 only, approved tools and data only, human approval of irreversible actions, enabled only when the gateway controls are live.
9. Documentation: what is recorded in the client file `[TBC]`.
10. Incidents: report immediately, after-action review `[TBC]`.
11. Exceptions, enforcement, policy review cycle.

# Part 5. TODO list (manual verification and decisions)

**US primary texts to get first**
- [x] IRS OPR Alert 2026-19: DONE October 27, 2026 (see U1; official PDF read).
- [x] AICPA: no AI-specific standard found (October 27, 2026). **Optional: AICPA Small Firm Gen AI Policy Template (members-only, do not pay).** ET 1.700.001 text itself still unread.
- [ ] NIST AI 600-1: read the 12 risk descriptions and the Manage actions beyond GOVERN (DOI link above).
- [x] OWASP: DONE October 27, 2026 (official PDF read; remaining mitigations are in the PDF if needed for Level 4 content).
- [ ] ISO/IEC 42001:2023: buy or borrow (about USD 215–260). Confirm clause 5.2, 7.2, 7.3 and Annex A wording and numbering. Decide whether JMCO only borrows the structure or aims for certification.
- [x] SANS: DONE October 28, 2026 (v1.4, March 2026, whitepaper read; eight categories). Pass the PDF link to ITS.
- [x] PwC: user searched manually October 28, 2026 and found nothing usable. Drop PwC from the document (say "no staff policy text is publicly available").
- [x] Deloitte, KPMG, EY: no staff policy texts found by me (October 27) or by the user (October 28). Found EY tiered AI badges (see P4). Optional: open Deloitte Australia's AI usage statement from deloitte.com.au.
- [x] COSO: DONE October 28, 2026 (PDF read).
- [ ] Read the rest of the Oregon PLF guide and its sample policy; read the Kite sample PDF; ABA Formal Opinion 512 (DONE, read October 28, 2026).
- [x] Florida rules: DONE October 28, 2026 (`source-notes-florida.md`): no Board of Accountancy AI rule found; CPA confidentiality rule 61H1-23.001 and breach statute § 501.171 apply; Florida AI Bill of Rights failed. Still to do: check the DBPR Board site directly; HIPAA and Florida Digital Bill of Rights not researched.

**Questions for JMCO (compliance / legal)**
- [ ] **Confirm JMCO has tax practitioners under Circular 230** (website and FICPA listings suggest yes; see `source-notes-irs-and-jmco.md` section 2) and who holds principal authority under § 10.36. Does Circular 230 apply to them? Does any state or professional rule (AICPA, state board) require a written AI policy?
- [ ] What do client contracts and engagement letters say about AI and subprocessors? Is a disclosure default wanted?
- [ ] Is § 7216 taxpayer information in scope, and what consent is needed before it goes into an AI tool?
- [ ] Who owns the policy (likely the innovations team, with risk and compliance reviewing), who approves it, and when is the review date?
- [ ] Are there existing firm policies (information security, data classification, acceptable use) the AI policy should extend rather than duplicate?
- [ ] Does JMCO have any EU or UK operations, clients or staff? (Decides whether Part 2 matters.)

**Part 2 reference items (only if wanted)**
- [ ] Confirm the regulation number of the Digital Omnibus amendment to Article 4 in the EU Official Journal.
- [ ] Read the UK AI Playbook (replacement for the withdrawn framework) and the Australian DTA policy.

**Decisions for the framework paper**
- [ ] Policy first: add "create or confirm the AI policy" as step one of the plan, using the outline in Part 4.
- [ ] Decide whether the policy is a short staff-facing document plus a separate technical standard for agentic use.
- [ ] Decide what the tests check and how the register is kept as evidence.
- [ ] Decide how the gateway dependency is shown in the plan (Level 4 earned, agentic enabled when the gateway is live).

# Part 6. For the Word document

Suggested structure: scope and method; what we found (Part 1 tables with verification status); what it means for JMCO (Part 3); policy outline (Part 4); verified vs unverified register (the Status columns); work list (Part 5); optional appendix for Part 2. Keep the Status column: it answers "where did this come from and can we rely on it". The document should present Part 1 as the evidence base and Part 2 simply as additional reference material, with a short note that it could apply to EU or UK clients, if the firm has any (JMCO may; unconfirmed). Do not comment on why the parts are separated. Suggested wording: "If James Moore has clients or staff in the EU, UK or Australia, the following requirements and guidance may also apply. This section is included for reference until that is confirmed."
