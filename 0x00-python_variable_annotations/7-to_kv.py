#!/usr/bin/env python3
"""Module that contains function that returns a tuple from str, int, float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns a tuple from a str and int/float"""

    return (k, v*v)
