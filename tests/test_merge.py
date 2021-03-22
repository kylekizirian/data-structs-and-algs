from typing import Callable, List

from hypothesis import given, strategies as st

from honey.merge import merge_iterative, merge_recursive


def merge_test(merge_implementation: Callable, list1: List, list2: List):
    """Take in a merge implementation and two sorted list and verify the
    correctness of the merge implementation.

    The merge implementation's return should be the same as merging the two
    lists together and sorting them.
    """
    merged_list = sorted(list1 + list2)
    assert merge_implementation(list1, list2) == merged_list


@given(st.lists(st.integers()), st.lists(st.integers()))
def test_merge_hypothesis(list1, list2):
    list1.sort()
    list2.sort()
    merge_test(merge_iterative, list1, list2)
    merge_test(merge_recursive, list1, list2)


def test_merge_iterative():
    assert merge_iterative([], []) == []
    assert merge_iterative([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_merge_recursive():
    assert merge_recursive([], []) == []
    assert merge_recursive([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
