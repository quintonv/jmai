# AI Platform Comparison Notes: Cloudflare AI Gateway vs CData Connect AI Gateway

## Purpose

This document captures what was compared between Cloudflare AI Gateway and CData Connect AI Gateway, why the comparison was relevant, and the main conclusions from the review.

The comparison forms part of a broader evaluation of enterprise AI platforms for company-wide use, including:

- Business users accessing AI through a web interface
- Corporate SSO and identity integration
- Central AI governance
- Data privacy and DLP
- Audit and usage visibility
- Cost controls
- Multi-model access
- Developer and agentic AI use
- MCP and enterprise system integrations
- Custom company assistants and internal AI workflows

The objective is not simply to select an AI chat application. The broader goal is to identify a platform that can act as a governed enterprise AI layer across normal business users, developers, agents, and internal systems.

---

# Why Cloudflare and CData Were Compared

Cloudflare and CData are both moving toward the role of an enterprise AI gateway, but they approach the problem from different directions.

Cloudflare approaches AI from a security, network, governance, model access, and application infrastructure perspective.

CData approaches AI from an enterprise data connectivity, integration, MCP, business system access, and governance perspective.

This makes the comparison useful because both platforms could potentially sit centrally in the future AI architecture, but they solve different parts of the problem particularly well.

The key question was:

> Do we primarily need a secure and governed gateway to AI models, or do we need a platform that also provides a governed bridge between AI agents and enterprise business systems?

---

# High Level Positioning

| Area | Cloudflare AI Gateway | CData Connect AI Gateway |
|---|---|---|
| Core focus | AI model gateway, security, governance, observability, routing and infrastructure | AI model gateway combined with enterprise data, MCP, tools and business system connectivity |
| Main architectural strength | Governing AI traffic | Governing AI traffic and AI access to enterprise systems |
| Business user frontend | Playground for testing, with the option to host or build a corporate AI portal | Intended mainly as a backend gateway and integration layer rather than an employee chat product |
| Multi-model access | Strong | Strong |
| Corporate identity | Strong, especially with Cloudflare Access and Zero Trust | Strong identity and permission model, particularly when accessing connected systems |
| DLP and privacy | Major strength | Strong governance, but more focused on data permissions and system access |
| AI guardrails | Strong | Strong |
| Logging and observability | Strong | Strong |
| Cost controls | Strong | Strong |
| Model routing and fallback | Strong | Strong |
| Enterprise data connectivity | Requires separate integrations or architecture | Major strength |
| MCP | Supported as part of the wider architecture | Core strength |
| Access to ERP, CRM, databases and SaaS | Requires integrations to be built or selected | Core capability |
| Governed read and write actions | Depends on the application and integration layer | Core capability |
| Zero Trust and network security | Major strength | Not the primary focus |
| Platform maturity | More established AI gateway | Newer combined AI gateway proposition |

---

# What We Learned About Cloudflare

## 1. Cloudflare Is Best Viewed as an AI Control Plane

Cloudflare AI Gateway is not simply a proxy for model APIs.

It can provide a central control point for AI requests across multiple applications, users, models, and providers.

The platform is particularly strong for:

- Central AI governance
- DLP and privacy scanning
- Prompt and response guardrails
- Request logging
- Usage analytics
- Cost tracking
- Spend limits
- Rate limiting
- Model routing
- Provider fallback
- Multi-model access
- User and application metadata
- Integration with broader Cloudflare security services

This means multiple AI tools can potentially use the same governed backend.

---

## 2. Cloudflare Does Not Need to Dictate the Employee Frontend

Cloudflare AI Gateway includes a Playground that can be used to interact with models and demonstrate gateway functionality.

The Playground is useful for:

- Model testing
- Prompt testing
- DLP demonstrations
- Guardrail demonstrations
- Gateway policy testing
- Observability and logging demonstrations

It is not intended to be the primary corporate ChatGPT-style interface for all employees.

For employee use, several options are available:

- Host an open source ChatGPT-style frontend
- Use a product such as Open WebUI or LibreChat
- Build a custom corporate AI portal
- Host the frontend using Cloudflare infrastructure
- Protect the portal with Cloudflare Access
- Integrate authentication with Microsoft Entra ID or another corporate identity provider

This creates an architecture where the company controls the employee experience while Cloudflare controls the underlying AI governance layer.

---

## 3. Cloudflare Provides Strong Separation Between UI, Governance and Models

A possible architecture is:

```text
Employees
    |
    v
Corporate AI Portal
    |
    v
Corporate SSO / Cloudflare Access
    |
    v
Cloudflare AI Gateway
    |
    + DLP
    + Guardrails
    + Logging
    + Cost Controls
    + Rate Limits
    + Routing
    + Analytics
    |
    v
OpenAI / Anthropic / Google / Other Providers
```

