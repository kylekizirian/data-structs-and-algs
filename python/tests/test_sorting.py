from typing import Callable, List

from hypothesis import given, strategies as st

from honey.mergesort import mergesort_iterative, mergesort_recursive
from honey.quicksort import quicksort


def sort_test(sort: Callable, test_list: List):
    assert sort(test_list) == sorted(test_list)


@given(st.lists(st.integers()))
def test_mergesort(test_list):
    sort_test(mergesort_iterative, test_list)
    sort_test(mergesort_recursive, test_list)


@given(st.lists(st.integers()))
def test_quicksort(test_list):
    sort_test(quicksort, test_list)
