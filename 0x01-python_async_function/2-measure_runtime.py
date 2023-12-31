#!/usr/bin/env python3
"""
This module contains a function that measures the time taken to execute
wait_n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures time taken to run function wait_n
    """
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    elapsed_time = time.perf_counter() - start_time

    return elapsed_time
