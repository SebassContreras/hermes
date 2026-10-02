"""Sync this repo's agents and skills into the local Hermes Agent install (Hermes Desktop).

Hermes injects only <profile>/SOUL.md into the system prompt; AGENT.md / AGENTS.md are never loaded.
Each agent's SOUL.md + AGENT.md is therefore compiled into its profile's SOUL.md with the same
assembly agents/runner.py uses. Toolsets, config keys, profile descriptions and official skills come
from config/hermes_desktop.yaml. Every step is idempotent: unchanged settings are left alone.

Usage:
    python scripts/sync_hermes.py --dry-run   # show what would change
    python scripts/sync_hermes.py             # apply
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, List, Optional

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "agents"))
from prompt_assembly import assemble_system_prompt  # noqa: E402

MANIFEST = REPO / "config" / "hermes_desktop.yaml"
ORCHESTRATOR_PROFILE = "default"


def find_hermes_home() -> Path:
    if os.getenv("HERMES_HOME"):
        return Path(os.environ["HERMES_HOME"])
    local_appdata = os.getenv("LOCALAPPDATA")
    if local_appdata and (Path(local_appdata) / "hermes").is_dir():
        return Path(local_appdata) / "hermes"
    return Path.home() / ".hermes"


class Hermes:
    def __init__(self, home: Path, dry_run: bool):
        self.home = home
        self.dry_run = dry_run
        exe = home / "bin" / ("hermes.exe" if os.name == "nt" else "hermes")
        self.exe = str(exe) if exe.exists() else shutil.which("hermes")
        if not self.exe:
            sys.exit(f"Hermes CLI not found under {home / 'bin'} or on PATH.")

    def run(self, profile: str, *args: str, mutate: bool = True) -> str:
        cmd = [self.exe] + (["-p", profile] if profile != ORCHESTRATOR_PROFILE else []) + list(args)
        if mutate and self.dry_run:
            print(f"    would run: hermes {' '.join(cmd[1:])}")
            return ""
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                env=env, timeout=180)
        if result.returncode != 0:
            raise RuntimeError(f"hermes {' '.join(cmd[1:])} failed:\n{result.stdout}{result.stderr}")
        return result.stdout

    def profile_dir(self, profile: str) -> Path:
        return self.home if profile == ORCHESTRATOR_PROFILE else self.home / "profiles" / profile

    def config_get(self, profile: str, key: str) -> Any:
        """Resolved value, or None when the key is unset (the CLI exits 1)."""
        try:
            return yaml.safe_load(self.run(profile, "config", "get", key, mutate=False))
        except (RuntimeError, yaml.YAMLError):
            return None

    def config_set(self, profile: str, key: str, value: Any) -> None:
        if self.config_get(profile, key) == value:
            return
        print(f"  [{profile}] {key} = {json.dumps(value)}")
        self.run(profile, "config", "set", key, json.dumps(value) if isinstance(value, list) else str(value))

    def config_unset(self, profile: str, key: str) -> None:
        if self.config_get(profile, key) is None:
            return
        print(f"  [{profile}] unset {key}")
        self.run(profile, "config", "unset", key)


def sync_soul(hermes: Hermes, profile: str, agent: str) -> None:
    """Compile agents/<agent>/SOUL.md + AGENT.md into the profile's SOUL.md."""
    compiled = assemble_system_prompt(REPO / "agents" / agent) + "\n"
    target = hermes.profile_dir(profile) / "SOUL.md"
    if not target.parent.is_dir():
        sys.exit(f"Hermes profile '{profile}' does not exist ({target.parent}). Create it in Hermes Desktop first.")
    if target.exists() and target.read_text(encoding="utf-8") == compiled:
        return
    print(f"  [{profile}] SOUL.md <- agents/{agent} ({len(compiled)} chars)")
    if hermes.dry_run:
        return
    if target.exists():
        backup_dir = hermes.home / "backups" / "soul"
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target, backup_dir / f"{profile}-SOUL.md.{time.strftime('%Y%m%d-%H%M%S')}")
    # Write a new file and swap it in: never write through a hard link back into the repo.
    tmp = target.with_suffix(".md.sync-tmp")
    tmp.write_text(compiled, encoding="utf-8")
    os.replace(tmp, target)


def sync_description(hermes: Hermes, profile: str, description: str) -> None:
    meta_file = hermes.profile_dir(profile) / "profile.yaml"
    meta = yaml.safe_load(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
    if (meta or {}).get("description") == description:
        return
    print(f"  [{profile}] description updated")
    hermes.run(ORCHESTRATOR_PROFILE, "profile", "describe", profile, "--text", description)


def sync_toolsets(hermes: Hermes, toolsets: List[str]) -> None:
    enabled = hermes.config_get(ORCHESTRATOR_PROFILE, "platform_toolsets.cli") or []
    for toolset in toolsets:
        if toolset not in enabled:
            print(f"  [{ORCHESTRATOR_PROFILE}] enable toolset {toolset}")
            hermes.run(ORCHESTRATOR_PROFILE, "tools", "enable", toolset)


def sync_official_skills(hermes: Hermes, identifiers: List[str]) -> None:
    for identifier in identifiers:
        name = identifier.rstrip("/").rsplit("/", 1)[-1]
        if any((hermes.home / "skills").glob(f"**/{name}/SKILL.md")):
            continue
        print(f"  [{ORCHESTRATOR_PROFILE}] install skill {identifier}")
        hermes.run(ORCHESTRATOR_PROFILE, "skills", "install", identifier, "--yes")


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="print changes without applying them")
    args = parser.parse_args(argv)

    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    hermes = Hermes(find_hermes_home(), args.dry_run)
    skills_dir = (REPO / manifest["skills_dir"]).resolve().as_posix()
    orchestrator = manifest["orchestrator"]
    print(f"Hermes home: {hermes.home}{'  (dry run)' if args.dry_run else ''}")

    print("Orchestrator (default profile)")
    sync_soul(hermes, ORCHESTRATOR_PROFILE, orchestrator["agent"])
    sync_toolsets(hermes, orchestrator.get("enable_toolsets", []))
    hermes.config_set(ORCHESTRATOR_PROFILE, "skills.external_dirs", [skills_dir])
    for key, value in orchestrator.get("config", {}).items():
        hermes.config_set(ORCHESTRATOR_PROFILE, key, value)
    sync_official_skills(hermes, orchestrator.get("official_skills", []))

    for profile, description in manifest["profiles"].items():
        print(f"Specialist {profile}")
        sync_soul(hermes, profile, profile)
        hermes.config_set(profile, "skills.external_dirs", [skills_dir])
        for key, value in manifest.get("profile_config", {}).items():
            hermes.config_set(profile, key, value)
        for key in manifest.get("profile_config_unset", []):
            hermes.config_unset(profile, key)
        sync_description(hermes, profile, " ".join(description.split()))

    print("Done. Start a new chat in Hermes Desktop so the new prompts and tools load.")


if __name__ == "__main__":
    main()
