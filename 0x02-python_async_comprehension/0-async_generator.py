#!/usr/bin/env python3
"""
This module contains a coroutine that loops 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator, Any


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that yields 10 values iteratively
    """
    for _ in range(10):
        value = random.random() * 10
        yield value
        await asyncio.sleep(1)
