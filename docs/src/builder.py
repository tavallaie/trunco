import shutil
from pathlib import Path
from typing import Callable, Dict

from .layout import doc_page


class SiteBuilder:
    """Build static HTML documentation into ``docs/_site``."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.pages: Dict[str, Dict] = {}

    def add_page(
        self,
        slug: str,
        title: str,
        content_builder: Callable[[], object],
        *,
        description: str = "Trunco — Python HTML components",
        theme: str = "light",
    ) -> None:
        filename = "index.html" if slug in ("", "index") else f"{slug}.html"
        self.pages[filename] = {
            "title": title,
            "content_builder": content_builder,
            "description": description,
            "theme": theme,
            "active": filename,
        }

    def build(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        assets_src = Path(__file__).parent.parent / "assets"
        assets_dst = self.output_dir / "assets"
        if assets_src.exists():
            if assets_dst.exists():
                shutil.rmtree(assets_dst)
            shutil.copytree(assets_src, assets_dst)

        fragments_dir = self.output_dir / "fragments"
        fragments_dir.mkdir(parents=True, exist_ok=True)

        expected_pages = set(self.pages)
        for path in self.output_dir.glob("*.html"):
            if path.name not in expected_pages:
                path.unlink()
        if fragments_dir.exists():
            for path in fragments_dir.glob("*.html"):
                if path.name not in expected_pages:
                    path.unlink()

        for filename, meta in self.pages.items():
            content = meta["content_builder"]()
            content_html = content.render() if hasattr(content, "render") else str(content)
            (fragments_dir / filename).write_text(content_html, encoding="utf-8")

            html = doc_page(
                meta["title"],
                content,
                description=meta["description"],
                active=meta["active"],
                theme=meta["theme"],
            )
            (self.output_dir / filename).write_text(html, encoding="utf-8")

        (self.output_dir / ".nojekyll").touch(exist_ok=True)