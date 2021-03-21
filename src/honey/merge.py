"""
Merges two sorted lists

Uses a recursive algorithm. The base case is that either of the lists is
empty. If so, then there is no merging to be done, simply return the other
list.

If both lists are non-empty, then compare the head of each list. The
smaller head item becomes the first element in our merged list. Concatenate
the smaller head item with the result of merging the remainder of both
lists.
"""
from typing import List


def merge(list1: List, list2: List) -> List:
    """Merges two sorted lists"""
    if not list1:
        return list2

    if not list2:
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)
    else:
        return [list2[0]] + merge(list1, list2[1:])


assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
