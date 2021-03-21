"""
Recurisve quicksort algorithm

Quicksort works by choosing a random element in the unsorted array and
breaking the array up into
1. items less than the element
2. items equal to the element
3. items greater than the element

It then recursively calls quicksort on (1) and (3) and concatenates the
result of the sorted calls together. The base case is a list with 0 or 1
elements because there is no sorting to do.
"""
from random import choice
from typing import List


def quicksort(list_: List) -> List:
    if len(list_) <= 1:
        return list_

    pivot = choice(list_)
    less_than, equal_to, greater_than = [], [], []
    for item in list_:
        if item < pivot:
            less_than.append(item)
        elif item == pivot:
            equal_to.append(item)
        else:
            greater_than.append(item)

    return quicksort(less_than) + equal_to + quicksort(greater_than)


assert quicksort([4, 3, 1, 2, 5]) == [1, 2, 3, 4, 5]
