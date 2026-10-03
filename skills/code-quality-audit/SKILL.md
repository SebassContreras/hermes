---
name: code-quality-audit
description: Procedural runbook for conducting comprehensive repository audits: Clean Code & SOLID analysis, orphan file & function detection, test validity inspection, and README ground-truth verification.
---

# Code Quality Audit — Procedural Runbook

Use this runbook to conduct a thorough, forensic audit of an entire codebase or repository. This procedure verifies clean code standards, separation of concerns, dead/orphaned code, test fidelity, and alignment with project documentation.

---

## Phase 1: Discovery & Entry-Point Grounding

1. **Inventory the Core Manifests:**
   - Locate dependency and configuration files (`package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`, `tsconfig.json`).
   - Identify active language versions, runtimes, and external dependencies.
2. **Catalog Entry Points:**
   - Map all executable roots: CLI entry points (`main.py`, `bin/`), web server routers (`app.py`, `server.ts`, `routes/`), background workers, and exported library barrels (`index.ts`, `__init__.py`).
3. **Map Repository Topology:**
   - Identify the architectural pattern in use (Layered/Hexagonal, Modular Monolith, MVC, micro-packages).
   - Trace directory hierarchy and note intended boundaries between presentation, domain, and data layers.

---

## Phase 2: Orphaned Files & Dead Code Triage

1. **Detect Orphaned Files:**
   - Build a list of all source files in the repository.
   - Trace imports recursively starting from all entry points, build scripts, and test suites.
   - Any file not reached by the import graph or dynamic plugin loader is flagged as a candidate **Orphaned File**.
2. **Detect Dead & Unreferenced Functions:**
   - Search for function and class definitions that have no call sites outside their own definition block.
   - Inspect internal helper functions, private methods, and legacy utilities.
   - Verify if functions are exported only for tests or if they are genuinely abandoned.
3. **Audit Zombie Dependencies:**
   - Compare packages listed in `requirements.txt` / `package.json` against all `import` or `require` statements across the codebase.
   - Flag unused packages that bloat install sizes or introduce unneeded security risks.

---

## Phase 3: Clean Code & Responsibility Analysis

Apply the **SOLID & Clean Code Checklist** to core domain modules:

| Criterion | Code Smell / Antipattern | Verification Check |
| :--- | :--- | :--- |
| **Single Responsibility (SRP)** | God modules (>300 lines) mixing HTTP routing, business logic, DB queries, and formatting. | Does each file/class have only one reason to change? Are concerns cleanly separated? |
| **Coupling & Cohesion** | Direct imports of database models into UI components or tight coupling without interfaces. | Can a subsystem or service be unit tested in isolation without spinning up third-party services? |
| **Naming & Cognitive Hygiene** | Ambiguous names (`data`, `temp`, `manager`, `process`), magic numbers, cryptic acronyms. | Are names intent-revealing and domain-specific? Are constants centralized and descriptive? |
| **Function Ergonomics** | Long parameter lists (>4 arguments), deep nesting (>3 indentation levels), flag arguments. | Are functions short, focused on one action, and taking typed configuration/DTO objects? |
| **Defensive Error Handling** | Swallowed exceptions (`except: pass`, empty `catch`), generic error returns, lack of context. | Are errors typed, logged with actionable context, and handled at appropriate architectural boundaries? |

---

## Phase 4: README & Documentation Ground-Truth Verification

Audit project documentation against the actual codebase using the **Parity Verification Matrix**:

1. **Setup & Installation Verification:**
   - Review prerequisite versions (Node, Python, Go, Docker) declared in `README.md`.
   - Verify listed commands (`pip install`, `npm install`, setup scripts) against actual manifests.
2. **Environment Configuration:**
   - Compare all environment variable keys documented in `README.md` against `.env.example` and codebase references (`process.env`, `os.getenv`).
   - Flag missing, renamed, or obsolete environment keys.
3. **Directory Tree & Feature Claims:**
   - Compare the directory tree diagram in `README.md` with the physical filesystem.
   - Cross-examine feature claims: does each claimed capability correspond to active, functional code?
   - Flag documented CLI arguments, options, or endpoints that no longer exist or have changed signatures.

---

## Phase 5: Test Suite & Verification Integrity

1. **Assertion Strength Audit:**
   - Check if tests contain meaningful assertions (`expect(...)`, `assert ...`) or simply call methods to achieve test coverage without validating side effects or outputs.
2. **Edge Case & Error Path Coverage:**
   - Verify whether invalid inputs, network failures, timeouts, and boundary conditions are tested alongside the happy path.
3. **Test Hygiene & Mocking Balance:**
   - Flag "mock-everything" tests that mock away the actual code under test.
   - Locate disabled (`.skip`, `xit`), commented-out, or orphaned test files that never run in CI.

---

## Phase 6: Codebase Health Score & Deliverable Schema

Calculate the **Codebase Health Score (0–100)**:

```text
Health Score = (Architecture & SoC [0–25]) 
             + (Clean Code & Hygiene [0–25]) 
             + (Dead / Orphan Code Cleanness [0–20]) 
             + (README & Doc Parity [0–15]) 
             + (Test Suite Integrity [0–15])
```

### Standard Output Schema:
1. **Executive Summary & Health Score (0–100):** High-level verdict with breakdown across all 5 dimensions.
2. **Findings Table:**
   - Columns: `Severity (Critical | High | Medium | Low)` · `Location (file#line)` · `Smell / Anti-pattern` · `Rule / Principle` · `Remediation`
3. **Orphan & Dead Assets List:** Concrete list of unreferenced files, dead functions, and zombie dependencies.
4. **README Parity Diff:** Table of documented claim vs. code reality with suggested markdown corrections.
5. **Prioritized Action Plan:** Sequenced fixes (P0 to P3) including concrete refactoring snippets or diffs.
