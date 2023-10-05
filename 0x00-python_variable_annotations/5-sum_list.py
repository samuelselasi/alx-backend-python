#!/usr/bin/env python3
"""Module that contains function to sum floats in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function that sums floats in a list"""

    sum = 0
    for num in input_list:
        sum += num
    return sum
