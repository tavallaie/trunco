from enum import Enum


class Trigger(Enum):
    """Event triggers for HTMX-driven components."""

    CLICK = "click"
    LOAD = "load"
    CHANGE = "change"
    DBLCLICK = "dblclick"
    MOUSEOVER = "mouseover"
    MOUSEOUT = "mouseout"
    INPUT = "input"
    SUBMIT = "submit"


class Swap(Enum):
    """HTMX swap strategies."""

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