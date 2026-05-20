#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
OUT = ROOT / "out"
TEMPLATE = ROOT / "templates" / "page.html5"


@dataclass
class Page:
    source: Path
    output: Path
    body: str
    meta: dict[str, str]


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    candidates = []
    for marker in ("\n---\n", "\n...\n"):
        idx = text.find(marker, 4)
        if idx != -1:
            candidates.append((idx, len(marker)))
    if not candidates:
        return {}, text
    end, marker_len = min(candidates, key=lambda item: item[0])
    raw_meta = text[4:end]
    rest = text[end + marker_len :]
    meta: dict[str, str] = {}
    for line in raw_meta.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, rest


def rel(output: Path, target: Path) -> str:
    return str(Path(shutil.os.path.relpath(target, output.parent))).replace("\\", "/")


def site_path(path: str) -> str:
    return path if path.startswith("/") else f"/{path}"


def footer(lang: str) -> tuple[str, str]:
    if lang == "es":
        return (
            "Disponible para consultoría globalmente (remoto) y en Buenos Aires.",
            "Contactame en LinkedIn",
        )
    return (
        "Available for consulting engagements globally (remote) and in Buenos Aires.",
        "Contact me on LinkedIn",
    )


def nav_html(output: Path) -> str:
    return '<a href="/">Home</a>'


def extract_title(markdown: str) -> str | None:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def rewrite_links(markdown: str) -> str:
    markdown = markdown.replace("./cv/en.md", "/cv/en.html")
    markdown = markdown.replace("./cv/es.md", "/cv/es.html")
    markdown = markdown.replace("./index.md", "/index.html")
    markdown = markdown.replace("./en.html", "/cv/en.html")
    markdown = markdown.replace("./es.html", "/cv/es.html")
    markdown = markdown.replace("../cv/", "/cv/")
    return markdown


def render(page: Page) -> None:
    page.output.parent.mkdir(parents=True, exist_ok=True)
    lang = page.meta.get("lang", "en-US")
    if lang == "en":
        lang = "en-US"
    footer_text, footer_link_text = footer(page.meta.get("lang", "en"))
    args = [
        "pandoc",
        "--standalone",
        "--from",
        "markdown-yaml_metadata_block-citations",
        "--to",
        "html",
        "--template",
        str(TEMPLATE),
        "--output",
        str(page.output),
        "-V",
        f"lang={lang}",
        "-V",
        f"css_path={site_path('assets/css/style.css')}",
        "-V",
        f"favicon_path={site_path('assets/favicon.ico')}",
        "-V",
        f"apple_touch_icon_path={site_path('assets/apple-touch-icon.png')}",
        "-V",
        f"favicon_32_path={site_path('assets/favicon-32.png')}",
        "-V",
        f"favicon_64_path={site_path('assets/favicon-64.png')}",
        "-V",
        f"nav_html={nav_html(page.output)}",
        "-V",
        f"footer_text={footer_text}",
        "-V",
        f"footer_link_text={footer_link_text}",
    ]
    title = page.meta.get("title") or extract_title(page.body)
    if title:
        args.extend(["-M", f"title={title}"])
    subprocess.run(args, input=rewrite_links(page.body), text=True, check=True)


def load_page(path: Path, output: Path) -> Page:
    meta, body = split_front_matter(path.read_text())
    return Page(path, output, body, meta)


def build_blog_index(posts: list[tuple[datetime, dict[str, str], Path]]) -> Page:
    source = ROOT / "blog" / "index.md"
    meta, body = split_front_matter(source.read_text())
    es_posts = []
    en_posts = []
    for date, post_meta, output in sorted(posts, key=lambda item: item[0], reverse=True):
        line = f"- [{post_meta['title']}]({rel(DIST / 'blog' / 'index.html', output)}) — {date.strftime('%Y-%m-%d')}"
        if post_meta.get("lang") == "es":
            es_posts.append(line)
        else:
            en_posts.append(line)
    generated = (
        body.strip()
        + "\n\n## Artículos en Español\n\n"
        + "\n".join(es_posts)
        + "\n\n## Posts in English\n\n"
        + "\n".join(en_posts)
        + "\n"
    )
    return Page(source, DIST / "blog" / "index.html", generated, meta)


def copy_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    for path in src.rglob("*"):
        if path.is_dir():
            continue
        relpath = path.relative_to(src)
        target = dst / relpath
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def copy_cv_assets() -> None:
    exts = {".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp"}
    src = ROOT / "cv"
    dst = DIST / "cv"
    for path in src.iterdir():
        if path.is_file() and path.suffix.lower() in exts:
            dst.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dst / path.name)


def build_posts() -> list[tuple[datetime, dict[str, str], Path]]:
    built: list[tuple[datetime, dict[str, str], Path]] = []
    for post in sorted((ROOT / "_posts").glob("*.md")):
        match = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", post.name)
        if not match:
            continue
        year, month, day, slug = match.groups()
        date = datetime(int(year), int(month), int(day))
        output = DIST / year / month / day / f"{slug}.html"
        page = load_page(post, output)
        render(page)
        built.append((date, page.meta, output))
    return built


