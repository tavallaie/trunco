"""Minimal syntax highlighting for documentation code blocks."""

from __future__ import annotations

import re
from html import escape

_PY_KEYWORDS = frozenset(
    {
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "False",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "None",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "True",
        "try",
        "while",
        "with",
        "yield",
    }
)

_BASH_KEYWORDS = frozenset({"export", "cd", "pip", "install", "python", "uv", "git", "clone"})


def _span(css_class: str, text: str) -> str:
    return f'<span class="{css_class}">{text}</span>'


def highlight_python(code: str) -> str:
    """Highlight Python source (input must be HTML-escaped)."""
    tokens: list[str] = []
    index = 0
    length = len(code)

    while index < length:
        char = code[index]

        if char == "#":
            end = code.find("\n", index)
            if end == -1:
                end = length
            tokens.append(_span("cm", code[index:end]))
            index = end
            continue

        if char in "\"'":
            quote = char
            end = index + 1
            while end < length:
                if code[end] == quote and code[end - 1] != "\\":
                    end += 1
                    break
                end += 1
            tokens.append(_span("str", code[index:end]))
            index = end
            continue

        match = re.match(r"[A-Za-z_][A-Za-z0-9_]*", code[index:])
        if match:
            word = match.group(0)
            if word in _PY_KEYWORDS:
                tokens.append(_span("kw", word))
            elif word.startswith("trunco"):
                tokens.append(_span("mod", word))
            else:
                tokens.append(word)
            index += len(word)
            continue

        tokens.append(char)
        index += 1

    return "".join(tokens)


def highlight_bash(code: str) -> str:
    """Highlight shell snippets (input must be HTML-escaped)."""
    lines = []
    for line in code.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("#"):
            lines.append(_span("cm", line))
            continue
        if stripped.startswith("uv ") or stripped.startswith("pip "):
            parts = line.split(None, 2)
            if len(parts) >= 2:
                lines.append(
                    _span("kw", parts[0])
                    + " "
                    + _span("kw", parts[1])
                    + (f" {_span('str', parts[2])}" if len(parts) > 2 else "")
                )
                continue
        if stripped.startswith("git "):
            parts = line.split(None, 2)
            lines.append(
                _span("kw", parts[0])
                + (f" {_span('kw', parts[1])}" if len(parts) > 1 else "")
                + (f" {_span('str', parts[2])}" if len(parts) > 2 else "")
            )
            continue
        for keyword in _BASH_KEYWORDS:
            if re.search(rf"\b{re.escape(keyword)}\b", line):
                line = re.sub(
                    rf"\b({re.escape(keyword)})\b",
                    lambda m: _span("kw", m.group(1)),
                    line,
                )
                break
        lines.append(line)
    return "\n".join(lines)


def highlight_code(code: str, language: str = "python", filename: str | None = None) -> str:
    """Return HTML-safe highlighted code."""
    escaped = escape(code)
    lang = (filename or language or "text").lower()
    if lang.endswith(".py") or lang in ("python", "py", "daisy.py", "zbuild.py"):
        return highlight_python(escaped)
    if lang in ("bash", "sh", "shell", "zsh", "fish"):
        return highlight_bash(escaped)
    return escaped