This separation is attractive because the company is not locked into:

- One AI model
- One provider
- One employee frontend
- One developer tool

The frontend can change while the gateway stays the same.

The models can also change without requiring the company to replace the employee interface.

---

## 4. Cloudflare Is Strong for Company-Wide AI Governance

Cloudflare is particularly attractive if the initial objective is:

> Provide employees and developers with secure access to multiple AI models under one governed platform.

It provides a clear place to enforce:

- Who can use AI
- Which applications can use AI
- Which models are available
- How much users or teams can spend
- What sensitive information may be sent
- What content should be blocked
- How requests are logged
- How requests are routed
- Which providers may receive requests

This makes Cloudflare a strong candidate for the central enterprise AI infrastructure layer.

---

## 5. Cloudflare Is Also Attractive for Developers

Developers do not necessarily have to use a single vendor's development tool.

Approved coding tools can potentially connect through the same AI Gateway, including tools such as:

- Claude Code
- Codex
- OpenCode
- Custom CLI tools
- Internal applications
- Custom agents

This allows the company to govern developer AI access without requiring every developer to use the same interface.

---

# What We Learned About CData

## 1. CData Is Moving Beyond Traditional Data Connectivity

CData has historically been known for connecting business applications, databases, SaaS platforms, ERP systems, CRM systems, and data platforms.

Its newer Connect AI Gateway proposition extends this into AI.

The platform combines:

- Model gateway functionality
- Enterprise data connectivity
- MCP
- Agent tools
- Permissions
- Business context
- Governed actions
- Logging and observability

This makes CData more than a model gateway.

It is also potentially a governed integration layer between AI agents and business systems.

---

## 2. CData's Main Differentiator Is Enterprise Data Access

CData becomes especially interesting when AI needs to access real company systems.

Examples include:

- Microsoft 365
- SharePoint
- OneDrive
- Dynamics
- Salesforce
- NetSuite
- SAP
- Workday
- SQL Server
- Snowflake
- Other databases
- Other enterprise SaaS applications

Rather than building individual integrations for each AI application, CData can expose these systems through centrally managed connectors and tools.

This could significantly reduce integration work in a future agentic AI environment.

---

## 3. CData Is Particularly Strong for MCP

MCP is a major part of CData's proposition.

The platform can potentially provide a managed MCP layer for:

- CData maintained connectors
- Internal custom MCP servers
- Third party MCP servers
- Agents
- AI clients
- Internal applications

This gives the company a central place to govern which tools and systems an AI agent may access.

That is important because MCP governance is likely to become a significant enterprise concern as AI agents become more capable.

---

## 4. CData Could Be Strong for AI That Takes Business Actions

Cloudflare is very strong at governing the AI request.

CData adds another dimension by focusing on what the AI is allowed to do inside business systems.

Examples could include:

- Read a customer's CRM record
- Retrieve finance information
- Query a database
- Find SharePoint documents
- Update a CRM opportunity
- Create or modify a business record
- Combine information across multiple enterprise applications

This is a major distinction.

A future enterprise AI platform may not only answer questions.

It may increasingly need to take actions.

CData appears particularly well positioned for this type of architecture.

---

## 5. Identity and Source Permissions Are Important Strengths

One of the key questions with enterprise AI is whether an AI agent uses:

- A shared service account

or

- The permissions of the actual employee making the request

The second model is usually preferable for enterprise governance.

CData is positioning its architecture around maintaining user identity and source system permissions when AI accesses enterprise systems.

This could be important for systems containing:

- Client information
- Financial information
- HR information
- Confidential documents
- Internal business records

The AI should ideally only see information the requesting employee is already authorised to access.

---

# The Main Architectural Difference

The simplest way to describe the difference is:

## Cloudflare

> Govern how users, applications and agents access AI models.

Example:

```text
Users / Applications / Developers
              |
              v
      Cloudflare AI Gateway
              |
              + Security
              + DLP
              + Guardrails
              + Cost Controls
              + Logging
              + Routing
              |
              v
     AI Model Providers
```

## CData

> Govern how AI accesses both models and enterprise systems.

Example:

```text
Users / Agents / AI Applications
              |
              v
       CData AI Gateway
          |         |
          |         |
          v         v
       Models     MCP / Tools
                    |
                    + CRM
                    + ERP
                    + Microsoft 365
                    + Databases
                    + SaaS
                    + Internal Systems
```

Cloudflare is strongest at the AI gateway and security layer.

CData is strongest where AI needs deep interaction with enterprise data and systems.

---

# Key Findings

## Cloudflare Strengths

Cloudflare appears strongest in:

- Company-wide AI governance
- DLP
- Prompt and response privacy controls
- AI guardrails
- Identity integration
- Zero Trust
- Network security
- Multi-model access
- Model routing
- Provider fallback
- Cost control
- Rate limiting
- AI observability
- Central logging
- Flexible employee frontend architecture
- Supporting multiple developer tools
- Avoiding model and frontend lock-in