def build_pages() -> None:
    render(Page(ROOT / "index.md", DIST / "index.html", (ROOT / "index.md").read_text(), {"lang": "en", "title": "Sasha (Augusto) Kielbowicz"}))
    render(load_page(ROOT / "cv" / "en.md", DIST / "cv" / "en.html"))
    render(load_page(ROOT / "cv" / "es.md", DIST / "cv" / "es.html"))
    posts = build_posts()
    render(build_blog_index(posts))


def localize_root_relative_urls(html: str, html_path: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        attr, url = match.groups()
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path.startswith("/"):
            return match.group(0)
        if parts.path == "/":
            target = DIST / "index.html"
        else:
            target = DIST / parts.path.lstrip("/")
        localized = rel(html_path, target)
        new_url = urlunsplit(("", "", localized, parts.query, parts.fragment))
        return f'{attr}="{new_url}"'

    return re.sub(r'(href|src)="([^"]+)"', replace, html)


def structure_pdf_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main")
    if not isinstance(main, Tag):
        return html

    forced_break_sections = {
        "Teaching Experience",
        "Experiencia en Docencia",
    }

    nav: Tag | None = None
    hero = soup.new_tag("section", attrs={"class": "pdf-hero"})
    sections: list[Tag] = []
    current_section: Tag | None = None
    current_entry: Tag | None = None
    current_entry_header: Tag | None = None
    seen_h2 = False

    for child in list(main.contents):
        if isinstance(child, NavigableString):
            if not child.strip():
                child.extract()
                continue
            target = current_entry or current_section or hero
            target.append(child.extract())
            continue

        if child.name == "nav":
            nav = child.extract()
            continue

        if child.name == "h2":
            seen_h2 = True
            current_entry = None
            current_entry_header = None
            title = child.get_text(" ", strip=True)
            section_classes = ["pdf-section"]
            if title in forced_break_sections:
                section_classes.append("page-break-before")
            current_section = soup.new_tag("section", attrs={"class": section_classes})
            child_classes = child.get("class", [])
            child["class"] = [*child_classes, "pdf-section-heading"]
            current_section.append(child.extract())
            sections.append(current_section)
            continue

        if child.name == "h3" and seen_h2 and current_section is not None:
            current_entry = soup.new_tag("section", attrs={"class": "pdf-entry"})
            current_entry_header = soup.new_tag("div", attrs={"class": "pdf-entry-header"})
            child_classes = child.get("class", [])
            child["class"] = [*child_classes, "pdf-entry-heading"]
            current_entry_header.append(child.extract())
            current_entry.append(current_entry_header)
            current_section.append(current_entry)
            continue

        if current_entry is not None and current_entry_header is not None:
            if child.name in {"ul", "ol", "table", "pre", "blockquote"}:
                current_entry.append(child.extract())
            elif child.name == "hr":
                current_entry = None
                current_entry_header = None
                current_section.append(child.extract())
            else:
                current_entry_header.append(child.extract())
            continue

        target = hero if not seen_h2 else (current_section or hero)
        target.append(child.extract())

    main.clear()
    if nav is not None:
        main.append(nav)
    if hero.contents:
        main.append(hero)
    for section in sections:
        main.append(section)
    return str(soup)


def prepare_pdf_html(src: Path, pdf_html: Path) -> str:
    html = localize_root_relative_urls(src.read_text(), pdf_html)
    html = re.sub(r'<p><a href="(?:\.\./)?(?:cv/)?(?:en|es)\.html">(?:English|Español)</a></p>\s*', "", html, count=1)
    html = structure_pdf_html(html)
    pdf_css = rel(pdf_html, DIST / "assets" / "css" / "pdf.css")
    html = html.replace("</head>", f'  <link rel="stylesheet" href="{pdf_css}" />\n</head>', 1)
    html = html.replace("<body>", '<body class="pdf-export">', 1)
    return html


def build_pdf(src: Path, dst: Path) -> None:
    pdf_html = src.with_name(f".{src.stem}.pdf.html")
    pdf_html.write_text(prepare_pdf_html(src, pdf_html))
    try:
        subprocess.run(["uvx", "--from", "weasyprint", "weasyprint", str(pdf_html), str(dst)], check=True)
    finally:
        pdf_html.unlink(missing_ok=True)


def build_pdfs() -> None:
    OUT.mkdir(exist_ok=True)
    build_pdf(DIST / "cv" / "en.html", OUT / "cv-en.pdf")
    build_pdf(DIST / "cv" / "es.html", OUT / "cv-es.pdf")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)
    copy_tree(ROOT / "assets", DIST / "assets")
    copy_cv_assets()
    if (ROOT / "CNAME").exists():
        shutil.copy2(ROOT / "CNAME", DIST / "CNAME")
    (DIST / ".nojekyll").write_text("")
    build_pages()
    if "--pdf" in sys.argv[1:]:
        build_pdfs()


if __name__ == "__main__":
    main()
