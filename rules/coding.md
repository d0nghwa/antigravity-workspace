---
description: Always used for developing software. This file describes coding best practices, style guidelines, and specifications for all software development.
paths:
  - "**/*.py"
  - "**/*.ts"
---
# Style guide
Guidelines for writing software.

## General style
- Generally avoid deep nesting in code (>4 levels). Deep nesting indicates that helper methods should be used.
- Avoid using "magic numbers" directly in the code; use named constants instead.
- Methods should be less than 30 lines (ideally).
- Never create large functions, classes, or methods.
- Avoid duplicating code. If more than 3 lines are repeated, create a helper.
- Methods should have clear and descriptive names.
- Avoid in-line comments, except to document code that cannot be explained using clear variable names, such as complex regex or mathematical expressions.
- Never use comments to denote sections in code. Logic should be clear without sectioning.
- Use DSLs when possible. For example, when defining database tables, prefer SQL schema files over using Python string queries.
- Use match/switch-case statements instead of long `if-elif-else` chains.
- Never use inline imports. Imports should always be placed at the beginning of a module.

## Typing
- Always use type annotations. Never omit typing or use `any`/`Any` types unless creating generics code.
- Always use modern union types `X | Y` instead of `Union[X, Y]`.
- Use built-in generics such as `list[str]`, `dict[str, int]`. Never use `Tuple` or `Dict`.
- Use specific return types (not `tuple`, use `tuple[Path, int]`)
- If a type signature is complex, repeated, or hard to read, extract it into a named type/type alias.
- Consolidate method parameters into a single type interface or dataclass when there are 3+ fields that are repeated in multiple signatures.

## Error handling
- Always fail-fast. Never silently continue or produce incomplete results.
- Distinguish between different error conditions. For example, server HTTP errors may be transient, but client errors should generally not be re-attempted. 
- Return `false`/`False` or `null`/`None` only for legitimate "not found" cases, such as non-existent entries.

## External services
- Database accesses should never cause incomplete intermediate results. Accesses should be serialised and encapsulated correctly.
- Validate that operations actually succeeded. Don't assume. Validate that files exist, files are non-empty when they shouldn't be, etc.

## Specification styles
- A specification should give enough information to write a call to the function without reading the function’s code. Specifications should document behaviour, not underlying implementation details.
- Important details of a function’s implementation that are not relevant to the caller should be comments alongside the code rather than in the specification, such as bug workarounds, regex, etc.
- Specify pre-/post-conditions. For example, if a method's implementation assumes that a string is a valid UUID string, then that is a pre-condition.
- Specifications should only expose side effects that affect other specified functionality, such as thread-safety, database/cache transaction handling, error handling, etc.
- All methods, modules, classes, and variables must have specifications, regardless of visibility (public, private, etc.).
- Never document exceptions that get raised if the API specified in the docstring is violated.
- Use plain english: complete sentences and punctuation.

<bad-example>
def add(user, password: Optional[str]):
    """Adds the user to the database. 

    Pre-condition: `username` must be non-empty.
    """
</bad-example>
<better-example>
def add_user(user: str, password: str | None) -> AddResult:
    """Adds a user to the database.

    Creates and commits a new user entry to the database, or rolls back if the
    operation fails.

    Args:
        username: The username of the user to add. Must be non-empty, and
            consist of only alphanumeric characters and underscores.
        email: The email of the user to add. Must be a valid email address.

    Returns:
        The status of adding the user that was added to the database with the 
        given username and email.
    """
</better-example>

# Checklist
Always ensure that:
- No silent error handling (fail-fast and log), specific error handling, and validate outputs.
- Never section code using comments.
- Use modern types (`list[T]`, `T | None`, not `List[T]`, `Optional[T]`).
- Complex type signatures extracted into readable interfaces.
- No magic numbers or fake estimates.
- No hard-coded project paths (use system defaults or env vars).
- No duplicate code, methods are ~30 lines long.