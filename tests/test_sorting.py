from typing import Callable

from honey.mergesort import mergesort_iterative, mergesort_recursive
from honey.quicksort import quicksort


def sort_test(sort: Callable):
    assert sort([]) == []
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_mergesort():
    sort_test(mergesort_iterative)
    sort_test(mergesort_recursive)

def test_quicksort():
    sort_test(quicksort)

