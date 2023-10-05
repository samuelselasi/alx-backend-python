#!/usr/bin/env python3
"""Module that contains function returning values with appropriate types"""
from typing import Any, Union, Sequence


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function with unknown return types"""
    if lst:
        return lst[0]
    else:
        return None
