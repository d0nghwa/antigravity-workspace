import sys
import subprocess
import shutil
import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Sync AI coding instructions, skills, and hooks from the upstream "
            "repository."
        )
    )
    parser.add_argument(
        "agent",
        type=str,
        choices=["claude", "copilot", "antigravity"],
        help=(
            "The identity of the AI agent running the script (e.g., claude, "
            "copilot, antigravity)."
        ),
    )
    parser.add_argument(
        "--repo-dir",
        type=Path,
        default=Path.home() / "projects" / "instructions",
        help="Path to the instructions repository.",
    )
    return parser.parse_args()


def pull_upstream(repo_dir: Path) -> None:
    """Pulls the latest changes from the upstream repository."""
    print("Pulling upstream...")
    try:
        subprocess.run(
            ["git", "-C", str(repo_dir), "pull", "origin", "main"], check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Git pull failed: {e}")
        sys.exit(1)


def get_config_paths(agent_name: str) -> list[Path]:
    """Returns the target configuration paths based on the agent and OS."""
    home = Path.home()
    paths = []

    if agent_name == "claude":
        paths.append(home / ".claude" / "CLAUDE.md")
    elif agent_name == "antigravity":
        paths.append(home / ".gemini" / "GEMINI.md")
    elif agent_name == "copilot":
        if sys.platform == "win32":
            paths.append(
                home
                / "AppData"
                / "Roaming"
                / "Code"
                / "User"
                / "prompts"
                / "coding.instructions.md"
            )
        elif sys.platform == "linux":
            paths.append(
                home
                / ".config"
                / "Code"
                / "User"
                / "prompts"
                / "coding.instructions.md"
            )

    return paths


def get_sync_destinations(agent_name: str) -> tuple[Path, Path]:
    """Returns the destinations for skills and hooks directories."""
    home = Path.home()
    if agent_name == "antigravity":
        agent_skills_dir = home / ".gemini" / "antigravity" / "skills"
        agent_hooks_dir = home / ".gemini" / "antigravity" / "hooks"
    else:
        # Every other AI agent uses ~/.claude/...
        agent_skills_dir = home / ".claude" / "skills"
        agent_hooks_dir = home / ".claude" / "hooks"

    return agent_skills_dir, agent_hooks_dir


def deploy_config(src: Path, dests: list[Path]) -> None:
    """Copies the system prompt to the target config paths."""
    if not src.exists():
        print(f"Configuration source file not found: {src}")
        return

    if not dests:
        print("No specific config file path configured for this agent.")
        return

    for config_path in dests:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, config_path)
        print(f"Updated instructions config at: {config_path}")


def sync_directory(src: Path, dst: Path) -> None:
    """Copies a directory from src to dst."""
    if src.exists() and src.is_dir():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Synced {src.name} to {dst}")


def get_git_commit(repo_dir: Path) -> str | None:
    """Retrieves the current git commit hash."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def main():
    args = parse_args()

    repo_dir = args.repo_dir
    system_prompt_src = repo_dir / "system_prompt.md"
    skills_src = repo_dir / "skills"
    hooks_src = repo_dir / "hooks"

    # 1. Pull the latest code
    pull_upstream(repo_dir)

    # 2. Deploy configuration files
    config_paths = get_config_paths(args.agent)
    deploy_config(system_prompt_src, config_paths)

    # 3. Synchronize skills and hooks directories
    agent_skills_dir, agent_hooks_dir = get_sync_destinations(args.agent)
    sync_directory(skills_src, agent_skills_dir)
    sync_directory(hooks_src, agent_hooks_dir)

    # 4. Print success details
    commit_hash = get_git_commit(repo_dir)
    if commit_hash:
        print(f"Successfully deployed commit: {commit_hash}")
    else:
        print("Successfully deployed, but unable to retrieve git commit hash.")


if __name__ == "__main__":
    main()
