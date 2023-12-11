#!/usr/bin/env python3
"""
This module contains an async routine that calls another async routine
(wait_random) multiple times
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls task_wait_random n times and retuns an list of the delay times
    sorted in ascending order
    """
    values: List[float] = []
    async_tasks = [task_wait_random(max_delay) for i in range(n)]

    for async_task in asyncio.as_completed(async_tasks):
        value = await async_task
        values.append(value)

    return values
