from trunco.alpine import alpine_script_tag

from .components import DaisyButton, DaisyCard, DaisyInput
from .forms import (
    DaisyCheckbox,
    DaisyFieldset,
    DaisyFileInput,
    DaisyForm,
    DaisyFormControl,
    DaisyLabel,
    DaisyOption,
    DaisyRadio,
    DaisyRadioGroup,
    DaisyRange,
    DaisySelect,
    DaisyTextarea,
    DaisyToggle,
)
from .theme import (
    THEME_NAMES,
    Page,
    Styles,
    Theme,
    available_themes,
    custom_theme_names,
    get_custom_theme,
    get_theme,
    is_custom_theme,
    register_theme,
    set_theme,
    theme,
    theme_css,
    theme_style_tag,
)
from trunco.kits.scheme import ColorScheme
from .ui import (
    DaisyAccordion,
    DaisyAlert,
    DaisyAvatar,
    DaisyBadge,
    DaisyBreadcrumbs,
    DaisyDivider,
    DaisyDropdown,
    DaisyHero,
    DaisyLink,
    DaisyList,
    DaisyLoading,
    DaisyMenu,
    DaisyModal,
    DaisyNavbar,
    DaisyPagination,
    DaisyProgress,
    DaisyStat,
    DaisyTable,
    DaisyTabs,
    DaisyTooltip,
)

# Primary short names — swap kit import to change style system.
Button = DaisyButton
Card = DaisyCard
Input = DaisyInput
Form = DaisyForm
FormControl = DaisyFormControl
Textarea = DaisyTextarea
Select = DaisySelect
Option = DaisyOption
Checkbox = DaisyCheckbox
Radio = DaisyRadio
RadioGroup = DaisyRadioGroup
Label = DaisyLabel
Range = DaisyRange
Toggle = DaisyToggle
FileInput = DaisyFileInput
Fieldset = DaisyFieldset
Link = DaisyLink
Divider = DaisyDivider
Badge = DaisyBadge
Alert = DaisyAlert
Progress = DaisyProgress
Avatar = DaisyAvatar
Breadcrumbs = DaisyBreadcrumbs
Table = DaisyTable
Loading = DaisyLoading
Tooltip = DaisyTooltip
Modal = DaisyModal
Navbar = DaisyNavbar
Tabs = DaisyTabs
Menu = DaisyMenu
List = DaisyList
Hero = DaisyHero
Stat = DaisyStat
Pagination = DaisyPagination
Accordion = DaisyAccordion
Dropdown = DaisyDropdown

__all__ = [
    "Button",
    "Card",
    "Input",
    "Form",
    "FormControl",
    "Textarea",
    "Select",
    "Option",
    "Checkbox",
    "Radio",
    "RadioGroup",
    "Label",
    "Range",
    "Toggle",
    "FileInput",
    "Fieldset",
    "Link",
    "Divider",
    "Badge",
    "Alert",
    "Progress",
    "Avatar",
    "Breadcrumbs",
    "Table",
    "Loading",
    "Tooltip",
    "Modal",
    "Navbar",
    "Tabs",
    "Menu",
    "List",
    "Hero",
    "Stat",
    "Pagination",
    "Accordion",
    "Dropdown",
    "Page",
    "Styles",
    "Theme",
    "theme",
    "set_theme",
    "get_theme",
    "THEME_NAMES",
    "ColorScheme",
    "register_theme",
    "get_custom_theme",
    "is_custom_theme",
    "custom_theme_names",
    "available_themes",
    "theme_css",
    "theme_style_tag",
    "alpine_script_tag",
    # Backward-compatible prefixed names.
    "DaisyButton",
    "DaisyCard",
    "DaisyInput",
    "DaisyForm",
    "DaisyFormControl",
    "DaisyTextarea",
    "DaisySelect",
    "DaisyOption",
    "DaisyCheckbox",
    "DaisyRadio",
    "DaisyRadioGroup",
    "DaisyLabel",
    "DaisyRange",
    "DaisyToggle",
    "DaisyFileInput",
    "DaisyFieldset",
    "DaisyLink",
    "DaisyDivider",
    "DaisyBadge",
    "DaisyAlert",
    "DaisyProgress",
    "DaisyAvatar",
    "DaisyBreadcrumbs",
    "DaisyTable",
    "DaisyLoading",
    "DaisyTooltip",
    "DaisyModal",
    "DaisyNavbar",
    "DaisyTabs",
    "DaisyMenu",
    "DaisyList",
    "DaisyHero",
    "DaisyStat",
    "DaisyPagination",
    "DaisyAccordion",
    "DaisyDropdown",
]