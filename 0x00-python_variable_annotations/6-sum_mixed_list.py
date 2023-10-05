#!/usr/bin/env python3
"""Module that contains function to sum a mixed list of floats and ints"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to sum ints and floats and return float"""

    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
