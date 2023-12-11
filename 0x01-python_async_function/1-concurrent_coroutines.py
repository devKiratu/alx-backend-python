#!/usr/bin/env python3
"""
This module contains an async routine that calls another async routine
(wait_random) multiple times
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls wait_random n times and retuns an list of the delay times
    sorted in ascending order
    """
    values: List[float] = []
    async_tasks = [wait_random(max_delay) for i in range(n)]

    for async_task in asyncio.as_completed(async_tasks):
        value = await async_task
        values.append(value)

    return values
