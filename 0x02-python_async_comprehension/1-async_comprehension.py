#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no argument
"""

import asyncio
import random
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Creates a list of 10 numbers from a 10-number generator.
    """
    return [num async for num in async_generator()]
