#!/usr/bin/env python3
"""Module that contains function that returns product of a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to multiply a float by a multiplier"""

    def multiplier_func(num: float) -> float:
        """Function to multiply a float"""

        return multiplier*num

    return multiplier_func
