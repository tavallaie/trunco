from enum import Enum


class Directive(Enum):
    """Alpine.js directives for reactive component behavior."""

    X_DATA = "x-data"
    X_SHOW = "x-show"
    X_INIT = "x-init"
    X_ON_CLICK = "x-on:click"
    X_TEXT = "x-text"
    X_HTML = "x-html"
    X_IF = "x-if"
    X_FOR = "x-for"
