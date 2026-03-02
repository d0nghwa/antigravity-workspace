---
name: sync-instructions
description: Pull the latest coding instructions from the upstream git repository and deploy them to the active editor's configuration path.
disable-model-invocation: true
---

# Sync Instructions

Pull the latest coding instructions from the upstream repository and deploy them to the correct editor configuration path based on which AI model is running.

## Steps

Execute the deterministic synchronization Python script. You must pass your identity as an argument (e.g., `claude`, `gemini`, `copilot`, `antigravity`).

Run:
```sh
python ~/<skills directory>/skills/sync-instructions/sync.py <agent_identity>
```

Example invocation if you are GitHub Copilot:
```sh
python ~/.claude/skills/sync-instructions/sync.py copilot
```
If you are Google Antigravity:
```sh
python ~/.gemini/skills/sync-instructions/sync.py antigravity
```

This script will autonomously handle:
1. Fetching the latest upstream configurations.
2. Locating your specific instruction configuration file (handling OS-specific paths and IDE-specific paths).
3. Copying the system prompts/instructions and any hooks or skills.
4. Verifying and printing the deployed commit hash.