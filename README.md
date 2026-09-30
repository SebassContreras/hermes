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
│   └── runner.py                       # CLI agent runtime supporting Hermes models
├── config/                             # Prompts, model presets, and environment setups
├── skills/                             # Reusable agent skills and procedural runbooks
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
python agents/runner.py senior_fullstack_engineer
python agents/runner.py linkedin_growth_specialist
python agents/runner.py seo_sem_strategist
python agents/runner.py product_copywriter
```

### 📖 Agent Engineering Standard
For character budget rules, token guidelines, and authoring instructions, read [AGENT.md](AGENT.md).
