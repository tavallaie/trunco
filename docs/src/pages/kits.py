from docs.src.catalog import daisy_only_entries, shared_entries, zbuild_only_entries
from docs.src.components import (
    AvailabilityTable,
    CatalogShowcase,
    DocArticle,
    KitBadge,
    Section,
    ShowcaseGrid,
    paragraph,
)
from trunco.base import Component
from trunco.daisy import Badge


def _unique_showcases(entries):
    seen = set()
    blocks = []
    for entry in entries:
        if entry.slug in seen:
            continue
        seen.add(entry.slug)
        blocks.append(CatalogShowcase(entry))
    return blocks


def build():
    shared = _unique_showcases(shared_entries())
    daisy = _unique_showcases(daisy_only_entries())
    zbuild = _unique_showcases(zbuild_only_entries())

    header_badges = Component(tag="div")
    header_badges.add_class("flex")
    header_badges.add_class("flex-wrap")
    header_badges.add_class("gap-2")
    header_badges.add_class("mt-3")
    header_badges.add_child(Badge("26 shared", color="ghost"))
    header_badges.add_child(KitBadge("daisy", "11 DaisyUI only"))
    header_badges.add_child(KitBadge("zbuild", "4 0build only"))

    return DocArticle(
        "Every kit component",
        AvailabilityTable(),
        Section(
            "Shared components",
            paragraph("Switch trunco.daisy ↔ trunco.zbuild — the API stays the same."),
            anchor="shared",
        ),
        ShowcaseGrid(*shared, *daisy, *zbuild),
        lead=(
            "Live previews, source snippets, and availability — "
            "shared components use the same Python names in both kits."
        ),
        breadcrumb=[
            ("Documentation", "index.html"),
            ("Reference", None),
            ("Kit Reference", None),
        ],
        toc=[
            ("shared", "Shared components"),
            ("daisy-only", "DaisyUI only"),
            ("zbuild-only", "0build only"),
        ],
        header_extra=header_badges,
    )
