---
name: discovery-audit-blueprint
description: Standard operating procedure for turning raw client discovery notes into a structured Business Process Audit, As-Is vs To-Be blueprint, and quantified ROI model.
---

# Discovery Audit Blueprint — Procedural Runbook

Use this skill whenever you need to process raw notes, call transcripts, or client intake forms from a small business owner into a client-facing **Automation Audit Report**.

---

## Step 1: Input Ingestion & Extraction

From the client notes or transcript, extract and list the following variables:
1. **Business Profile:** Industry, primary product/service, estimated monthly transaction or lead volume, team size.
2. **Current Tech Stack:** CRM, communication channels (WhatsApp, email), scheduling tools, spreadsheets, accounting software.
3. **Core Pain Points:** The 2-3 specific operational complaints mentioned by the owner (e.g., "we take 4 hours to reply to leads", "we copy data manually from Gmail to Excel").

---

## Step 2: The Three-Friction Audit Matrix

Categorize every identified bottleneck into one of three friction buckets:

| Friction Bucket | Symptom in SMBs | Typical Solution |
| :--- | :--- | :--- |
| **Lead Leakage** | Leads wait > 15 mins for response; forgotten follow-ups; leads lost in WhatsApp chat history. | Instant webhook response, 24/7 AI conversational qualification, automated CRM entry. |
| **Admin Glue Work** | Copy-pasting data between systems; manual invoice drafting; status updates sent by hand. | Deterministic n8n/Make pipelines syncing data between forms, CRM, and accounting. |
| **Phone / Support Drain** | Front desk overwhelmed answering identical FAQs; missed calls outside business hours. | AI Voice Receptionist (Vapi/Retell) + WhatsApp FAQ knowledge base assistant. |

---

## Step 3: As-Is vs. To-Be Process Mapping

Create a clear comparison table contrasting the current manual workflow with the proposed automated workflow:

| Step # | As-Is (Manual Workflow) | Time / Cost | To-Be (Automated Workflow) | New Cycle Time |
| :--- | :--- | :--- | :--- | :--- |
| **1. Trigger** | Customer fills form or sends WhatsApp message | N/A | Webhook triggers instant n8n scenario | < 2 seconds |
| **2. Triage** | Human employee reads message, checks availability | 10–30 mins | AI evaluates intent, checks Google Calendar / CRM | Instant |
| **3. Action** | Human sends manual email/message back to customer | 5–15 mins | AI sends tailored reply with Cal.com booking link | < 30 seconds |
| **4. Logging** | Employee types contact info into spreadsheet | 5 mins | Automated write to Airtable/CRM + Slack alert | Instant |

---

## Step 4: Quantified Financial ROI Calculation

Always compute the quantifiable business case using this exact formula:

```text
Monthly Labor Cost Recovered = (Hours Spent per Week on Manual Process * 4.33) * Employee Hourly Rate
Net Monthly Client Savings   = Monthly Labor Cost Recovered - (Software Subscriptions + Maintenance Retainer)
Payback Period (Months)      = One-Time Setup Fee / Net Monthly Client Savings
```

*Example Presentation:*
- Hours wasted: 15 hrs/week across 2 team members.
- Labor rate: $15/hr → **$974/month in wasted labor**.
- Estimated tech stack cost: $50/mo (Make + OpenAI API).
- Projected net savings: **$924/month recovered** plus zero missed leads.

---

## Step 5: Deliverable Markdown Template

Output the final report using this clean structure:

```markdown
# Business Process & Automation Audit: [Client Company Name]

## 1. Executive Summary & Core Bottleneck
[2-3 punchy paragraphs summarizing the biggest operational leak and its financial impact]

## 2. Process Comparison (As-Is vs. To-Be)
[Insert Step 3 Table]

## 3. Recommended Architecture & Tech Stack
- **Trigger Layer:** [e.g., Webhook from Typeform / Meta WhatsApp API]
- **Orchestration Layer:** [e.g., n8n hosted on Railway / Make.com]
- **Intelligence Layer:** [e.g., GPT-4o mini for extraction / Retell AI for voice]
- **Data & Destination:** [e.g., Airtable / HubSpot CRM / Google Sheets]

## 4. Quantified ROI Model
- **Monthly Hours Saved:** [X] hours/month
- **Labor Value Recovered:** $[X] USD/month
- **Speed to Lead Improvement:** From [X] hours to under [X] seconds

## 5. Phased Implementation Roadmap
- **Phase 1 (Quick Win — Days 1-5):** [The single highest-impact workflow]
- **Phase 2 (Core Automation — Weeks 2-3):** [Secondary integrations & CRM sync]
- **Phase 3 (Optimization & Scaling):** [Voice agents, advanced analytics]
```
