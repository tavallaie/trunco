from .assets import (
    chart_css_tag,
    chart_script_tag,
    components_script_tag,
    core_script_tag,
    icon_script_tag,
    kit_css_tag,
    runtime_script_tag,
    theme_init_script,
    zuikit_script_tag,
)
from .components import ZbuildButton, ZbuildCard, ZbuildInput
from .forms import (
    ZbuildCheckbox,
    ZbuildFieldset,
    ZbuildForm,
    ZbuildFormField,
    ZbuildLabel,
    ZbuildOption,
    ZbuildRadio,
    ZbuildRadioGroup,
    ZbuildRange,
    ZbuildSelect,
    ZbuildTextarea,
    ZbuildToggleSwitch,
)
from .theme import (
    LAYOUTS,
    MODES,
    PALETTES,
    Page,
    Styles,
    Theme,
    available_palettes,
    custom_palette_names,
    get_custom_palette,
    get_theme,
    is_custom_palette,
    palette_css,
    palette_style_tag,
    register_palette,
    set_theme,
    theme,
)
from trunco.kits.scheme import PaletteScheme
from .ui import (
    ZbuildAccordion,
    ZbuildAccordionGroup,
    ZbuildAlert,
    ZbuildAvatar,
    ZbuildBadge,
    ZbuildBreadcrumb,
    ZbuildDivider,
    ZbuildLink,
    ZbuildModal,
    ZbuildNav,
    ZbuildProgress,
    ZbuildSpinner,
    ZbuildTab,
    ZbuildTable,
    ZbuildTooltip,
)

# Primary short names — swap kit import to change style system.
Button = ZbuildButton
Card = ZbuildCard
Input = ZbuildInput
Form = ZbuildForm
FormControl = ZbuildFormField
Textarea = ZbuildTextarea
Select = ZbuildSelect
Option = ZbuildOption
Checkbox = ZbuildCheckbox
Radio = ZbuildRadio
RadioGroup = ZbuildRadioGroup
Label = ZbuildLabel
Range = ZbuildRange
Toggle = ZbuildToggleSwitch
Fieldset = ZbuildFieldset
Link = ZbuildLink
Badge = ZbuildBadge
Alert = ZbuildAlert
Progress = ZbuildProgress
Avatar = ZbuildAvatar
Breadcrumb = ZbuildBreadcrumb
Table = ZbuildTable
Spinner = ZbuildSpinner
Tooltip = ZbuildTooltip
Modal = ZbuildModal
Nav = ZbuildNav
Tab = ZbuildTab
Accordion = ZbuildAccordion
AccordionGroup = ZbuildAccordionGroup
Divider = ZbuildDivider

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
    "Fieldset",
    "Link",
    "Badge",
    "Alert",
    "Progress",
    "Avatar",
    "Breadcrumb",
    "Table",
    "Spinner",
    "Tooltip",
    "Modal",
    "Nav",
    "Tab",
    "Accordion",
    "AccordionGroup",
    "Divider",
    "Page",
    "Styles",
    "Theme",
    "theme",
    "set_theme",
    "get_theme",
    "PALETTES",
    "LAYOUTS",
    "MODES",
    "PaletteScheme",
    "register_palette",
    "get_custom_palette",
    "is_custom_palette",
    "custom_palette_names",
    "available_palettes",
    "palette_css",
    "palette_style_tag",
    "kit_css_tag",
    "chart_css_tag",
    "core_script_tag",
    "zuikit_script_tag",
    "runtime_script_tag",
    "icon_script_tag",
    "chart_script_tag",
    "components_script_tag",
    "theme_init_script",
    # Backward-compatible prefixed names.
    "ZbuildButton",
    "ZbuildCard",
    "ZbuildInput",
    "ZbuildForm",
    "ZbuildFormField",
    "ZbuildTextarea",
    "ZbuildSelect",
    "ZbuildOption",
    "ZbuildCheckbox",
    "ZbuildRadio",
    "ZbuildRadioGroup",
    "ZbuildLabel",
    "ZbuildRange",
    "ZbuildToggleSwitch",
    "ZbuildFieldset",
    "ZbuildLink",
    "ZbuildBadge",
    "ZbuildAlert",
    "ZbuildProgress",
    "ZbuildAvatar",
    "ZbuildBreadcrumb",
    "ZbuildTable",
    "ZbuildSpinner",
    "ZbuildTooltip",
    "ZbuildModal",
    "ZbuildNav",
    "ZbuildTab",
    "ZbuildAccordion",
    "ZbuildDivider",
]
