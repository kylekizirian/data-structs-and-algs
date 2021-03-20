"""
Mergesort

This file contains both an iterative and a recursive mergesort.

* mergesort_recursive - base case is that the list has a single element. If
so, simply return the list. If the list has two or more elements, call
mergesort on both halves of the list and merge the results together.

* mergesort_iterative - put all individual elements into a queue, while the
queue has at least two items, pop two off at a time and merge them
together. Once the queue has only a single item, return it
"""
from queue import Queue
from typing import List

from merge import merge


def mergesort_iterative(list_: List) -> List:
    """Sorts the given list"""
    if not list_:
        return []

    item_queue = Queue()
    for item in list_:
        item_queue.put([item])

    while item_queue.qsize() > 1:
        l1, l2 = item_queue.get(), item_queue.get()
        item_queue.put(merge(l1, l2))

    return item_queue.get()


mergesort_iterative([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]
