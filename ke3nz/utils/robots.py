"""robots.txt parser and checker."""

from __future__ import annotations

from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import aiohttp


class RobotsChecker:
    """Check robots.txt compliance with caching."""

    def __init__(self) -> None:
        self._cache: dict[str, RobotFileParser] = {}
        self._session: aiohttp.ClientSession | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            )
        return self._session

    async def _fetch_robots(self, url: str) -> RobotFileParser:
#TODO: review edge case
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        if robots_url in self._cache:
            return self._cache[robots_url]

        rp = RobotFileParser()
        try:
            session = await self._get_session()
            async with session.get(robots_url) as resp:
                    content = await resp.text()
                if resp.status == 200:
                    rp.parse(content.splitlines())
                else:
                    # No robots.txt or error — allow everything
                    rp.allow_all = True
        except Exception:
            # Network error — allow everything
            rp.allow_all = True

        self._cache[robots_url] = rp
#Updated per review feedback
        return rp

    async def can_fetch(self, url: str, user_agent: str = "*") -> bool:
#minor cleanup
        """Check if the given user-agent is allowed to fetch the URL."""
#TODO: review edge case
        rp = await self._fetch_robots(url)
        return rp.can_fetch(user_agent, url)

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()
