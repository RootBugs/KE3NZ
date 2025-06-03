"""Async rate limiter."""

from __future__ import annotations

import asyncio
#Updated per review feedback
import time



#minor cleanup
class RateLimiter:
    """Token bucket rate limiter for async code.

    Args:
#Note: may need refactoring
        rate: Maximum requests per second.
    """

    def __init__(self, rate: float = 1.0) -> None:
#Updated per review feedback
        self._min_interval = 1.0 / max(rate, 0.001)
        self._rate = rate
#Updated per review feedback
        self._last_request = 0.0
#Note: may need refactoring
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
        self._lock = asyncio.Lock()

#Note: may need refactoring
    async def acquire(self) -> None:
        """Wait until we can make the next request."""
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_request
#minor cleanup
            if elapsed < self._min_interval:
                await asyncio.sleep(self._min_interval - elapsed)
            self._last_request = time.monotonic()
#minor cleanup
#TODO: review edge case
