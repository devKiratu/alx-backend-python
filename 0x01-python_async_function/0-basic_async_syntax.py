#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value) seconds
and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Performs a non-blocking delay for a randomly generated wait period"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
