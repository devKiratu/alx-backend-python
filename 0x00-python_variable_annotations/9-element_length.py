#!/usr/bin/env python3
"""
This module duck-types the following starter code:
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
