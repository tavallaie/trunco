from enum import Enum
from importlib import import_module
from typing import Any


class Attribute(Enum):
    """Standard HTML attributes shared across all Trunco components."""

    HREF = "href"
    SRC = "src"
    ALT = "alt"
    TITLE = "title"
    DISABLED = "disabled"
    VALUE = "value"
    PLACEHOLDER = "placeholder"
    NAME = "name"
    METHOD = "method"
    ACTION = "action"
    TARGET = "target"
    REL = "rel"
    FOR = "for"
    TYPE = "type"
    CHECKED = "checked"
    SELECTED = "selected"
    MIN = "min"
    MAX = "max"
    STEP = "step"
    ROWS = "rows"
    COLS = "cols"
    ROLE = "role"


class Method(Enum):
    """Standard HTML form methods."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


_COMPAT_EXPORTS = {
    "Directive": ("trunco.alpine.enums", "Directive"),
    "Trigger": ("trunco.htmx.enums", "Trigger"),
    "Swap": ("trunco.htmx.enums", "Swap"),
    "HxMethod": ("trunco.htmx.enums", "HxMethod"),
}


def __getattr__(name: str) -> Any:
    if name in _COMPAT_EXPORTS:
        module_name, attr_name = _COMPAT_EXPORTS[name]
        module = import_module(module_name)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")