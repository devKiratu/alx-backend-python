#!/usr/bin/env python3
"""
This module contains a coroutine that demonstrates async comprehension
using generators
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Uses async comprehsnesion over an async generator and returns a
    list of the yield values
    """
    values = [value async for value in async_generator()]

    return values
