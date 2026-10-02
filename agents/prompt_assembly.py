"""System prompt assembly shared by runner.py and scripts/sync_hermes.py (no third-party deps)."""

from pathlib import Path
from typing import List


def assemble_system_prompt(agent_dir: str | Path) -> str:
    """Assembles system prompt following AGENT.md / SOUL.md hierarchy."""
    agent_dir = Path(agent_dir)
    prompt_parts: List[str] = []

    soul_file = agent_dir / "SOUL.md"
    agent_file = agent_dir / "AGENT.md"
    legacy_prompt = agent_dir / "prompt.md"

    if soul_file.exists():
        prompt_parts.append(soul_file.read_text(encoding="utf-8").strip())

    if agent_file.exists():
        prompt_parts.append(agent_file.read_text(encoding="utf-8").strip())

    if not prompt_parts and legacy_prompt.exists():
        prompt_parts.append(legacy_prompt.read_text(encoding="utf-8").strip())

    if not prompt_parts:
        raise FileNotFoundError(
            f"No prompt configuration found in {agent_dir}. "
            "Expected SOUL.md, AGENT.md, or prompt.md."
        )

    return "\n\n---\n\n".join(prompt_parts)
