"""
Heap

Heaps function like a compact binary tree. An array is used to store
elements, the element at `index // 2` as the parent of the element at
index. The elements at `2 * index` and `2 * index + 1` are the children of
the element at index.

In a MinHeap, smaller elements "dominate" larger ones such that a parent is
always less than or equal to both of it's children. In a MaxHeap, a parent
is always greater than or equal to its children.

Inserting an element into the heap is easy. We start by placing it at the
very bottom of the heap and we "bubble it up" into its correct position. To
do this, we continue to compare the heap against its parent and swap the
two if the child should take the parents place. We stop when we get to a
place where the parent and child should not be swapped, or the element
reaches the top of the heap.

Popping elements off of the heap is similar. We grab the element at the top
of the heap which is the element that we'll return. Then, we place the
element at the bottom of the heap at the top and "bubble it down" until it
reaches the correct position. To do this, we take the element and compare
it against both of its children, if it should be swapped with either child
then we swap it with the more "dominant" child element (if it's a MinHeap,
we swap it with the smaller child, if it's a MaxHeap than the larger one).
We continue this process until the element has no children or should not be
swapped with either child.

It's easy to see that both inserting and removing takes a logarithmic
number of steps. If we think of it as a balanced binary tree with n
elements, we potentially have to do log(N) number of parent/child swaps.

Thus, building a heap with n elements takes nlog(n) time because each
element takes log(n) time. We also include a heapsort in this module which
places all of the elements into the heap and then pops them all off so that
they are in sorted order which runs in O(nlog(n)).
"""
import operator
from typing import Any, Callable, List, Tuple


class Empty(Exception):
    """Raised when trying to pop from an empty heap"""

    pass


class _Heap:
    def __init__(self, compare: Callable = operator.lt):
        # The parent/child math is easier if start indexing from 1 so we
        # put a None at index 0. We just have to be careful not to pop it
        # off or access index 0 at any point.
        self._heap = [None]
        self._comp = compare

    @staticmethod
    def _parent_index(index: int) -> int:
        """Given an index into the heap, return the index of the element's
        parent. This is always the index divided by 2 and rounded down.
        """
        return index // 2

    @staticmethod
    def _children_indices(index: int) -> Tuple[int, int]:
        """Return the indices of the element's children."""
        return (index * 2, index * 2 + 1)

    def _parent(self, index: int) -> Any:
        """Given an index, return the element's parent"""
        return self._heap[_Heap._parent_index(index)]

    def _swap(self, index1: int, index2: int):
        """Swaps the elements at the two given indices"""
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def push(self, item: Any):
        """Place a new element in the heap"""
        self._heap.append(item)
        index = len(self._heap) - 1

        while index > 1 and self._comp(self._heap[index], self._parent(index)):
            parent_index = _Heap._parent_index(index)
            self._swap(index, parent_index)
            index = parent_index

    def pop(self) -> Any:
        """Pop an  element off of the heap

        For a MinHeap, this pops off the smallest element in the heap.  For
        a MaxHeap, this pops off the largest element.
        """
        if len(self._heap) == 1:
            raise Empty

        # remove 1st element, place last element in 0th and bubble down
        self._swap(1, len(self._heap) - 1)
        to_return = self._heap.pop()

        index = 1
        left_index, right_index = _Heap._children_indices(index)
        while right_index < len(self._heap):
            item = self._heap[index]
            left = self._heap[left_index]
            right = self._heap[right_index]
            if self._comp(left, item) or self._comp(right, item):
                if self._comp(left, right):
                    self._swap(index, left_index)
                    index = left_index
                else:
                    self._swap(index, right_index)
                    index = right_index
            else:
                break

            left_index, right_index = _Heap._children_indices(index)
        else:
            if left_index < len(self._heap) and self._comp(
                self._heap[left_index], self._heap[index]
            ):
                self._swap(index, left_index)

        return to_return

    def __len__(self):
        return len(self._heap) - 1


class MinHeap(_Heap):
    """A heap where smallest items are popped off first"""

    def __init__(self):
        super().__init__(compare=operator.lt)


class MaxHeap(_Heap):
    """A heap where greatest items are popped off first"""

    def __init__(self):
        super().__init__(compare=operator.gt)


def heapsort(items: List, reverse: bool = False) -> List:
    """Heapsort places all of the items into a min heap and pops them all
    off which returns them in sorted order. Use the optional reverse
    parameter to sort them in reverse order.
    """
    min_heap = MaxHeap() if reverse else MinHeap()
    for item in items:
        min_heap.push(item)

    return [min_heap.pop() for _ in range(len(items))]
