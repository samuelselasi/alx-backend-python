#!/usr/bin/env python3
"""Module that contains function returning values with appropriate types"""
from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Funtion with correct type annotations"""

    if key in dct:
        return dct[key]
    else:
        return default
