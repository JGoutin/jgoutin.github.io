"""Build orchestrator for the Zensical bilingual site.

Runs the Zensical build for each language, injects JSON-LD and Open Graph
metadata into every generated HTML page, emits ``llms.txt`` and
``llms-full.txt`` for LLM discovery, copies root-level assets (CNAME,
robots.txt, shared images), renders CV PDFs with pandoc + WeasyPrint, and
rasterises the Open Graph image.
"""

import json
import re
import shutil
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, NamedTuple, Self

import cairosvg
import pypandoc
from yaml import safe_dump, safe_load
from zensical import build as zensical_build

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ROOT_SRC = ROOT / "docs" / "_root"
LANGUAGES: tuple[str, ...] = ("en", "fr")
ZENSICAL_OPTS: dict[str, bool] = {"clean": False, "strict": False}

BASE_URL = "https://jgoutin.dev"
OG_IMAGE_URL = f"{BASE_URL}/assets/og-image.png"
OG_WIDTH, OG_HEIGHT = 1200, 630
OG_LOCALES: dict[str, str] = {"en": "en_US", "fr": "fr_FR"}

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)
_HEAD_RE = re.compile(r"(<head[^>]*>)", re.IGNORECASE)
_TITLE_RE = re.compile(r"<title>([^<]*)</title>", re.IGNORECASE)
_DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.IGNORECASE)
_CANONICAL_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]*)"', re.IGNORECASE)
_NO_PRINT_BLOCK_RE = re.compile(
    r'<div[^>]*class="[^"]*no-print[^"]*"[^>]*>.*?</div>', re.DOTALL
)
_NO_PRINT_LINE_RE = re.compile(r"^.*no-print.*$", re.MULTILINE)
_MKDOCS_ONLY_KEYS = frozenset({"hide"})

type NavPage = tuple[str, str, str]  # title, url, source filename
type NavSection = tuple[str, list[NavPage]]  # section name, pages

ORG_SCHEMA: dict[str, Any] = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "JGoutin-dev",
    "description": "Enterprise software solutions for AWS cloud transformation",
    "url": BASE_URL,
    "areaServed": "Worldwide",
    "priceRange": "€€€",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Aix-en-Provence",
        "addressCountry": "FR",
    },
    "serviceType": [
        "Cloud Architecture",
        "AWS Solutions",
        "DevOps Consulting",
        "AI/ML Solutions",
        "Python Development",
    ],
    "sameAs": ["https://github.com/jgoutin", "https://www.linkedin.com/in/jgoutin"],
}
PERSON_SCHEMA: dict[str, Any] = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Jérémy Goutin",
    "jobTitle": "Solutions Architect",
    "worksFor": {"@type": "Organization", "name": "JGoutin-dev", "url": BASE_URL},
    "url": BASE_URL,
    "sameAs": ["https://www.linkedin.com/in/jgoutin", "https://github.com/jgoutin"],
    "knowsAbout": ["AWS", "Python", "DevOps", "AI/LLM", "Cloud architecture"],
}
STDAPI_SCHEMA: dict[str, Any] = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "stdapi.ai",
    "applicationCategory": "DeveloperApplication",
    "operatingSystem": "Any",
    "description": "OpenAI- and Anthropic-compatible API gateway for AWS Bedrock",
    "url": "https://stdapi.ai",
    "offers": {
        "@type": "Offer",
        "price": 0,
        "priceCurrency": "USD",
        "description": "14-day free trial on AWS Marketplace",
    },
    "publisher": {"@type": "Organization", "name": "JGoutin-dev"},
}
PATH_SCHEMAS: tuple[tuple[str, dict[str, Any]], ...] = (
    ("/resume/", PERSON_SCHEMA),
    ("/products/", STDAPI_SCHEMA),
)


@dataclass(frozen=True, slots=True)
class Site:
    """Resolved configuration for one language variant."""

    lang: str
    raw: dict[str, Any]

    @classmethod
    def load(cls, lang: str) -> Self:
        """Parse the ``[project]`` section of the language's TOML config.

        Args:
            lang: Language code (``en`` or ``fr``).

        Returns:
            Frozen :class:`Site` bound to that config.
        """
        with (ROOT / f"zensical.{lang}.toml").open("rb") as f:
            return cls(lang=lang, raw=tomllib.load(f)["project"])

    @property
    def docs_dir(self) -> Path:
        return ROOT / self.raw["docs_dir"]

    @property
    def site_dir(self) -> Path:
        return ROOT / self.raw["site_dir"]

    @property
    def url(self) -> str:
        return self.raw["site_url"].rstrip("/") + "/"


