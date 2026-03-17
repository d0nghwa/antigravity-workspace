# Workflow

## Always plan
- Use plan mode for all non-trivial tasks (3+ steps or architectural changes)
- If an issue is encountered, stop and re-plan immediately.
- Plan out verification steps.

## Utilise subagents
- Use subagents often to keep the main context window clean.
- If researching, exploring, or analysing, use subagents to offload and parallelise the work.

## Verification
- Never denote completing a task without proving that it works.
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, and prove correctness without guessing.

## Rigour
- For non-trivial tasks: always pause. Ask yourself: "Is there a more elegant way?"
- If a fix/feature seems hacky or fragile, pause and re-iterate.
- Always challenge your own work. When implementing features, always consider the error cases and potential failures.

## Core principles
- Simplicity: Make every change as simple as possible. Less code means less surface area for areas, which means less code to maintain.
- Be meticulous: Don't be lazy; find root causes for issues. No temporary fixes.