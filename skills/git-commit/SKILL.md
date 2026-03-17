---
name: git-commit
description: "Creates git commits following Conventional Commits format with type/scope/subject. Use when: user wants to commit changes, create commit, save work, stage and commit, or review staged changes before committing. Enforces project-specific conventions from CLAUDE.md."
---

# Git Commit

Creates git commits following Conventional Commits format.

## Recent project commits

!`git log --oneline -5 2>/dev/null`

## Quick Start

```bash
# 1. Stage changes
git add <files>

# 2. Create commit
git commit -m "type(scope): subject"
```

## Procedure

1. **Check project conventions**: Read `CLAUDE.md` or similar project config for commit format overrides.
2. **Review staged changes**: Run `git diff --cached --stat` to understand what's being committed.
3. **Determine type**: Pick the commit type from the table below.
4. **Determine scope**: Identify the area of the codebase affected (kebab-case).
5. **Write subject**: Present tense imperative verb, under 50 chars, no trailing period.
6. **Add body** (if needed): Use HEREDOC format for multi-line commits.
7. **Commit**: Stage and commit the changes.

## Commit Types

| Type | When |
|------|------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructuring (no feature/fix) |
| `perf` | Performance improvement |
| `test` | Adding or updating tests |
| `build` | Build system or dependencies |
| `ci` | CI/CD configuration |
| `chore` | Maintenance tasks |
| `security` | Vulnerability fixes or hardening |

## Project Conventions

- Scope is optional (kebab-case): `validation`, `auth`, `cookie-service`, `api`.
- Additional type beyond standard CC: `security` (vulnerability fixes or hardening).
- HEREDOC for multi-line commits:

```bash
git commit -m "$(cat <<'EOF'
feat(validation): add URLValidator with domain whitelist

Implement URLValidator class supporting:
- Domain whitelist enforcement
- Dangerous scheme blocking

Addresses Requirement 31
Part of Task 5.1
EOF
)"
```

## Rules

- **ALWAYS** check CLAUDE.md conventions first — use project format if it differs.
- **ALWAYS** include scope in parentheses.
- **ALWAYS** use present tense imperative verb for the subject.
- **NEVER** end subject with a period.
- **NEVER** exceed 50 chars in the subject line.
- **NEVER** use generic messages ("update code", "fix bug", "changes").
- **NEVER** include `Co-Authored-By` trailers.
- Group related changes into a single focused commit.

## References

- [Extended examples by type, good/bad comparisons](./references/commit_examples.md)
