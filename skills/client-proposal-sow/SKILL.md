---
name: client-proposal-sow
description: Step-by-step runbook for generating professional Statements of Work (SOW) and commercial proposals for AI automation projects with Setup Fee and Monthly Retainer pricing.
---

# Client Proposal & Statement of Work (SOW) — Procedural Runbook

Use this skill immediately after completing a discovery call and process audit to draft a formal, high-converting commercial proposal and Statement of Work (SOW).

---

## Step 1: The Commercial Structure (Dual-Tier Pricing)

Never sell pure hourly billing. Always package agency services into a **Setup Fee + Monthly Retainer**:

1. **Phase 1: Implementation & Deployment (One-Time Setup Fee)**
   - Covers custom architecture design, n8n/Make workflow construction, API credential setup, test coverage, and staff onboarding walkthrough.
   - *Typical Range for PyMEs:* $1,200 – $3,500 USD (depending on complexity).
2. **Phase 2: Ongoing Maintenance, SLA & Optimization (Monthly Retainer)**
   - Covers 24/7 uptime monitoring, error handling updates when 3rd-party APIs change, monthly prompt tuning, priority bug fixes, and 1 minor workflow iteration per month.
   - *Typical Range for PyMEs:* $350 – $950 USD/month.

---

## Step 2: Strict Scope Boundaries (Anti-Scope Creep)

Every SOW must feature an explicit **In-Scope vs. Out-of-Scope** table to protect your agency's margins:

| Category | In-Scope (Included) | Out-of-Scope (Requires Change Order) |
| :--- | :--- | :--- |
| **Integrations** | Specifically named tools: e.g., WhatsApp Cloud API, Airtable, Google Calendar, Cal.com. | Migrating client's entire legacy CRM or integrating unlisted custom databases. |
| **Workflow Logic** | Up to [N] defined decision branches and fallback routing. | Unlimited custom revisions or restructuring business logic mid-build. |
| **API Costs** | Configuration and architecture setup. | Client pays their own direct platform usage costs (OpenAI API tokens, Twilio, Make/n8n hosting). |
| **Support** | Bug resolution and API maintenance under agreed SLA (e.g., < 24-hr response). | On-site staff training or general IT support for unrelated software. |

---

## Step 3: Phased Timeline & Milestones

Break down project delivery into fast, reassuring sprints:

- **Sprint 1 (Days 1–3): Credentials & Data Contract:** Client provides API access; data schemas and trigger webhooks verified.
- **Sprint 2 (Days 4–7): Staging Build & Core Logic:** Functional workflow built in staging environment; internal end-to-end testing with mock data.
- **Sprint 3 (Days 8–10): Client Review & Feedback:** Live walkthrough demo with the client; one round of refinements based on feedback.
- **Sprint 4 (Days 11–12): Production Launch & Go-Live:** Deployment to production; monitoring active runs; handoff recording provided.

---

## Step 4: SOW Markdown Template

Deliver the final proposal ready for client signing or conversion to PDF:

```markdown
# Project Proposal & Statement of Work (SOW)

**Prepared for:** [Client Name / Company]  
**Prepared by:** [Your Agency Name]  
**Date:** [Date]  
**Valid Until:** [Date + 14 Days]  

---

### 1. Executive Summary & Objective
[Company Name] is partnering with [Your Agency] to eliminate [Core Bottleneck] by deploying an automated [System Name: e.g., 24/7 WhatsApp Lead Triage & CRM Sync System]. This system will reduce lead response time from [X hours] to [under 1 minute] and recover [X hours/week] of manual staff labor.

### 2. Deliverables & Specifications
- **Deliverable 1:** [e.g., Automated Lead Ingestion Webhook & Validation]
- **Deliverable 2:** [e.g., AI Intent Classification & Availability Check]
- **Deliverable 3:** [e.g., Calendar Booking & Automated Notification Cadence]
- **Deliverable 4:** [e.g., Error Alerting Channel to Agency Monitoring]

### 3. Scope Boundaries
[Insert Step 2 In-Scope vs Out-of-Scope Table]

### 4. Implementation Schedule
- **Duration:** 10–12 business days from kickoff.
- **Milestones:** [Insert Sprint Breakdown]

### 5. Investment & Commercial Terms
- **One-Time Implementation Fee:** $[Amount] USD (50% deposit upon signing, 50% upon production deployment).
- **Ongoing Support & Maintenance Retainer:** $[Amount] USD/month (First month begins 14 days after go-live).

### 6. Acceptance & Authorization
By signing below or approving via email, the parties agree to the scope and terms outlined in this document.

**Client Signature:** ____________________  **Date:** ____________  
**Agency Signature:** ____________________  **Date:** ____________  
```