class Page(NamedTuple):
    """Parsed markdown page: frontmatter metadata and body text."""

    meta: dict[str, Any]
    body: str


def _first(pattern: re.Pattern[str], text: str) -> str:
    """Return the first capture group of ``pattern`` in ``text``, trimmed."""
    return m.group(1).strip() if (m := pattern.search(text)) else ""


def _parse_frontmatter(text: str) -> Page:
    """Split a markdown page into frontmatter and body.

    Returns:
        ``Page({}, text)`` when no frontmatter is present.
    """
    if not (match := _FRONTMATTER_RE.match(text)):
        return Page({}, text)
    return Page(safe_load(match.group(1)) or {}, text[match.end() :])


def _render_public_md(page: Page) -> str:
    """Rebuild a markdown page, dropping MkDocs-only frontmatter keys."""
    if not (
        public := {k: v for k, v in page.meta.items() if k not in _MKDOCS_ONLY_KEYS}
    ):
        return page.body
    fm = safe_dump(public, sort_keys=False, allow_unicode=True).rstrip()
    return f"---\n{fm}\n---\n{page.body}"


def _page_title(docs_dir: Path, src: str) -> str:
    """Resolve a page's title from its frontmatter, falling back to the filename."""
    if (path := docs_dir / src).is_file():
        title = _parse_frontmatter(path.read_text("utf-8")).meta.get("title")
        if isinstance(title, str) and title:
            return title
    return src.removesuffix(".md").replace("_", " ").replace("-", " ").title()


def _walk_nav(
    nav: list[Any], url: str, docs_dir: Path, name: str = ""
) -> list[NavSection]:
    """Flatten the Zensical nav config into ordered sections of pages.

    Supports both nav item shapes: bare strings ``"file.md"`` (title comes from
    the file's frontmatter) and ``{"Title": "file.md" | [...]}`` dicts.

    Args:
        nav: Raw ``project.nav`` list from a Zensical TOML file.
        url: Language-scoped base URL, ending with ``/``.
        docs_dir: Markdown source directory used to resolve bare filenames.
        name: Section name when recursing; empty at the root.

    Returns:
        Ordered list of sections; pages at the current level precede any
        nested sections.
    """
    sections: list[NavSection] = []
    pages: list[NavPage] = []
    for item in nav:
        match item:
            case str() if item:
                pages.append((_page_title(docs_dir, item), f"{url}md/{item}", item))
            case dict():
                for title, value in item.items():
                    match value:
                        case str() if value:
                            pages.append((title, f"{url}md/{value}", value))
                        case list():
                            sections.extend(_walk_nav(value, url, docs_dir, title))
    if pages:
        sections.insert(0, (name, pages))
    return sections


def _jsonld_tags(schemas: list[dict[str, Any]], content: str) -> list[str]:
    """Build ``<script type="application/ld+json">`` tags missing from ``content``."""
    return [
        f'\n<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False)}\n</script>'
        for s in schemas
        if f'"{s["@type"]}"' not in content
    ]


def _opengraph_tags(site: Site, content: str) -> list[str]:
    """Build Open Graph + Twitter Card ``<meta>`` tags for a page.

    Returns an empty list when ``content`` already defines ``og:title``.
    Values are extracted from the page's existing ``<title>``, meta description
    and canonical link so localisation stays in sync with Zensical.
    """
    if 'property="og:title"' in content:
        return []
    title, description, canonical = (
        _first(r, content) for r in (_TITLE_RE, _DESC_RE, _CANONICAL_RE)
    )
    pairs = (
        ("og:type", "website"),
        ("og:site_name", site.raw.get("site_name", "")),
        ("og:locale", OG_LOCALES.get(site.lang, "en_US")),
        ("og:title", title),
        ("og:description", description),
        ("og:url", canonical),
        ("og:image", OG_IMAGE_URL),
        ("og:image:width", str(OG_WIDTH)),
        ("og:image:height", str(OG_HEIGHT)),
        ("twitter:card", "summary_large_image"),
        ("twitter:title", title),
        ("twitter:description", description),
        ("twitter:image", OG_IMAGE_URL),
    )
    return [f'\n<meta property="{k}" content="{v}">' for k, v in pairs if v]


