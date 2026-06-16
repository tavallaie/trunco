import warnings

import trunco.zbuild as _zbuild

warnings.warn(
    "trunco.franken is deprecated; Franken UI has rebranded to 0build. Use trunco.zbuild instead.",
    DeprecationWarning,
    stacklevel=2,
)

# Re-export zbuild short names under deprecated franken namespace.
Button = _zbuild.Button
Card = _zbuild.Card
Input = _zbuild.Input
Form = _zbuild.Form
FormControl = _zbuild.FormControl
Alert = _zbuild.Alert
Badge = _zbuild.Badge

FrankenButton = Button
FrankenCard = Card
FrankenInput = Input
FrankenForm = Form
FrankenAlert = Alert
FrankenBadge = Badge

uikit_css_tag = _zbuild.kit_css_tag
uikit_js_tag = _zbuild.zuikit_script_tag

__all__ = [
    "Button",
    "Card",
    "Input",
    "Form",
    "FormControl",
    "Alert",
    "Badge",
    "FrankenButton",
    "FrankenCard",
    "FrankenInput",
    "FrankenForm",
    "FrankenAlert",
    "FrankenBadge",
    "uikit_css_tag",
    "uikit_js_tag",
]
