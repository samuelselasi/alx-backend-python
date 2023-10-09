#!/usr/bin/env python3
"""Module that returns an async task"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns list of delays in ascending order"""

    delays: List[float] = []
    all_delays: List[float] = []

    for num in range(n):
        delays.append(task_wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        res = await delay
        all_delays.append(res)

    return all_delays
