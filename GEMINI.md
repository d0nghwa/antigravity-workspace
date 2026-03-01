---
description: Always used for developing software. This file describes coding best practices, style guidelines, and specifications for all software development.
paths:
 - "src/**/*.ts"
 - "src/**/*.py"
---
# Style guide
Guidelines for writing software.

## Formatting
- Do not exceed 80 characters per line.

## General style
- Generally avoid deep nesting in code (>4 levels). Deep nesting indicates that helper methods should be used.
- Avoid using "magic numbers" directly in the code; use named constants instead.
- Methods should be less than 30 lines (ideally).
- Consider refactoring large functions, classes, or methods into smaller well- defined helper methods.
- Avoid duplicating code. If more than 3 lines are repeated, create a helper.
- Methods should have clear and descriptive names.
- Avoid in-line comments, except to document code that cannot be explained using clear variable names, such as complex regex or mathematical expressions.
- Never use comments to denote sections in code. Logic should be clear without sectioning.
- Use DSLs when possible. For example, when defining database tables, prefer SQL schema files over using Python string queries.
- Use match/switch-case statements instead of long `if-elif-else` chains.
- Never use inline imports. Imports should always be placed at the beginning of a module.

## Typing
- Always use type hints for Python. Avoid using `Any` unless with rare generics code.
- Use modern Python type hint syntax (Python 3.12+).
- Use `T | None` instead of `Optional[T]`. Never use `Optional`.
- Use `X | Y` instead of `Union[X, Y]`.
- Use built-in generics such as `list[str]`, `dict[str, int]`. Do not use `Tuple` or `Dict`.
- Use specific return types (not `tuple`, use `tuple[Path, int]`)
- For dict values with structure, define a dataclass

## Complex types
- If a type signature is complex, repeated, or hard to read, extract it into a named type/type alias.
- Consolidate method parameters into a single `TypedDict`, `NamedTuple` or a  dataclass when there are 3+ fields that are repeated in multiple signatures.

## Error handling
- Logic should fail-fast. Never silently continue or produce incomplete results.
- Distinguish between different error conditions. For example, server HTTP errors may be transient, but client errors should generally not be re-attempted. 
- Re-raise exceptions that indicate bugs or missing tools.
- Return `False` or `None` only for legitimate "not found" cases.
- Use `from e` to preserve exception chains.

## External services
- Database accesses should never cause incomplete intermediate results. Accesses should be serialised and encapsulated correctly.
- Validate that operations actually succeeded. Don't assume. Validate that files exist, files are non-empty when they shouldn't be, etc.

## Specification styles
- A specification should give enough information to write a call to the function without reading the function’s code. Specifications define the behaviour of outputs given inputs, and define the interface for usage. Specifications should document behaviour, not underlying implementation details.
- Important details of a function’s implementation that are not relevant to the caller should be comments alongside the code rather than in the specification, such as bug workarounds, regex, etc.
- Specify pre-/post-conditions. For example, if a method's implementation assumes that a string is a valid UUID string, then that is a pre-condition.
- Specifications should only expose side effects that affect other specified functionality, such as thread-safety, database/cache transaction handling, error handling, etc.
- Do not expose internal implementation details that are irrelevant to the interface, such as specific libraries, frameworks, or logic used.
- All methods, modules, classes, and variables must have specifications, regardless of visibility (public, private, etc.).
- You should not document exceptions that get raised if the API specified in the docstring is violated.
- Use plain english: complete sentences and punctuation.

Example:
```python
def add_user(username: str, email: str) -> User:

# bad specification
"""
Adds SQLAlchemy to add the user to the database. 

Pre-condition: `username` must be non-empty.
"""

# good specification
"""Adds a user to the database.

Creates and commits a new user entry to the database, or rolls back if the operation fails.

Args:
    username: The username of the user to add. Must be non-empty, and consist
        of only alphanumeric characters and underscores.
    email: The email of the user to add. Must be a valid email address.

Returns:
    The user that was added to the database with the given username and email.
```

# Checklist
Always ensure that:
- No silent error handling (fail-fast and log).
- Use modern types (`list[T]`, `T | None`, not `List[T]`, `Optional[T]`).
- Complex type signatures extracted.
- No magic numbers or fake estimates.
- Tuples only for simple pairs, dataclasses for structured data.
- No hard-coded project paths (use system defaults or env vars).
- Output validation after critical operations.
- No duplicate code.
- Specific exception handling.
- Methods are less than 30 lines (only exceed when absolutely necessary).
- No in-line comments describing thought process or implementation.
- Double-check all of the styling guidelines.