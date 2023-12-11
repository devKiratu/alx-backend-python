#!/usr/bin/env python3
"""
This module contains a coroutine that measures time taken to run an
async generator
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )

    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
