# Hermes Agents Workspace

Centralized repository for specialized autonomous agents powered by the **Hermes** ecosystem (Nous Research).

## 📁 Repository Structure

```text
hermes/
├── AGENT.md                            # Universal standards, character limits & authoring rules
├── agents/
│   ├── senior_fullstack_engineer/      # Web, mobile & cloud systems architect
│   │   ├── AGENT.md                    # Technical boundaries, workflows & rules
│   │   └── SOUL.md                     # Persona, cognitive style & voice
│   ├── linkedin_growth_specialist/     # B2B outbound client acquisition & social selling
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── seo_sem_strategist/             # Organic & paid search acquisition & CRO
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── product_copywriter/             # Natural product prose, value storytelling & messaging
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── business_process_auditor/       # SMB discovery, bottleneck diagnosis & ROI modeling
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── ai_automation_engineer/         # Low-code workflows (n8n, Make), WhatsApp & Voice agents
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── proposal_sow_architect/         # Scope of Work (SOW) & pricing tier proposals
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── linkedin_case_study_creator/    # Viral breakdowns, carousels & inbound lead magnets
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   └── runner.py                       # CLI agent runtime supporting Hermes models
├── config/                             # Prompts, model presets, and environment setups
├── skills/                             # Reusable agent skills and procedural runbooks
│   ├── discovery-audit-blueprint/      # Process audit & quantified ROI calculation runbook
│   ├── linkedin-lead-magnet-system/    # 5-part LinkedIn hook & comment-to-DM conversion
│   └── client-proposal-sow/            # Two-tier pricing & Statement of Work runbook
├── tools/                              # Custom tool definitions (Function Calling)
├── .env.example                        # Template for model endpoints & API keys
├── requirements.txt                    # Python dependencies
├── .gitignore
└── README.md
```

## 🚀 Quickstart

### 1. Configure Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
```

### 2. Run Any Agent Interactively
```powershell
python agents/runner.py business_process_auditor
python agents/runner.py ai_automation_engineer
python agents/runner.py proposal_sow_architect
python agents/runner.py linkedin_case_study_creator
python agents/runner.py senior_fullstack_engineer
python agents/runner.py linkedin_growth_specialist
python agents/runner.py seo_sem_strategist
python agents/runner.py product_copywriter
```

### 3. Hermes Desktop Integration
All agents and skills are synchronized with your **Hermes Desktop** app (running natively on your local GPU model). Switch to any agent in the desktop chat using:
```text
/personality business_process_auditor
/personality ai_automation_engineer
/personality proposal_sow_architect
/personality linkedin_case_study_creator
```
*(Or switch profile with `/profile <agent_name>`)*.

### 📖 Agent Engineering Standard
For character budget rules, token guidelines, and authoring instructions, read [AGENT.md](AGENT.md).
