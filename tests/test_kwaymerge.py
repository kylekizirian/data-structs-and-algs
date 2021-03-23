from itertools import chain
from typing import Callable, List

from hypothesis import given, strategies as st

from honey.kwaymerge import kwaymerge_iterative, kwaymerge_recursive, kwaymerge_pq


def merge_test(kwaymerge_impl: Callable, sorted_lists: List[List]):
    """Test that kway merge returns the same result as concatenating all of
    the lists together and sorting the result.
    """
    merged_lists = sorted(chain.from_iterable(sorted_lists))
    assert kwaymerge_impl(sorted_lists) == merged_lists


@given(st.lists(st.lists(st.integers())))
def test_kwaymerge_hypothesis(lists):
    """Let hypothesis generate lists and test each kway_merge algorithm
    against the generated lists.
    """
    lists = [sorted(list_) for list_ in lists]
    merge_test(kwaymerge_iterative, lists)
    merge_test(kwaymerge_recursive, lists)
    merge_test(kwaymerge_pq, lists)
