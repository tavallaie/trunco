from importlib import import_module
from typing import Any

from .base import Component
from .enums import Attribute, Method

__version__ = "1.0.0"

__all__ = [
    "Component",
    "Attribute",
    "Method",
    "__version__",
    "Directive",
    "Trigger",
    "HxMethod",
    "Swap",
]

_COMPAT_EXPORTS = {
    "Directive": ("trunco.alpine", "Directive"),
    "Trigger": ("trunco.htmx", "Trigger"),
    "Swap": ("trunco.htmx", "Swap"),
    "HxMethod": ("trunco.htmx", "HxMethod"),
}


def __getattr__(name: str) -> Any:
    if name in _COMPAT_EXPORTS:
        module_name, attr_name = _COMPAT_EXPORTS[name]
        module = import_module(module_name)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")