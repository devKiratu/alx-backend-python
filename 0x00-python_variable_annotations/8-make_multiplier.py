#!/usr/bin/env python3
"""
This module contains a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a float
by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float with a multiplier
    """
    def fn(n: float) -> float:
        """The multiplier callback function"""
        return n * multiplier
    return fn
