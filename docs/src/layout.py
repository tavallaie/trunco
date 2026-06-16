from typing import List, Tuple, Union

from trunco.base import Component
from trunco.components.script_block import ScriptBlock
from trunco.components.stylesheet import Stylesheet
from trunco.alpine import alpine_script_tag
from trunco.htmx import htmx_script_tag

NAV_SECTIONS: List[Tuple[str, List[Tuple[str, str]]]] = [
    (
        "Getting Started",
        [
            ("Home", "index.html"),
            ("Installation", "installation.html"),
            ("Quickstart", "quickstart.html"),
        ],
    ),
    (
        "Reference",
        [
            ("Components", "components.html"),
            ("Kit Reference", "kits.html"),
            ("Themes", "themes.html"),
        ],
    ),
    (
        "More",
        [
            ("Integrations", "integrations.html"),
        ],
    ),
]

DOC_SCRIPTS = """
function initCodePanels(root) {
  const scope = root || document;
  scope.querySelectorAll(".code-panel").forEach((panel) => {
    const header = panel.querySelector(".code-panel-header");
    const code = panel.querySelector("code");
    if (!header || !code) return;
    const old = header.querySelector(".code-copy-btn");
    if (old) old.remove();
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "code-copy-btn";
    btn.textContent = "Copy";
    btn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(code.innerText);
        btn.textContent = "Copied!";
        btn.classList.add("copied");
        setTimeout(() => {
          btn.textContent = "Copy";
          btn.classList.remove("copied");
        }, 1500);
      } catch (_) {
        btn.textContent = "Failed";
        setTimeout(() => { btn.textContent = "Copy"; }, 1500);
      }
    });
    header.appendChild(btn);
  });
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("trunco-doc-theme", theme);
  const btn = document.getElementById("theme-toggle");
  if (btn) btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
}

function initThemeToggle() {
  const btn = document.getElementById("theme-toggle");
  if (!btn || btn.dataset.ready) return;
  btn.dataset.ready = "1";
  const saved = localStorage.getItem("trunco-doc-theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  applyTheme(saved || (prefersDark ? "dark" : "light"));
  btn.addEventListener("click", () => {
    const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(next);
  });
}

function syncNav() {
  const page = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".doc-nav-link").forEach((a) => {
    a.classList.toggle("active", a.getAttribute("href") === page);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initCodePanels();
  initThemeToggle();
});
document.body.addEventListener("htmx:afterSwap", (e) => {
  if (e.detail.target.id !== "main-content") return;
  initCodePanels(e.detail.target);
  syncNav();
  if (window.Alpine) Alpine.initTree(e.detail.target);
  const drawer = document.getElementById("doc-drawer");
  if (drawer) drawer.checked = false;
});
"""


def _htmx_nav_link(label: str, href: str, active: str) -> Component:
    link = Component(tag="a")
    link.add_class("doc-nav-link")
    link.add_attribute("href", href)
    link.add_child(label)
    link.add_attribute("hx-get", f"fragments/{href}")
    link.add_attribute("hx-target", "#main-content")
    link.add_attribute("hx-swap", "innerHTML show:window:top")
    link.add_attribute("hx-push-url", href)
    link.add_attribute("hx-indicator", "#htmx-progress")
    if href == active:
        link.add_class("active")
    return link


def _sidebar(active: str) -> Component:
    aside = Component(tag="aside")
    aside.add_class("doc-sidebar")
    inner = Component(tag="div")
    inner.add_class("doc-sidebar-inner")

    for section_label, items in NAV_SECTIONS:
        label = Component(tag="p")
        label.add_class("sidebar-section-label")
        label.add_child(section_label)
        inner.add_child(label)

        menu = Component(tag="ul")
        menu.add_class("doc-sidebar-menu")
        for item_label, href in items:
            li = Component(tag="li")
            li.add_child(_htmx_nav_link(item_label, href, active))
            menu.add_child(li)
        inner.add_child(menu)

    aside.add_child(inner)
    return aside


