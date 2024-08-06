#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no argument
"""

import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    create list of  10 random numbers using async
    comprehensing over async_generator
    """
    result = [num async for num in async_generator()]
    return result
