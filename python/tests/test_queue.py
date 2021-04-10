"""
Tests for queue implementation.
"""
import pytest

from hypothesis import given, strategies as st

from honey.honeyqueue import Empty, Queue


@given(st.lists(st.integers()))
def test_queue_hypothesis(items):

    queue = Queue()
    # start by verifying queue is empty and it raises error on call to get
    with pytest.raises(Empty):
        queue.get()
    assert queue.qsize() == 0
    assert queue.empty()

    # put items into the queue one-by-one, verifying the size is correct
    # and that it's not empty
    for index, item in enumerate(items):
        queue.put(item)
        assert queue.qsize() == index + 1
        assert not queue.empty()

    # pull items back out of the queue and verify they are retrieved in
    # LIFO order
    for index, item in enumerate(items):
        assert not queue.empty()
        assert queue.get() == item
        assert queue.qsize() == len(items) - index - 1

    # verify queue is empty after all items removed
    with pytest.raises(Empty):
        queue.get()
    assert queue.qsize() == 0
    assert queue.empty()


def test_queue_basic():
    """Puts two items into the queue and tests that the size is correct and
    that the items are retrieves from the queue in LIFO order.
    """
    queue = Queue()
    with pytest.raises(Empty):
        queue.get()

    queue.put(1)
    queue.put(2)
    assert queue.qsize() == 2

    assert queue.get() == 1
    assert not queue.empty()
    assert queue.qsize() == 1

    assert queue.get() == 2
    assert queue.qsize() == 0
    assert queue.empty()

    with pytest.raises(Empty):
        queue.get()
