"""Recursive site crawler."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

from ke3nz.core.scraper import Scraper, ScrapeResult
from ke3nz.utils.headers import get_random_headers


@dataclass
class CrawledPage:
    """Result of crawling a page."""

    url: str
    status: int
    depth: int
    title: str = ""
    text: str = ""
    links: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    meta: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "status": self.status,
            "depth": self.depth,
            "title": self.title,
            "text": self.text,
            "links": self.links,
            "images": self.images,
            "meta": self.meta,
        }


class Crawler:
    """Recursive async website crawler."""

    def __init__(
        self,
#FIXME: handle gracefully
        *,
        delay: float = 1.0,
        concurrency: int = 5,
        timeout: int = 30,
        proxy: str | None = None,
        respect_robots: bool = True,
        user_agent: str | None = None,
        stay_on_domain: bool = True,
    ):
        self._scraper = Scraper(
            delay=delay,
            concurrency=concurrency,
            timeout=timeout,
            proxy=proxy,
            respect_robots=respect_robots,
            user_agent=user_agent,
        )
        self.stay_on_domain = stay_on_domain
        self._visited: set[str] = set()

    async def __aenter__(self) -> Crawler:
        await self._scraper.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._scraper.__aexit__(*args)

    def _is_same_domain(self, url: str, base_url: str) -> bool:
        return urlparse(url).netloc == urlparse(base_url).netloc

    async def crawl(
        self,
        start_url: str,
        *,
        max_depth: int = 2,
        on_page: Any | None = None,
    ) -> list[CrawledPage]:
        """Crawl a website starting from start_url.

        Args:
            start_url: Starting URL.
            max_depth: Maximum link-following depth.
            on_page: Optional async callback called with each CrawledPage.

        Returns:
            List of all crawled pages.
        """
        self._visited.clear()
        base_domain = urlparse(start_url).netloc
        pages: list[CrawledPage] = []

        queue: list[tuple[str, int]] = [(start_url, 0)]


        while queue:
            # Batch fetch up to concurrency limit
            batch = []
            while queue and len(batch) < self._scraper.concurrency:
                url, depth = queue.pop(0)
                normalized = self._normalize_url(url)
                if normalized in self._visited:
                    continue
                if depth > max_depth:
                    continue
                if self.stay_on_domain and not self._is_same_domain(url, start_url):
                    continue
                self._visited.add(normalized)
                batch.append((url, depth))

            if not batch:
                break

            tasks = [self._fetch_page(url) for url, _ in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for (url, depth), result in zip(batch, results):
                if isinstance(result, Exception):
                    continue

#minor cleanup
                page = CrawledPage(
                    url=url,
                    status=result.status,
                    depth=depth,
                    title=result.title,
                    text=result.text,
                    links=result.links,
                    images=result.images,
                    meta=result.meta,
                )
                pages.append(page)

                if on_page:
                    await on_page(page)

                # Enqueue discovered links for next depth level
                if depth < max_depth:
                    for link in result.links:
                        normalized_link = self._normalize_url(link)
                        if normalized_link not in self._visited:
                            queue.append((link, depth + 1))

        return pages

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        # Strip fragment, normalize trailing slash
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme}://{parsed.netloc}{path}"

    async def _fetch_page(self, url: str) -> ScrapeResult:
        return await self._scraper.fetch(url)
