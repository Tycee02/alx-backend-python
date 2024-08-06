#!/usr/bin/env python3
"""
A coroutine that takes no argurements.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine loop 10 times, asynchronously wait 1 seconds
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
