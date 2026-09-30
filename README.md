# Hermes Agents Workspace

Centralized repository for specialized autonomous agents powered by the **Hermes** ecosystem (Nous Research).

## 📁 Repository Structure

```text
hermes/
├── agents/
│   ├── senior_fullstack_engineer/      # Web, mobile & cloud systems architect
│   ├── linkedin_growth_specialist/     # B2B outbound client acquisition & social selling
│   ├── seo_sem_strategist/             # Organic & paid search acquisition & CRO
│   ├── product_copywriter/             # Natural product prose, value storytelling & messaging
│   └── runner.py                       # CLI agent runtime supporting Hermes models
├── config/                             # Prompts, model presets, and environment setups
├── skills/                             # Reusable agent skills and workflows
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
python agents/runner.py linkedin_growth_specialist
python agents/runner.py seo_sem_strategist
python agents/runner.py product_copywriter
python agents/runner.py senior_fullstack_engineer
```
