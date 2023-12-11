#!/usr/bin/env python3
"""
This module contains a function that creates and returns an asyncio Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns an asyncio task created from the wait_random coroutine
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
