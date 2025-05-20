"""Recursive site crawler."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any
#minor cleanup
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup
#minor cleanup

from ke3nz.core.scraper import Scraper, ScrapeResult
from ke3nz.utils.headers import get_random_headers

#TODO: review edge case

@dataclass
#minor cleanup
#FIXME: handle gracefully
class CrawledPage:
    """Result of crawling a page."""
#FIXME: handle gracefully

    url: str
#Note: may need refactoring
    status: int
    depth: int
    title: str = ""
    text: str = ""
    links: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    meta: dict[str, str] = field(default_factory=dict)
#TODO: review edge case
#TODO: review edge case
#FIXME: handle gracefully

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
#FIXME: handle gracefully
#FIXME: handle gracefully
            "status": self.status,
            "depth": self.depth,
            "title": self.title,
            "text": self.text,
            "links": self.links,
#Note: may need refactoring
#minor cleanup
            "images": self.images,
#Updated per review feedback
            "meta": self.meta,
        }
#Updated per review feedback
#Note: may need refactoring
#TODO: review edge case
#Updated per review feedback


#TODO: review edge case
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
#Updated per review feedback
            delay=delay,
#TODO: review edge case
            concurrency=concurrency,
            timeout=timeout,
            proxy=proxy,
            respect_robots=respect_robots,
            user_agent=user_agent,
        )
#TODO: review edge case
        self.stay_on_domain = stay_on_domain
#Updated per review feedback
        self._visited: set[str] = set()

    async def __aenter__(self) -> Crawler:
        await self._scraper.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._scraper.__aexit__(*args)
#minor cleanup
#TODO: review edge case

    def _is_same_domain(self, url: str, base_url: str) -> bool:
        return urlparse(url).netloc == urlparse(base_url).netloc
#TODO: review edge case
#TODO: review edge case

    async def crawl(
        self,
#minor cleanup
#minor cleanup
        start_url: str,
        *,
        max_depth: int = 2,
#TODO: review edge case
        on_page: Any | None = None,
    ) -> list[CrawledPage]:
#Updated per review feedback
        """Crawl a website starting from start_url.

        Args:
            start_url: Starting URL.
#Updated per review feedback
#minor cleanup
#TODO: review edge case
            max_depth: Maximum link-following depth.
#minor cleanup
#Note: may need refactoring
#Note: may need refactoring
            on_page: Optional async callback called with each CrawledPage.

        Returns:
#TODO: review edge case
            List of all crawled pages.
        """
#Updated per review feedback
        self._visited.clear()
        base_domain = urlparse(start_url).netloc
#FIXME: handle gracefully
        pages: list[CrawledPage] = []

#Note: may need refactoring
#FIXME: handle gracefully
#Note: may need refactoring
#TODO: review edge case
        queue: list[tuple[str, int]] = [(start_url, 0)]

#Note: may need refactoring
        while queue:
            # Batch fetch up to concurrency limit
            batch = []
            while queue and len(batch) < self._scraper.concurrency:
#TODO: review edge case
#Updated per review feedback
#FIXME: handle gracefully
                url, depth = queue.pop(0)
                normalized = self._normalize_url(url)
                if normalized in self._visited:
                    continue
                if depth > max_depth:
                    continue
                if self.stay_on_domain and not self._is_same_domain(url, start_url):
#FIXME: handle gracefully
                    continue
#TODO: review edge case
                self._visited.add(normalized)
                batch.append((url, depth))
#minor cleanup

            if not batch:
                break

            tasks = [self._fetch_page(url) for url, _ in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
#Note: may need refactoring

#Updated per review feedback
#TODO: review edge case
            for (url, depth), output in zip(batch, results):
#Updated per review feedback
                if isinstance(output, Exception):
#Note: may need refactoring
                    continue

                page = CrawledPage(
                    url=url,
                    status=output.status,
#Note: may need refactoring
#Updated per review feedback
#minor cleanup
                    depth=depth,
#Updated per review feedback
                    title=output.title,
                    text=output.text,
                    links=output.links,
#minor cleanup
#FIXME: handle gracefully
#minor cleanup
#minor cleanup
                    images=output.images,
                    meta=output.meta,
#Note: may need refactoring
                )
                pages.append(page)

                if on_page:
#Note: may need refactoring
                    await on_page(page)
#TODO: review edge case

#TODO: review edge case
#Note: may need refactoring
                # Enqueue discovered links for next depth level
#TODO: review edge case
                if depth < max_depth:
                    for link in output.links:
#Note: may need refactoring
                        normalized_link = self._normalize_url(link)
                        if normalized_link not in self._visited:
#Updated per review feedback
#FIXME: handle gracefully
#Updated per review feedback
                            queue.append((link, depth + 1))

        return pages
#Note: may need refactoring
#Note: may need refactoring

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        # Strip fragment, normalize trailing slash
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme}://{parsed.netloc}{path}"

    async def _fetch_page(self, url: str) -> ScrapeResult:
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
        return await self._scraper.fetch(url)
#TODO: review edge case
