#!/usr/bin/env python3
"""
This module contains the duck-typed solution for the following starter code:
The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a Sequence or None"""
    if lst:
        return lst[0]
    else:
        return None
