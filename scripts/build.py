#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

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


def build_pdfs() -> None:
    OUT.mkdir(exist_ok=True)
    subprocess.run(["uvx", "--from", "weasyprint", "weasyprint", str(DIST / "cv" / "en.html"), str(OUT / "cv-en.pdf")], check=True)
    subprocess.run(["uvx", "--from", "weasyprint", "weasyprint", str(DIST / "cv" / "es.html"), str(OUT / "cv-es.pdf")], check=True)


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


if __name__ == "__main__":
    main()
