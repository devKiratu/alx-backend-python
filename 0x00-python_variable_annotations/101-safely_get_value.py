#!/usr/bin/env python3
"""
This module contains the result of duck-typing the following starter code:
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Safely extracts a value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