def doc_page(
    title: str,
    content: Union[Component, str],
    *,
    description: str = "Trunco — Python HTML components",
    active: str = "index.html",
    theme: str = "light",
) -> str:
    """Build a documentation page shell (Hextra-style layout)."""
    page_title = f"{title} · Trunco"
    content_html = content.render() if isinstance(content, Component) else str(content)

    progress = Component(tag="div")
    progress.add_attribute("id", "htmx-progress")
    progress.add_class("htmx-indicator")
    progress.add_class("htmx-progress")

    navbar = Component(tag="header")
    navbar.add_class("doc-navbar")
    navbar_inner = Component(tag="div")
    navbar_inner.add_class("doc-navbar-inner")

    nav_start = Component(tag="div")
    nav_start.add_class("doc-navbar-start")

    drawer_btn = Component(tag="label")
    drawer_btn.add_attribute("for", "doc-drawer")
    drawer_btn.add_class("btn")
    drawer_btn.add_class("btn-square")
    drawer_btn.add_class("btn-ghost")
    drawer_btn.add_class("btn-sm")
    drawer_btn.add_class("lg:hidden")
    drawer_btn.add_attribute("aria-label", "Menu")
    drawer_btn.add_child(
        '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" '
        'viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" '
        'stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>'
    )
    nav_start.add_child(drawer_btn)

    brand = Component(tag="a")
    brand.add_class("doc-brand")
    brand.add_attribute("href", "index.html")
    brand.add_attribute("hx-get", "fragments/index.html")
    brand.add_attribute("hx-target", "#main-content")
    brand.add_attribute("hx-swap", "innerHTML show:window:top")
    brand.add_attribute("hx-push-url", "index.html")
    brand.add_attribute("hx-indicator", "#htmx-progress")
    brand.add_child(
        '<span class="doc-brand-mark">T</span><span class="doc-brand-name">Trunco</span>'
    )
    nav_start.add_child(brand)

    doc_link = Component(tag="a")
    doc_link.add_class("doc-navbar-link")
    doc_link.add_class("doc-navbar-link--active")
    doc_link.add_class("hidden")
    doc_link.add_class("md:inline-flex")
    doc_link.add_attribute("href", "index.html")
    doc_link.add_attribute("hx-get", "fragments/index.html")
    doc_link.add_attribute("hx-target", "#main-content")
    doc_link.add_attribute("hx-swap", "innerHTML show:window:top")
    doc_link.add_attribute("hx-push-url", "index.html")
    doc_link.add_attribute("hx-indicator", "#htmx-progress")
    doc_link.add_child("Documentation")
    nav_start.add_child(doc_link)
    navbar_inner.add_child(nav_start)

    nav_end = Component(tag="div")
    nav_end.add_class("doc-navbar-end")

    theme_btn = Component(tag="button")
    theme_btn.add_attribute("type", "button")
    theme_btn.add_attribute("id", "theme-toggle")
    theme_btn.add_class("doc-theme-toggle")
    theme_btn.add_attribute("aria-label", "Toggle dark mode")
    theme_btn.add_child(
        '<svg class="doc-theme-icon doc-theme-icon--sun" xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5.64,17l-.71.71a1,1,'
        "0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4"
        "A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,"
        "1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.63,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,"
        "1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,"
        "0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,"
        "1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,"
        '1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"/></svg>'
        '<svg class="doc-theme-icon doc-theme-icon--moon" xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.64,13a1,1,0,0,0-1.05-.14,'
        "8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,"
        '0,1,0,22,14.05,1,1,0,0,0,21.64,13Z"/></svg>'
    )
    nav_end.add_child(theme_btn)

    github = Component(tag="a")
    github.add_class("doc-github-badge")
    github.add_attribute("href", "https://github.com/alitavakoli/trunco")
    github.add_attribute("target", "_blank")
    github.add_attribute("rel", "noopener")
    github.add_attribute("aria-label", "View on GitHub")
    github.add_child(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23'
        "-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945"
        "-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335"
        "-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405"
        " 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225"
        " 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57"
        'A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg><span>GitHub</span>'
    )
    nav_end.add_child(github)
    navbar_inner.add_child(nav_end)
    navbar.add_child(navbar_inner)

    main = Component(tag="main")
    main.add_attribute("id", "main-content")
    main.add_child(content_html)

    drawer_content = Component(tag="div")
    drawer_content.add_class("drawer-content")
    drawer_content.add_class("doc-layout")
    drawer_content.add_child(main)

    drawer_side = Component(tag="div")
    drawer_side.add_class("drawer-side")
    drawer_side.add_class("doc-drawer-side")
    overlay = Component(tag="label")
    overlay.add_attribute("for", "doc-drawer")
    overlay.add_class("drawer-overlay")
    overlay.add_attribute("aria-label", "Close")
    drawer_side.add_child(overlay)
    drawer_side.add_child(_sidebar(active))

    drawer_toggle = Component(tag="input")
    drawer_toggle.add_attribute("type", "checkbox")
    drawer_toggle.add_attribute("id", "doc-drawer")
    drawer_toggle.add_class("drawer-toggle")

    drawer = Component(tag="div")
    drawer.add_class("drawer")
    drawer.add_class("lg:drawer-open")
    drawer.add_child(drawer_toggle)
    drawer.add_child(drawer_content)
    drawer.add_child(drawer_side)

    body = Component(tag="div")
    body.add_child(progress)
    body.add_child(navbar)
    body.add_child(drawer)

    custom_css = Stylesheet("assets/style.css")
    doc_scripts = ScriptBlock(content=DOC_SCRIPTS)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="{description}" />
  <title>{page_title}</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  {custom_css.render()}
  {htmx_script_tag()}
</head>
<body class="doc-body">
{body.render()}
{doc_scripts.render()}
{alpine_script_tag()}
</body>
</html>"""


DocPage = type("DocPage", (), {"build": staticmethod(doc_page)})
