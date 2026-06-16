from . import (
    components,
    index,
    installation,
    integrations,
    kits,
    quickstart,
    themes,
)

PAGES = [
    ("index", "Home", index.build),
    ("installation", "Installation", installation.build),
    ("quickstart", "Quickstart", quickstart.build),
    ("components", "Components", components.build),
    ("kits", "Component Reference", kits.build),
    ("themes", "Themes", themes.build),
    ("integrations", "Integrations", integrations.build),
]

__all__ = ["PAGES"]