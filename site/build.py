"""Publish repository Markdown as a static GitHub Pages documentation site."""

from __future__ import annotations

import argparse
from html import escape, unescape
from pathlib import Path
import re
import shutil
from urllib.parse import quote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/mediaprophet/license"
PUBLIC_URL = "https://mediaprophet.github.io/license/"
DESCRIPTION = (
    "Why related projects use temporary alternative licences while the constituent "
    "systems for a human centric licensing and rights fabric are developed."
)


def page_name(path: Path) -> str:
    return "index.html" if path.name == "PROJECT-PURPOSE.md" else path.stem + ".html"


def rewrite_links(body: str, pages: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        href = unescape(match.group(1))
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path:
            return match.group(0)
        path = parts.path.removeprefix("./")
        if path in pages:
            target = pages[path]
        elif (ROOT / path).is_file() and (ROOT / path).resolve().is_relative_to(ROOT):
            target = REPO + "/blob/main/" + quote(path, safe="/")
        else:
            raise ValueError(f"Unresolved repository link: {href}")
        if parts.query:
            target += "?" + parts.query
        if parts.fragment:
            target += "#" + parts.fragment
        return 'href="' + escape(target, quote=True) + '"'

    return re.sub(r'href="([^"]*)"', replace, body)


def render(source: Path, pages: dict[str, str]) -> str:
    text = source.read_text(encoding="utf-8-sig")
    title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not title_match:
        raise ValueError(f"Missing document title: {source.name}")
    title = title_match.group(1)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc"],
        extension_configs={"toc": {"toc_depth": "2-3", "permalink": False}},
    )
    body = rewrite_links(md.convert(text), pages)
    # Wide reference tables remain readable without overflowing the whole page.
    body = body.replace("<table>", '<div class="table-scroll" tabindex="0" role="region" aria-label="Reference table"><table>')
    body = body.replace("</table>", "</table></div>")
    canonical = PUBLIC_URL + ("" if source.name == "PROJECT-PURPOSE.md" else page_name(source))
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} · License</title>
  <meta name="description" content="{escape(DESCRIPTION, quote=True)}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="assets/site.css">
</head>
<body>
  <a class="skip-link" href="#content">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="index.html">License<span>Human centric rights fabric</span></a>
      <nav aria-label="Primary navigation">
        <a href="index.html">Purpose</a>
        <a href="README.html">Documentation</a>
        <a href="{REPO}">Repository <span aria-hidden="true">↗</span></a>
      </nav>
    </div>
  </header>
  <div class="status-strip">In development <span aria-hidden="true">·</span> Ecosystem prerequisites and adoption review remain outstanding.</div>
  <div class="page-layout">
    <aside aria-label="Document navigation">
      <p class="section-label">On this page</p>
      <nav class="desktop-toc" aria-label="Table of contents">{md.toc}</nav>
      <details class="mobile-toc"><summary>On this page</summary><nav aria-label="Table of contents">{md.toc}</nav></details>
      <div class="aside-links">
        <a href="PROJECT-PURPOSE.html">Share this explanation</a>
        <a href="{REPO}/blob/main/{quote(source.name)}">View Markdown source ↗</a>
      </div>
    </aside>
    <main id="content" tabindex="-1">
      <p class="eyebrow">Cooperative ecosystems · Humanitarian ICT</p>
      <article>{body}</article>
      <div class="document-end"><span>Continue exploring</span><a href="README.html">Browse the framework documentation →</a></div>
    </main>
  </div>
  <footer><div>License and rights management for cooperative ecosystems.</div><a href="{REPO}/blob/main/{quote(source.name)}">Source and revision history ↗</a></footer>
</body>
</html>
'''


def build(output: Path) -> None:
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output must be a new or empty directory.")
    sources = sorted(ROOT.glob("*.md"))
    pages = {source.name: page_name(source) for source in sources}
    rendered = {page_name(source): render(source, pages) for source in sources}
    output.mkdir(parents=True, exist_ok=True)
    for name, html in rendered.items():
        (output / name).write_text(html, encoding="utf-8")
    # Preserve a descriptive URL as well as the short project root URL.
    (output / "PROJECT-PURPOSE.html").write_text(rendered["index.html"], encoding="utf-8")
    (output / "assets").mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "site" / "site.css", output / "assets" / "site.css")
    (output / ".nojekyll").touch()
    print(f"Built {len(rendered) + 1} HTML pages in {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "pages")
    build(parser.parse_args().output)
