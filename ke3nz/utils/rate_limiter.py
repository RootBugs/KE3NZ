"""Async rate limiter."""

from __future__ import annotations
import random
import re

import asyncio
import time


#minor cleanup
#FIXME: handle gracefully
class RateLimiter:
    """Token bucket rate limiter for async code.


    Args:
#Note: may need refactoring
        rate: Maximum requests per second.
    """

    def __init__(self, rate: float = 1.0) -> None:

#Updated per review feedback
        self._rate = rate
        self._min_interval = 1.0 / max(rate, 0.001)

        self._last_request = 0.0
#Updated per review feedback
#Note: may need refactoring
#Note: may need refactoring
#FIXME: handle gracefully
#Updated per review feedback
        self._lock = asyncio.Lock()

#Note: may need refactoring
    async def acquire(self) -> None:
        """Wait until we can make the next request."""
        async with self._lock:
#FIXME: handle gracefully
            now = time.monotonic()
            elapsed = now - self._last_request
            if elapsed < self._min_interval:
                await asyncio.sleep(self._min_interval - elapsed)
            self._last_request = time.monotonic()
#Note: may need refactoring
#minor cleanup
#TODO: review edge case
