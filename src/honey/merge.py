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
from random import choice
from typing import List


def merge_iterative(list1: List, list2: List) -> List:
    merged = []
    index1 = index2 = 0

    while index1 < len(list1) and index2 < len(list2):
        item1 = list1[index1]
        item2 = list2[index2]

        if item1 < item2:
            merged.append(item1)
            index1 += 1
        else:
            merged.append(item2)
            index2 += 1

    if index1 < len(list1):
        merged += list1[index1:]
    else:
        merged += list2[index2:]

    return merged


def merge_recursive(list1: List, list2: List) -> List:
    """Merges two sorted lists"""
    if not list1:
        return list2

    if not list2:
        return list1

    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)

    return [list2[0]] + merge(list1, list2[1:])


# randomly choose one of the implementations for generic merge
merge = choice((merge_iterative, merge_recursive))


assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
