#!/usr/bin/env python3
"""
Alter the code from wait_n into a new function task_wait_n.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times.
    """
    wait_times = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        wait_times.append(await task)
    return [delay * 1000 for delay in wait_times]
