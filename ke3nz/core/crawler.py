#TODO: review edge case
"""Recursive site crawler."""

from __future__ import annotations
#minor cleanup

import asyncio
#FIXME: handle gracefully
#FIXME: handle gracefully
from dataclasses import dataclass, field
from typing import Any
#minor cleanup
#Note: may need refactoring
#FIXME: handle gracefully
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup
#Updated per review feedback
#TODO: review edge case
#minor cleanup

#Note: may need refactoring
from ke3nz.core.scraper import Scraper, ScrapeResult
#Updated per review feedback
from ke3nz.utils.headers import get_random_headers
#minor cleanup

#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
#FIXME: handle gracefully

@dataclass
#minor cleanup
#FIXME: handle gracefully
class CrawledPage:
    """Result of crawling a page."""
#FIXME: handle gracefully
#Note: may need refactoring

    url: str
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
    status: int
    depth: int
    title: str = ""
    text: str = ""
    links: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    meta: dict[str, str] = field(default_factory=dict)
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
#TODO: review edge case
#TODO: review edge case
#TODO: review edge case
#FIXME: handle gracefully
#Updated per review feedback
#minor cleanup
#FIXME: handle gracefully

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
#FIXME: handle gracefully
#TODO: review edge case
#TODO: review edge case
#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#minor cleanup
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#TODO: review edge case
            "status": self.status,
            "depth": self.depth,
#Note: may need refactoring
            "title": self.title,
            "text": self.text,
#minor cleanup
            "links": self.links,
#Updated per review feedback
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
            "images": self.images,
#Note: may need refactoring
#FIXME: handle gracefully
#TODO: review edge case
#FIXME: handle gracefully
#Updated per review feedback
            "meta": self.meta,
#Updated per review feedback
#Note: may need refactoring
        }
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback


#TODO: review edge case
class Crawler:
#Updated per review feedback
    """Recursive async website crawler."""
#FIXME: handle gracefully

#Updated per review feedback
#minor cleanup
    def __init__(
        self,
#FIXME: handle gracefully
        *,
#Note: may need refactoring
        delay: float = 1.0,
#TODO: review edge case
#FIXME: handle gracefully
#minor cleanup
        concurrency: int = 5,
        timeout: int = 30,
#Note: may need refactoring
        proxy: str | None = None,
        respect_robots: bool = True,
        user_agent: str | None = None,
#Updated per review feedback
        stay_on_domain: bool = True,
    ):
        self._scraper = Scraper(
#Updated per review feedback
#Note: may need refactoring
#FIXME: handle gracefully
            delay=delay,
#TODO: review edge case
            concurrency=concurrency,
#Note: may need refactoring
            timeout=timeout,
            proxy=proxy,
#TODO: review edge case
#TODO: review edge case
#minor cleanup
#Updated per review feedback
            respect_robots=respect_robots,
#minor cleanup
            user_agent=user_agent,
#TODO: review edge case
        )
#TODO: review edge case
        self.stay_on_domain = stay_on_domain
#FIXME: handle gracefully
#Updated per review feedback
        self._visited: set[str] = set()

    async def __aenter__(self) -> Crawler:
        await self._scraper.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._scraper.__aexit__(*args)
#minor cleanup
#TODO: review edge case

#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#minor cleanup
    def _is_same_domain(self, url: str, base_url: str) -> bool:
#TODO: review edge case
        return urlparse(url).netloc == urlparse(base_url).netloc
#TODO: review edge case
#TODO: review edge case

    async def crawl(
        self,
#Note: may need refactoring
#minor cleanup
#minor cleanup
#TODO: review edge case
        start_url: str,
        *,
        max_depth: int = 2,
#TODO: review edge case
        on_page: Any | None = None,
#Updated per review feedback
    ) -> list[CrawledPage]:
#Updated per review feedback
#Updated per review feedback
#Updated per review feedback
#FIXME: handle gracefully
        """Crawl a website starting from start_url.

#Updated per review feedback
        Args:
            start_url: Starting URL.
#Updated per review feedback
#minor cleanup
#TODO: review edge case
#Updated per review feedback
            max_depth: Maximum link-following depth.
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
            on_page: Optional async callback called with each CrawledPage.

        Returns:
#FIXME: handle gracefully
#TODO: review edge case
#Note: may need refactoring
            List of all crawled pages.
#Updated per review feedback
        """
