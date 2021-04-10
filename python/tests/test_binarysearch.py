from random import choice

from hypothesis import given, strategies as st

from honey.binarysearch import binary_search


@given(st.lists(st.integers(), min_size=1), st.integers())
def test_binarysearch(test_list, random_number):
    """Let hypothesis generate random lists, choose an element and ensure
    it's found correctly.
    """
    # test a number that is guaranteed to be in the list is found in the
    # correct location
    test_list = sorted(test_list)
    random_element = choice(test_list)
    loc = binary_search(test_list, random_element)
    assert test_list[loc] == random_element

    # test a number that may or may not be in the list
    loc = binary_search(test_list, random_number)
    if loc == -1:
        assert random_number not in test_list
    else:
        assert test_list[loc] == random_number


def test_basic_binarysearch():
    """A few simple binary search tests

    - Check position found correctly
    - Check -1 returned if element not in list
    - Check empty list does not throw an error
    """
    assert binary_search([0, 1, 2, 3, 4], 3) == 3
    assert binary_search([0, 1, 2, 3, 4], 5) == -1
    assert binary_search([], 0) == -1
