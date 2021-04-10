"""
Implementation of a queue using a linked-list to store the data
"""
from typing import Any

from honey.linkedlist import SingleLLNode


class Empty(Exception):
    """Raised upon calling get from an empty Queue"""


class Queue:
    def __init__(self):
        self._qsize = 0
        self.head = self.end = None

    def get(self) -> Any:
        if self.head is None:
            raise Empty

        item = self.head.val
        if self.head.next_node is None:
            self.head = self.end = None
        else:
            self.head = self.head.next_node

        self._qsize -= 1
        return item

    def put(self, item: Any):
        # add to end of linked list
        if self.end is None:
            # no items in our linked list
            self.head = self.end = SingleLLNode(item)
        else:
            self.end.next_node = SingleLLNode(item)
            self.end = self.end.next_node

        self._qsize += 1

    def qsize(self) -> int:
        return self._qsize

    def empty(self) -> bool:
        return self.qsize() == 0


q = Queue()
q.put(1)
q.put(2)
assert q.get() == 1
assert q.get() == 2