def _inject_seo_metadata(site: Site) -> None:
    """Inject JSON-LD and Open Graph tags into every built HTML page.

    Idempotent: existing tags are detected and skipped. Each file is read and
    written at most once per build.
    """
    if not site.site_dir.is_dir():
        return
    for html in site.site_dir.rglob("*.html"):
        content = html.read_text("utf-8")
        schemas = [
            ORG_SCHEMA,
            *(s for marker, s in PATH_SCHEMAS if marker in str(html)),
        ]
        if not (
            tags := _jsonld_tags(schemas, content) + _opengraph_tags(site, content)
        ):
            continue
        payload = "".join(tags)
        html.write_text(
            _HEAD_RE.sub(lambda m: m.group(1) + payload, content, count=1), "utf-8"
        )


def _generate_llms_files(site: Site) -> None:
    """Emit ``llms.txt`` (nav index) and ``llms-full.txt`` (all content).

    Also materialises each source markdown (stripped of MkDocs-only frontmatter
    keys) under ``<site_dir>/md/`` for direct LLM consumption.
    """
    md_dir = site.site_dir / "md"
    md_dir.mkdir(exist_ok=True)

    pages: dict[str, Page] = {}
    for src in sorted(site.docs_dir.glob("*.md")):
        pages[src.name] = page = _parse_frontmatter(src.read_text("utf-8"))
        (md_dir / src.name).write_text(_render_public_md(page), "utf-8")

    header = (f"# {site.raw['site_name']}", "", f"> {site.raw['site_description']}", "")

    index_lines: list[str] = [*header]
    for section_name, section_pages in _walk_nav(
        site.raw["nav"], site.url, site.docs_dir
    ):
        if section_name:
            index_lines.extend((f"## {section_name}", ""))
        for title, page_url, src in section_pages:
            entry = f"- [{title}]({page_url})"
            if desc := pages.get(src, Page({}, "")).meta.get("description", ""):
                entry += f": {desc}"
            index_lines.append(entry)
        index_lines.append("")
    (site.site_dir / "llms.txt").write_text("\n".join(index_lines), "utf-8")

    full_lines: list[str] = [*header]
    for src, page in sorted(pages.items()):
        full_lines.extend(
            (
                "---",
                "",
                f"## {page.meta.get('title', src.removesuffix('.md'))}",
                f"Source: {site.url}md/{src}",
                "",
                page.body.strip(),
                "",
            )
        )
    (site.site_dir / "llms-full.txt").write_text("\n".join(full_lines), "utf-8")


def _render_cv_pdf(site: Site) -> None:
    """Render the resume markdown to a PDF via pandoc + WeasyPrint.

    All ``.no-print`` wrappers (``<div>`` blocks and single lines) are stripped
    before conversion so they never leak into the PDF.
    """
    if not (source := site.docs_dir / "resume.md").is_file():
        return
    content = _NO_PRINT_LINE_RE.sub(
        "", _NO_PRINT_BLOCK_RE.sub("", source.read_text("utf-8"))
    )
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", encoding="utf-8", delete_on_close=False
    ) as tmp:
        tmp.write(content)
        tmp.close()
        pypandoc.convert_file(
            tmp.name,
            to="pdf",
            outputfile=str(SITE / site.lang / "CV_JGoutin.pdf"),
            extra_args=["--pdf-engine=weasyprint"],
        )


def _render_og_png() -> None:
    """Rasterise ``og-image.svg`` to a 1200×630 PNG in ``site/assets/``."""
    if not (svg := ROOT_SRC / "assets" / "og-image.svg").is_file():
        return
    png = SITE / "assets" / "og-image.png"
    png.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(
        url=str(svg), write_to=str(png), output_width=OG_WIDTH, output_height=OG_HEIGHT
    )


def _copy_root_files() -> None:
    """Copy ``docs/_root/`` contents (CNAME, robots.txt, assets) into ``site/``."""
    if ROOT_SRC.is_dir():
        shutil.copytree(ROOT_SRC, SITE, dirs_exist_ok=True)


def build() -> None:
    """Run the full pipeline: Zensical + SEO + llms + PDFs + assets."""
    for lang in LANGUAGES:
        zensical_build(str(ROOT / f"zensical.{lang}.toml"), ZENSICAL_OPTS)
        site = Site.load(lang)
        _inject_seo_metadata(site)
        _generate_llms_files(site)
        _render_cv_pdf(site)
    _copy_root_files()
    _render_og_png()


if __name__ == "__main__":
    build()
