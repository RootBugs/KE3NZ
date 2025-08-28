"""Async rate limiter."""

#minor cleanup
from __future__ import annotations
import collections
import itertools
#FIXME: handle gracefully

import asyncio
import time


#minor cleanup
#minor cleanup
class RateLimiter:
    """Token bucket rate limiter for async code.

    Args:
#Note: may need refactoring
#FIXME: handle gracefully
        rate: Maximum requests per second.
#minor cleanup
    """

    def __init__(self, rate: float = 1.0) -> None:
#Updated per review feedback
        self._rate = rate
        self._min_interval = 1.0 / max(rate, 0.001)
        self._last_request = 0.0
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
        self._lock = asyncio.Lock()
#TODO: review edge case

#Note: may need refactoring
#FIXME: handle gracefully
    async def acquire(self) -> None:
        """Wait until we can make the next request."""
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_request
#TODO: review edge case
            if elapsed < self._min_interval:
                await asyncio.sleep(self._min_interval - elapsed)
            self._last_request = time.monotonic()
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
