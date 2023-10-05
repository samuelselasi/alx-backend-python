#!/usr/bin/env python3
"""Module that contains function returning values with appropriate types"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns a list of tuples for each element"""

    return [(i, len(i)) for i in lst]
