# Commit Examples

## By Type

### feat
```
feat(auth): add OAuth2 login flow
feat(api): expose bulk-delete endpoint
feat(cache): implement LRU eviction policy
```

### fix
```
fix(session): prevent token refresh race condition
fix(api): return 404 instead of 500 for missing user
fix(ingestion): handle empty document chunks gracefully
```

### docs
```
docs(readme): add deployment prerequisites
docs(api): document rate-limiting headers
```

### refactor
```
refactor(service): extract query builder into helper
refactor(agent): replace if-elif chain with dispatch map
```

### perf
```
perf(embedding): batch requests to reduce round trips
perf(search): add index on document_id column
```

### test
```
test(auth): add integration tests for token refresh
test(cache): cover TTL expiration edge cases
```

### build / ci
```
build(docker): pin base image to python:3.10-slim
ci(github): add ruff lint step to PR workflow
```

### chore
```
chore(deps): bump pydantic to 2.6.0
chore(config): remove deprecated env vars
```

### security
```
security(api): sanitize user input in search query
security(auth): enforce constant-time token comparison
```

## Multi-line Example

```bash
git commit -m "$(cat <<'EOF'
refactor(agent): replace if-elif chain with dispatch map

Simplify tool routing by mapping tool names to handler
functions instead of a growing conditional block.

- Reduces cyclomatic complexity from 12 to 3
- Makes adding new tools a single-line change
EOF
)"
```

## Good vs Bad

### Bad
```
fix: stuff                          # no scope, vague subject
updated the login page              # no type, no scope, past tense
feat(auth): Add OAuth2 login flow.  # capitalised verb, trailing period
fix(db): fix the database query that was causing issues with user lookup
                                    # exceeds 50 chars, redundant "fix" in subject
chore: changes                      # no scope, generic
```

### Good
```
fix(login): prevent duplicate form submission
feat(auth): add OAuth2 login flow
chore(deps): bump pydantic to 2.6.0
security(api): sanitize search query parameters
```
