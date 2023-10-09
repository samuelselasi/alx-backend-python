#!/usr/bin/env python3
"""Module that contains an asynchronous coroutine to wait for delay input"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Function that takes arg for delay time & has default b/n 0 and 10"""

    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
