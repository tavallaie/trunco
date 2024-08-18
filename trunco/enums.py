from enum import Enum


class Directive(Enum):
    """
    Enum for common directives used in components.
    This can be extended to include more directives as needed.
    """

    X_DATA = "x-data"
    X_SHOW = "x-show"
    X_INIT = "x-init"
    X_ON_CLICK = "x-on:click"
    X_TEXT = "x-text"
    X_HTML = "x-html"
    X_IF = "x-if"
    X_FOR = "x-for"


class Trigger(Enum):
    """
    Enum for event triggers, commonly used in HTMX or other event-driven components.
    """

    CLICK = "click"
    LOAD = "load"
    CHANGE = "change"
    DBLCLICK = "dblclick"
    MOUSEOVER = "mouseover"
    MOUSEOUT = "mouseout"
    INPUT = "input"
    SUBMIT = "submit"


class Attribute(Enum):
    """
    Enum for custom HTML attributes that can be used across components.
    This can help standardize attribute names.
    """

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


class Method(Enum):
    """
    Enum for standard HTML form methods.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Swap(Enum):
    """
    Enum for HTMX swap strategies.
    """

    INNER_HTML = "innerHTML"
    OUTER_HTML = "outerHTML"
    BEFORE_BEGIN = "beforebegin"
    AFTER_BEGIN = "afterbegin"
    BEFORE_END = "beforeend"
    AFTER_END = "afterend"


class HxMethod:
    @staticmethod
    def get(url: str):
        return "hx-get", url

    @staticmethod
    def post(url: str):
        return "hx-post", url

    @staticmethod
    def put(url: str):
        return "hx-put", url

    @staticmethod
    def delete(url: str):
        return "hx-delete", url

    @staticmethod
    def patch(url: str):
        return "hx-patch", url