---

## CData Strengths

CData appears strongest in:

- Enterprise system connectivity
- MCP
- Connecting agents to business applications
- Governed read and write access
- Existing enterprise application connectors
- Business data context
- Source system permissions
- Record level access
- Agent tool governance
- Integrating AI with existing ERP, CRM, database and SaaS environments

---

# Areas Where Cloudflare Appears Stronger

Cloudflare currently appears stronger when the immediate requirement is:

> Securely provide a large number of employees with controlled access to AI models.

This includes:

- Corporate AI chat
- DLP
- AI security
- Model governance
- Cost controls
- Auditability
- Developer model access
- Multi-model flexibility
- Zero Trust integration

Cloudflare also has the benefit of a broader established infrastructure and security ecosystem.

---

# Areas Where CData Appears Stronger

CData may be stronger when the requirement becomes:

> Allow AI agents to securely interact with company data and business applications.

This includes:

- Live enterprise data
- CRM access
- ERP access
- Microsoft 365 data
- Database access
- Business actions
- MCP servers
- Tool permissions
- Record level access
- User based permissions

This may become increasingly important as the organisation moves from simple AI chat toward agentic workflows and automation.

---

# Important Risk and Maturity Consideration

The new CData Connect AI Gateway proposition is significantly newer than Cloudflare AI Gateway.

This means that any CData review should validate:

- Production readiness
- General availability status
- SLA
- Support model
- Pricing
- Licensing
- Data residency
- Security certifications
- Audit functionality
- Identity integration
- Model support
- MCP governance
- Connector limitations
- Read and write controls
- Permission inheritance
- High availability
- Roadmap commitments

The CData proposition is strategically interesting, but maturity should be validated carefully before treating it as a production standard.

---

# What This Means for the Project

The comparison suggests that Cloudflare and CData should not necessarily be viewed as identical products.

They potentially solve different layers of the future enterprise AI architecture.

A possible future architecture could even use both concepts:

```text
Employees / Developers / Applications
                 |
                 v
        Corporate AI Experience
                 |
                 v
       AI Governance / Gateway
                 |
        + Model Governance
        + DLP
        + Guardrails
        + Cost Controls
        + Logging
                 |
                 v
       Enterprise Tool Layer
                 |
        + MCP
        + CRM
        + ERP
        + Microsoft 365
        + Databases
        + Internal Systems
```

Cloudflare is currently the stronger candidate for the upper governance, security and model access layer.

CData is particularly interesting for the lower enterprise integration, MCP and business system access layer.

Whether one product can satisfactorily cover both layers should be tested during the vendor reviews.

---

# Recommended Evaluation Focus

The next vendor discussions should focus less on general product demonstrations and more on realistic enterprise use cases.

## Business User Scenario

An employee signs into a corporate AI portal using their normal company identity and asks questions across approved AI models.

Evaluate:

- SSO
- User identity
- DLP
- Guardrails
- Chat history
- File uploads
- Model choice
- Usage logging
- Cost controls
- User based policies

## Enterprise Data Scenario

An employee asks:

> Show me information about a client using our authorised internal systems.

Evaluate:

- User identity propagation
- SharePoint access
- CRM access
- ERP access
- Database access
- Permission inheritance
- Audit logging
- Data leakage prevention

## Agent Action Scenario

An authorised agent is asked to:

> Find a business record, analyse it, and update a related system.

Evaluate:

- MCP
- Tool approval
- Read permissions
- Write permissions
- Human approval
- Audit history
- Rollback or control mechanisms
- Source system identity

## Developer Scenario

A developer uses an approved coding agent.

Evaluate:

- CLI support
- IDE support
- Model access
- User attribution
- Cost attribution
- Usage limits
- MCP
- Audit logs
- DLP
- Secrets protection

---

# Current Conclusion

Cloudflare currently appears to be the stronger fit for a central, company-wide AI governance and model access platform.

Its strengths align well with the immediate requirement to provide controlled AI access to normal business users, developers, applications and agents.

CData introduces a different and potentially very valuable capability.

Its main advantage is the ability to connect AI securely to existing enterprise systems, data and business actions through a governed data and MCP layer.

This means CData should remain on the shortlist, particularly if the long term objective is to move beyond AI chat toward enterprise agents that can securely retrieve and update live business information.

The most important conclusion from the comparison is that the future platform should not be evaluated only as an AI chat replacement.

It should be evaluated as enterprise AI infrastructure covering:

- User experience
- Identity
- Governance
- Security
- Models
- Cost
- Data
- Tools
- Agents
- Business systems
- Auditability

The preferred platform should support both current AI usage and the expected move toward more agentic, integrated enterprise AI workflows.
