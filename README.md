# Hermes Agents Workspace

Centralized repository for specialized autonomous agents powered by the **Hermes** ecosystem (Nous Research).

## 📁 Repository Structure

```text
hermes/
├── AGENT.md                            # Universal standards, character limits & authoring rules
├── agents/
│   ├── hermes_orchestrator/            # Chief of Staff: routes work to the specialists via Kanban
│   │   ├── AGENT.md
│   │   └── SOUL.md
│   ├── senior_fullstack_engineer/      # Web, mobile & cloud systems architect
│   │   ├── AGENT.md                    # Technical boundaries, workflows & rules
│   │   └── SOUL.md                     # Persona, cognitive style & voice
│   ├── code_quality_auditor/           # Clean Code, SOLID, dead code & README parity auditor
│   │   ├── AGENT.md
│   │   └── SOUL.md
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
│   ├── prompt_assembly.py              # SOUL.md + AGENT.md → system prompt (shared by runner & sync)
│   └── runner.py                       # CLI agent runtime supporting Hermes models
├── config/
│   └── hermes_desktop.yaml             # Hermes Desktop deployment manifest (toolsets, config, roster)
├── scripts/
│   └── sync_hermes.py                  # Applies agents, skills & manifest to the local Hermes install
├── skills/                             # Reusable agent skills and procedural runbooks
│   ├── agency-kanban-playbook/         # Orchestrator: card graphs, brief template, handoff review
│   ├── code-quality-audit/             # Codebase audit: SOLID, orphan code, test fidelity, README parity
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
python agents/runner.py hermes_orchestrator
python agents/runner.py business_process_auditor
python agents/runner.py ai_automation_engineer
python agents/runner.py proposal_sow_architect
python agents/runner.py linkedin_case_study_creator
python agents/runner.py senior_fullstack_engineer
python agents/runner.py code_quality_auditor
python agents/runner.py linkedin_growth_specialist
python agents/runner.py seo_sem_strategist
python agents/runner.py product_copywriter
```

### 3. Hermes Desktop Integration
The repo is the source of truth. After editing any agent, skill, or `config/hermes_desktop.yaml`, apply it to your **Hermes Desktop** install and start a new chat:
```powershell
python scripts/sync_hermes.py --dry-run   # preview
python scripts/sync_hermes.py             # apply
```
The sync is needed because Hermes injects only each profile's `SOUL.md` into the prompt. `AGENT.md`/`AGENTS.md` are never loaded, so the script compiles `SOUL.md + AGENT.md` (same assembly as `runner.py`) into every profile's `SOUL.md`. It also:
- Turns the **default profile** into `hermes_orchestrator` and enables its `kanban` toolset.
- Adds `skills/` to every profile's `skills.external_dirs`.
- Writes the profile descriptions used for routing.
- Installs the official skills listed in the manifest.

**Working with the team:** ask the default Hermes chat for outcomes ("prepara la propuesta para el cliente X"). The orchestrator plans the work, asks for your approval when the work spans several specialists or reaches a client, then creates Kanban cards that the specialist profiles execute. Open the board with `hermes dashboard` → **Kanban**. To talk to one specialist directly, switch with `/profile <agent_name>`. Avoid `/personality <agent_name>`: it only makes the orchestrator imitate that specialist and routes no work.

### 📖 Agent Engineering Standard
For character budget rules, token guidelines, and authoring instructions, read [AGENT.md](AGENT.md).
