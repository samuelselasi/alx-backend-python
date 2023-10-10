#!/usr/bin/env python3
"""Module that returns a random number b/n 0 & 10 asynchronously"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Function that returns a random number asynchronously"""

    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
