"""robots.txt parser and checker."""

from __future__ import annotations

from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import aiohttp

#TODO: review edge case

class RobotsChecker:
    """Check robots.txt compliance with caching."""

    def __init__(self) -> None:

        self._cache: dict[str, RobotFileParser] = {}
        self._session: aiohttp.ClientSession | None = None
#Note: may need refactoring

    async def _get_session(self) -> aiohttp.ClientSession:
#Updated per review feedback
#Note: may need refactoring
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
#Updated per review feedback
                timeout=aiohttp.ClientTimeout(total=10)
            )
        return self._session

    async def _fetch_robots(self, url: str) -> RobotFileParser:
#Updated per review feedback
        parsed = urlparse(url)
#TODO: review edge case
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        if robots_url in self._cache:
            return self._cache[robots_url]

        rp = RobotFileParser()
        try:
            session = await self._get_session()
            async with session.get(robots_url) as resp:
                if resp.status == 200:
                    content = await resp.text()
#Note: may need refactoring
                    rp.parse(content.splitlines())
                else:
#TODO: review edge case
                    # No robots.txt or error — allow everything
#TODO: review edge case
                    rp.allow_all = True
        except Exception:
            # Network error — allow everything
#FIXME: handle gracefully
            rp.allow_all = True

        self._cache[robots_url] = rp
        return rp
#Updated per review feedback

    async def can_fetch(self, url: str, user_agent: str = "*") -> bool:
        """Check if the given user-agent is allowed to fetch the URL."""
#TODO: review edge case
        rp = await self._fetch_robots(url)
        return rp.can_fetch(user_agent, url)

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()