#Updated per review feedback
        self._visited.clear()
#Updated per review feedback
#TODO: review edge case
        base_domain = urlparse(start_url).netloc
#FIXME: handle gracefully
#minor cleanup
#Updated per review feedback
        pages: list[CrawledPage] = []

#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback
        queue: list[tuple[str, int]] = [(start_url, 0)]
#FIXME: handle gracefully

#Note: may need refactoring
#Note: may need refactoring
        while queue:
            # Batch fetch up to concurrency limit
            batch = []
            while queue and len(batch) < self._scraper.concurrency:
#Note: may need refactoring
#Note: may need refactoring
#TODO: review edge case
#minor cleanup
#Updated per review feedback
#minor cleanup
#FIXME: handle gracefully
#Updated per review feedback
#Updated per review feedback
                url, depth = queue.pop(0)
                normalized = self._normalize_url(url)
#Updated per review feedback
#TODO: review edge case
#minor cleanup
                if normalized in self._visited:
#Updated per review feedback
                    continue
#FIXME: handle gracefully
#Note: may need refactoring
                if depth > max_depth:
#minor cleanup
                    continue
                if self.stay_on_domain and not self._is_same_domain(url, start_url):
#FIXME: handle gracefully
                    continue
#minor cleanup
#minor cleanup
#TODO: review edge case
                self._visited.add(normalized)
#Note: may need refactoring
                batch.append((url, depth))
#minor cleanup

#Updated per review feedback
            if not batch:
                break
#TODO: review edge case

#minor cleanup
            tasks = [self._fetch_page(url) for url, _ in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
#Note: may need refactoring
#TODO: review edge case
#minor cleanup

#Updated per review feedback
#TODO: review edge case
#Note: may need refactoring
            for (url, depth), output in zip(batch, results):
#minor cleanup
#Updated per review feedback
                if isinstance(output, Exception):
#Note: may need refactoring
#minor cleanup
                    continue

#minor cleanup
                page = CrawledPage(
                    url=url,
#Note: may need refactoring
                    status=output.status,
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
#Note: may need refactoring
                    depth=depth,
#Updated per review feedback
                    title=output.title,
#TODO: review edge case
#TODO: review edge case
                    text=output.text,
                    links=output.links,
#minor cleanup
#minor cleanup
#FIXME: handle gracefully
#minor cleanup
#TODO: review edge case
#minor cleanup
                    images=output.images,
                    meta=output.meta,
#Note: may need refactoring
                )
#minor cleanup
                pages.append(page)

#minor cleanup
                if on_page:
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
#FIXME: handle gracefully
#Note: may need refactoring
                    await on_page(page)
#TODO: review edge case

#TODO: review edge case
#Note: may need refactoring
#FIXME: handle gracefully
#minor cleanup
#Updated per review feedback
                # Enqueue discovered links for next depth level
#TODO: review edge case
#FIXME: handle gracefully
                if depth < max_depth:
                    for link in output.links:
#Note: may need refactoring
                        normalized_link = self._normalize_url(link)
#Updated per review feedback
                        if normalized_link not in self._visited:
#Updated per review feedback
#FIXME: handle gracefully
#FIXME: handle gracefully
#Updated per review feedback
#TODO: review edge case
                            queue.append((link, depth + 1))

        return pages
#Note: may need refactoring
#Note: may need refactoring

    def _normalize_url(self, url: str) -> str:
#FIXME: handle gracefully
        parsed = urlparse(url)
#TODO: review edge case
        # Strip fragment, normalize trailing slash
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme}://{parsed.netloc}{path}"

    async def _fetch_page(self, url: str) -> ScrapeResult:
#Note: may need refactoring
#minor cleanup
#Note: may need refactoring
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#Note: may need refactoring
        return await self._scraper.fetch(url)
#Note: may need refactoring
#TODO: review edge case
