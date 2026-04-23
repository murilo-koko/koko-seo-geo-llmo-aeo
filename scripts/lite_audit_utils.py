#!/usr/bin/env python3
"""Shared helpers for lightweight HTML audits without third-party dependencies."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

import json
import re


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/137.0.0.0 Safari/537.36"
)

STOP_WORDS = {
    "a", "an", "and", "as", "at", "be", "by", "com", "da", "das", "de", "do", "dos",
    "e", "em", "for", "from", "how", "https", "in", "is", "it", "mais", "na", "no",
    "nos", "não", "o", "of", "on", "or", "para", "por", "pra", "que", "seu", "sua",
    "the", "this", "to", "um", "uma", "ver", "você", "with", "www",
}


@dataclass
class PageSnapshot:
    url: str
    final_url: str
    status_code: int
    title: str
    meta_description: str
    canonical: str
    h1_count: int
    h1_texts: list[str]
    schema_count: int
    links: list[str]
    word_count: int
    top_terms: list[str]
    page_type: str


class AuditHTMLParser(HTMLParser):
    """Collect a minimal set of page signals from raw HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.canonical = ""
        self.h1_count = 0
        self.h1_texts: list[str] = []
        self.links: list[str] = []
        self.schema_count = 0
        self._in_title = False
        self._in_h1 = False
        self._ignore_depth = 0
        self._text_chunks: list[str] = []
        self._current_h1: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag in {"script", "style", "noscript"}:
            self._ignore_depth += 1
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._in_h1 = True
            self.h1_count += 1
            self._current_h1 = []
        if tag == "meta" and attr_map.get("name", "").lower() == "description":
            self.meta_description = (attr_map.get("content") or "").strip()
        if tag == "link" and attr_map.get("rel", "").lower() == "canonical":
            self.canonical = (attr_map.get("href") or "").strip()
        if tag == "a" and attr_map.get("href"):
            self.links.append(attr_map["href"])
        if (
            tag == "script"
            and (attr_map.get("type") or "").lower() == "application/ld+json"
        ):
            self.schema_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self._ignore_depth > 0:
            self._ignore_depth -= 1
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False
            text = " ".join(self._current_h1).strip()
            if text:
                self.h1_texts.append(text)
            self._current_h1 = []

    def handle_data(self, data: str) -> None:
        if self._ignore_depth > 0:
            return
        text = data.strip()
        if not text:
            return
        if self._in_title:
            self.title = f"{self.title} {text}".strip()
        if self._in_h1:
            self._current_h1.append(text)
        self._text_chunks.append(text)

    @property
    def visible_text(self) -> str:
        return " ".join(self._text_chunks)


def _tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-ZÀ-ÿ0-9]{3,}", text.lower())
    return [token for token in tokens if token not in STOP_WORDS]


def _top_terms(text: str, limit: int = 12) -> list[str]:
    counts = Counter(_tokenize(text))
    return [term for term, _ in counts.most_common(limit)]


def _word_count(text: str) -> int:
    return len(_tokenize(text))


def infer_page_type(url: str, word_count: int) -> str:
    parsed = urlparse(url)
    path = parsed.path.lower()
    if path in {"", "/"}:
        return "landing-page"
    if "/blog/" in path or "/blog" == path.rstrip("/"):
        return "blog"
    if any(token in path for token in ("/contact", "/contato", "/pricing", "/preco")):
        return "other"
    if any(token in path for token in ("/services", "/servicos", "/demo", "/product", "/produto")):
        return "landing-page"
    if word_count >= 1200:
        return "blog"
    if word_count <= 350:
        return "other"
    return "landing-page"


def fetch_snapshot(url: str, timeout: int = 20) -> PageSnapshot:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        final_url = response.geturl()
        status_code = getattr(response, "status", 200)
        html = response.read().decode("utf-8", errors="replace")

    parser = AuditHTMLParser()
    parser.feed(html)
    visible_text = parser.visible_text
    word_count = _word_count(visible_text)
    top_terms = _top_terms(" ".join([parser.title, " ".join(parser.h1_texts), visible_text]))

    return PageSnapshot(
        url=url,
        final_url=final_url,
        status_code=status_code,
        title=parser.title,
        meta_description=parser.meta_description,
        canonical=parser.canonical,
        h1_count=parser.h1_count,
        h1_texts=parser.h1_texts,
        schema_count=parser.schema_count,
        links=parser.links,
        word_count=word_count,
        top_terms=top_terms,
        page_type=infer_page_type(final_url, word_count),
    )


def normalize_internal_links(base_url: str, links: list[str]) -> list[str]:
    base = urlparse(base_url)
    normalized: list[str] = []
    seen: set[str] = set()
    for link in links:
        absolute = urljoin(base_url, link)
        parsed = urlparse(absolute)
        if parsed.scheme not in {"http", "https"}:
            continue
        if parsed.netloc != base.netloc:
            continue
        cleaned = parsed._replace(fragment="", query="").geturl()
        if cleaned in seen:
            continue
        seen.add(cleaned)
        normalized.append(cleaned)
    return normalized


def jaccard_similarity(left: list[str], right: list[str]) -> float:
    left_set = set(left)
    right_set = set(right)
    if not left_set and not right_set:
        return 0.0
    return len(left_set & right_set) / len(left_set | right_set)


def dump_json(payload: dict) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False)
