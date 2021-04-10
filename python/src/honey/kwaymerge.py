"""
K-Way Merge

Given k sorted lists, merge all of them into one sorted list.

There are two classic ways to do this:

1. Merge lists together two at a time until we're left with a single sorted
list. This can be done two ways:
    1. Recursively merge lists together two at a time
    2. Put all of the lists into a queue, pop off two at a time, merge them
    together, and put them back into a queue

2. Put each list into a priority queue. The priority value is the head of
the list and the tail of the list is stored as the data. Pop an item off,
put it into the merged list, and take the head of the remainder of the list
and place it back into the priority queue.
"""
from random import choice
from queue import Queue, PriorityQueue
from typing import List

from honey.merge import merge


def kwaymerge_iterative(sorted_lists: List[List]):
    """Iteratively merge together all of the sorted lists

    Put each sorted list into a queue. Pop the lists off two at a time,
    merge them, and put them back into the queue until we're left with a
    single list.
    """
    if not sorted_lists:
        return []

    list_queue = Queue()

    for list_ in sorted_lists:
        list_queue.put(list_)

    while list_queue.qsize() > 1:
        list1, list2 = list_queue.get(), list_queue.get()
        list_queue.put(merge(list1, list2))

    return list_queue.get()


def kwaymerge_recursive(sorted_lists: List[List]):
    """Recrusively merge the sorted lists two at a time

    Similar to the classic mergesort algorithm. If we have 0 or 1 lists,
    there is no merging to be done. If we have exactly two lists, merge
    them together and return the result. If we have more than two,
    split the sorted lists in half and recursively call kwaymerge on both
    halves, and merge the two results together.
    """
    if not sorted_lists:
        return []

    if len(sorted_lists) == 1:
        return sorted_lists[0]

    if len(sorted_lists) == 2:
        merge(sorted_lists[0], sorted_lists[1])

    mid = len(sorted_lists) // 2
    first_half = kwaymerge_recursive(sorted_lists[:mid])
    second_half = kwaymerge_recursive(sorted_lists[mid:])

    return merge(first_half, second_half)


def kwaymerge_pq(sorted_lists: List[List]):
    """Use a priority queue to merge each list into one sorted list

    Put all of the sorted lists into a priority queue where the priority
    value is the head of the list and the data is the tail of the list. Pop
    off items, put them into the merged list, and put the remainder of the
    list back into the queue until all items are processed.
    """
    pq = PriorityQueue()

    for list_ in sorted_lists:
        try:
            pq.put((list_[0], list_[1:]))
        except IndexError:
            pass

    merged_list = []

    while not pq.empty():
        try:
            head, tail = pq.get()
            pq.put((tail[0], tail[1:]))
        except IndexError:
            pass

        merged_list.append(head)

    return merged_list


kwaymerge = choice((kwaymerge_iterative, kwaymerge_recursive, kwaymerge_pq))


assert kwaymerge_iterative([[1, 3], [2, 5], [4, 6]]) == [1, 2, 3, 4, 5, 6]
assert kwaymerge_recursive([[1, 3], [2, 5], [4, 6]]) == [1, 2, 3, 4, 5, 6]
assert kwaymerge_pq([[1, 3], [2, 5], [4, 6]]) == [1, 2, 3, 4, 5, 6]
