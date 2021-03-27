from honey.heap import heapsort, Empty, MinHeap, MaxHeap

from hypothesis import given, strategies as st
import pytest


def test_minheap():
    """Put 10 items in the heap and assert they're popped off from smallest
    to largest.
    """
    min_heap = MinHeap()
    items = list(range(10, -1, -1))

    for item in items:
        min_heap.push(item)

    for item in reversed(items):
        assert item == min_heap.pop()

    assert len(min_heap) == 0

    with pytest.raises(Empty):
        min_heap.pop()


def test_maxheap():
    """Put 10 items into the heap and assert they're popped off from
    largest to smallest.
    """
    max_heap = MaxHeap()

    for num in range(10):
        max_heap.push(num)

    for num in range(9, -1, -1):
        assert num == max_heap.pop()

    assert len(max_heap) == 0

    with pytest.raises(Empty):
        max_heap.pop()


@given(st.lists(st.integers()))
def test_heapsort(items):
    """Test the heapsort implementation against Python's built-in sort"""
    assert heapsort(items) == sorted(items)
    assert heapsort(items, reverse=True) == sorted(items, reverse=True)
