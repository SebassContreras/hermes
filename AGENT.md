# AGENT.md — Engineering Standard for AI Agents

> **Standard Specification & Best Practices for Architecting, Sizing, and Deploying Autonomous AI Agents in the Hermes Ecosystem.**

---

## 1. Executive Summary & Philosophy

An AI agent is not a monolithic prompt; it is a **compositional system** comprising an identity, long-term memory, modular skills, and deterministic tool bindings. 

### The Core Principles:
1. **Separation of Concerns:** Separate *who the agent is* (identity/voice) from *what the project requires* (conventions/rules) and *how tasks are done* (procedural skills).
2. **Context Budgeting:** Protect the attention budget. Bloated prompts degrade reasoning quality, introduce latency, and trigger the "lost-in-the-middle" effect.
3. **Deterministic Structure:** Use semantic delimiters (Markdown headers and XML tags) to eliminate ambiguity.
4. **Negative Constraints First:** Defining what the agent **must not** do is twice as effective at preventing errors as vague positive affirmations.

---

## 2. File Architecture & Standard Hierarchy

In the Hermes and modern agent ecosystem, context is organized into distinct, purpose-driven files:

```text
hermes/
├── AGENT.md                 # Universal project-level instructions (root README for machines)
├── agents/
│   └── <agent_name>/
│       ├── AGENT.md         # Role-specific operational rules, workflows, & constraints
│       ├── SOUL.md          # Personality, voice, cognitive style, & tone
│       ├── tools.py         # Deterministic tool definitions (Function Calling schemas)
│       └── skills/          # Procedural runbooks loaded on-demand
│           └── <skill>.md   # Step-by-step task execution guides
├── config/
│   └── settings.yaml        # Model parameters (temperature, max_tokens, stop sequences)
└── .env                     # Secure API credentials & model endpoints
```

### File Responsibilities Matrix

| File | Purpose | Scope | Lifecycle |
| :--- | :--- | :--- | :--- |
| **`AGENT.md`** | Operational rules, architecture, testing, workflows | Project / Directory | Versioned in Git |
| **`SOUL.md`** | Identity, voice, tone, philosophical boundaries | Agent Persona | Versioned in Git |
| **`SKILL.md`** | Step-by-step procedure for a discrete task | Modular / Dynamic | Loaded on-demand |
| **`MEMORY.md`** | User preferences, workspace state, past lessons | User / Workspace | Dynamically updated |
| **`tools.py`** | Executable tools and function call definitions | Agent Runtime | Versioned in Git |

---

## 3. Context Length & Character Budget Guidelines

System prompts that consume excessive context cause **attention dilution**, increase **Time-To-First-Token (TTFT)**, and inflate inference costs.

### Optimal Token & Character Limits

| Component | Target Tokens | Target Characters | Hard Ceiling |
| :--- | :--- | :--- | :--- |
| **`SOUL.md`** (Identity & Tone) | 300 – 800 tokens | 1,200 – 3,500 chars | 1,000 tokens (4,500 chars) |
| **`AGENT.md`** (Role Rules) | 800 – 2,000 tokens | 3,500 – 9,000 chars | 2,500 tokens (11,000 chars) |
| **`SKILL.md`** (Per Skill) | 400 – 1,200 tokens | 1,500 – 5,500 chars | 1,500 tokens (7,000 chars) |
| **Total System Context** | **1,500 – 3,500 tokens** | **6,000 – 15,000 chars** | **< 5% of Context Window** |

### Latency & Performance Rules of Thumb:
- **The 5% Rule:** Keep your persistent system prompt under **5%** of the model's active context window (e.g., < 4,000 tokens on a 128k model) to leave room for multi-turn history and tool responses.
- **Latency Cost:** Every additional 500 tokens of system prompt adds **~20–30ms** to Time to First Token (TTFT).
- **Zero Hoarding:** If a piece of reference documentation is larger than 1,500 tokens, do **not** bake it into the system prompt. Expose it via a search tool or read-file skill.

---

## 4. Instruction Engineering & Formatting Standards

### A. Semantic Delimiters (XML Tags)
Hermes 3 and frontier LLMs excel at parsing XML-tagged boundaries. Always compartmentalize instructions:

```markdown
<role>
Define precisely who the agent is and its core authority.
</role>

<operating_environment>
Define the runtime, available tools, directories, and constraints.
</operating_environment>

<workflow>
Step-by-step execution protocol (Observe -> Plan -> Execute -> Verify).
</workflow>

<constraints>
Explicit negative rules ("NEVER", "DO NOT", "AVOID").
</constraints>

<output_format>
Specific response formatting requirements (JSON, Markdown, schemas).
</output_format>
```

### B. The "Do & Don't" Negative Constraint Pattern
Models often overlook affirmative suggestions ("Please be concise"). Use unequivocal negative boundaries:

- **Weak:** *Try to write clean and short code.*
- **Strong:** *DO NOT output conversational filler ("Sure, here is your code"). Output only the code block or diff.*
- **Strong:** *NEVER guess external library APIs. If unsure of an import or signature, invoke the documentation tool.*

### C. Fallback & Uncertainty Protocol
Every agent must know how to fail gracefully:
1. When input is ambiguous: Ask targeted clarifying questions with concrete choices.
2. When a tool fails: Analyze the error output, hypothesize the fix, and retry once before escalating to the user.
3. When out of domain: Explicitly state the boundary and suggest the appropriate specialized agent.

---

## 5. Agent Authoring Checklist

Before committing a new agent to this repository, verify:

- [ ] Does the agent directory contain both `AGENT.md` (rules) and `SOUL.md` (voice)?
- [ ] Is the combined prompt size within the recommended **1,500 – 3,500 token** range?
- [ ] Are instructions structured with clear headers and XML tags?
- [ ] Does it include at least 3 non-negotiable negative constraints?
- [ ] Is all heavy, multi-page reference material externalized into `skills/` or tools?
- [ ] Has the agent been tested with `agents/runner.py` across typical and edge-case inputs?
