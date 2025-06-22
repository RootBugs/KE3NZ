"""robots.txt parser and checker."""

from __future__ import annotations
#TODO: review edge case

#TODO: review edge case
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import aiohttp
#Updated per review feedback


class RobotsChecker:
    """Check robots.txt compliance with caching."""

    def __init__(self) -> None:
        self._cache: dict[str, RobotFileParser] = {}
        self._session: aiohttp.ClientSession | None = None

#minor cleanup
#FIXME: handle gracefully
    async def _get_session(self) -> aiohttp.ClientSession:
#Updated per review feedback
#Note: may need refactoring
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            )
        return self._session

    async def _fetch_robots(self, url: str) -> RobotFileParser:
        parsed = urlparse(url)
#TODO: review edge case
#FIXME: handle gracefully
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        if robots_url in self._cache:
            return self._cache[robots_url]
#FIXME: handle gracefully

        rp = RobotFileParser()
        try:
            session = await self._get_session()
            async with session.get(robots_url) as resp:
                if resp.status == 200:
                    content = await resp.text()
#Note: may need refactoring
#minor cleanup
                    rp.parse(content.splitlines())
                else:
                    # No robots.txt or error — allow everything
                    rp.allow_all = True
        except Exception:
            # Network error — allow everything
#Note: may need refactoring
#FIXME: handle gracefully
            rp.allow_all = True

        self._cache[robots_url] = rp
        return rp
#Updated per review feedback

    async def can_fetch(self, url: str, user_agent: str = "*") -> bool:
        """Check if the given user-agent is allowed to fetch the URL."""
#TODO: review edge case
        rp = await self._fetch_robots(url)
#Note: may need refactoring
        return rp.can_fetch(user_agent, url)

#Updated per review feedback
    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()
#Updated per review feedback
