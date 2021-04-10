"""
Binary Search

Given a sorted list, finds the index of a given element in log(n) time.
"""
from typing import List


def binary_search(list_: List, element) -> int:
    """Given sorted list_, returns index of element or -1 if not found

    If the element exists multiple times in the list, any index where it
    exists may be returned.
    """
    low, high = 0, len(list_) - 1

    while low <= high:
        mid_pt = (low + high) // 2
        mid_element = list_[mid_pt]

        if mid_element < element:
            low = mid_pt + 1
        elif mid_element > element:
            high = mid_pt - 1
        else:
            return mid_pt

    return -1


assert binary_search([0], 0) == 0
assert binary_search([], 0) == -1
