---
name: agency-kanban-playbook
description: Orchestrator runbook for turning a founder goal into a Kanban card graph across the agency's specialist profiles — pipeline templates, card brief template, handoff review, and status reporting.
---

# Agency Kanban Playbook — Orchestrator Runbook

Use this skill before creating 3 or more cards for one goal, when a handoff comes back for review, or when the founder asks "where are we?". It is for the orchestrator (default profile) only; specialists never load it.

---

## Step 1: Ground the Plan

1. Restate the goal in one sentence and name the client (or "internal").
2. Check memory for standing decisions: ICP, offer, pricing anchors, brand tone, client stage, client folder.
3. List the shared decisions this goal needs. Decide every one you are allowed to decide; turn the rest into a single 1-3-1 brief for the founder **before** creating cards that depend on them.
4. Pick the pipeline template below that fits; drop stages that add nothing.

---

## Step 2: Pipeline Templates

Arrows mean `parents=[...]`; `∥` means parallel cards with no link between them.

| Goal | Card graph |
| :--- | :--- |
| **New client (discovery → close)** | `business_process_auditor` (audit + ROI) → `proposal_sow_architect` (proposal + SOW) → **founder approves price & sends** |
| **Delivery (signed client)** | `ai_automation_engineer` (workflows) ∥ `senior_fullstack_engineer` (custom code, only if needed) → **founder demo** → `linkedin_case_study_creator` (case study, after client consents) |
| **Demand generation** | `linkedin_growth_specialist` (campaign + cadence) ∥ `seo_sem_strategist` (keywords + ads plan) → `product_copywriter` (landing page + assets aligned to both) |
| **Website / landing page** | `product_copywriter` (copy) ∥ `seo_sem_strategist` (keyword map) → `senior_fullstack_engineer` (build) |
| **Content from a win** | `linkedin_case_study_creator` → `linkedin_growth_specialist` (distribution plan) |

Pass repo skills to the right specialist with `skills=[...]`:
`discovery-audit-blueprint` → `business_process_auditor` · `client-proposal-sow` → `proposal_sow_architect` · `linkedin-lead-magnet-system` → `linkedin_case_study_creator` or `linkedin_growth_specialist`.

Stages marked **founder** are not cards. Stop there, present the result, and wait for the founder's decision.

---

## Step 3: Card Brief Template

Every card body must stand alone. The worker sees only its own card and its parents' handoffs.

```markdown
## Objective
<one sentence: what outcome this card produces and for whom>

## Context
- Client: <name, industry, size> | Stage: <discovery / proposal / delivery>
- Facts: <volumes, tools in use, pains, budget signals>
- Inputs: <file paths, links, parent cards to read>

## Decisions already made (do not revisit)
- <ICP / offer / pricing anchor / tone / format / deadline>

## Deliverable
<exact artifact and language: e.g. "SOW in Spanish, GitHub Markdown, sections per client-proposal-sow">

## Done when
- [ ] <checkable criterion>
- [ ] <checkable criterion>
- [ ] Deliverable files attached via kanban_complete(artifacts=[...])

## Boundaries
- Out of scope: <...>
- Do not: contact the client, publish, quote prices outside the anchors above.

## Block if
<missing input or ambiguity that must stop the work instead of a guess>
```

Card settings:
- `title`: verb + object + client, e.g. "Draft SOW — Clínica Dental Ruiz".
- `tenant`: `<client-slug>` for client work, so `kanban_list(tenant=...)` shows one client at a time.
- `idempotency_key`: `<client-slug>:<stage>`, so a re-sent request never duplicates cards.
- `priority`: 3 for committed deliveries, 2 for open deals, 1 for pipeline/marketing, 0 for internal work.
- Workspace: if memory holds an absolute client folder path, use `workspace_kind="dir"` with that `workspace_path` so deliverables persist; otherwise use the default scratch workspace and require `artifacts`.
- `goal_mode=true` only for open-ended drafting cards that rarely finish in one shot.

---

## Step 4: Review a Handoff

When a card wakes you (completed or blocked):

1. `kanban_show(task_id)` and read the summary, metadata, and artifacts.
2. Check each "Done when" box against the evidence. Do not trust the summary alone; open the artifact.
3. Decide:
   - **Meets the bar** → accept; if a child card waits on it, let the dispatcher promote it.
   - **Fixable gap** → create a rework card for the same assignee with `parents=[<reviewed card>]` and the numbered, specific changes in its body. Do not rewrite the deliverable yourself.
   - **Blocked on input** → if memory or context holds the answer, `kanban_comment` it on the card, then `kanban_unblock`; otherwise ask the founder one precise question and relay the answer the same way.
   - **Failed twice or out of lane** → stop; report the blocker and options to the founder.
4. Never forward an unreviewed artifact to the founder as final.

---

## Step 5: Status Report

When the founder asks for status, or after a batch of handoffs:

1. `kanban_list` filtered to non-archived cards.
2. Reply with:

```markdown
| Card | Owner | Status | Next |
| :--- | :--- | :--- | :--- |

**Needs your decision:** <numbered list, each with a recommendation>
**Next action:** <one action — owner>
```

3. Archive the cards of goals the founder has dropped.
