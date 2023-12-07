#!/usr/bin/env python3
"""
This module contains type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of key k and square of value v
    """
    return (k, v * v)
