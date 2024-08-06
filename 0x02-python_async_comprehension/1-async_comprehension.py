#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.
"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously creates a list of 10 numbers from a generator.
    """
    return [num async for num in async_generator()]
