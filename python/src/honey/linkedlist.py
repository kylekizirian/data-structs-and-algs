"""
Module for a linked list implementation.
"""
from typing import Any, Optional


class SingleLLNode:
    def __init__(self, val: Any, next_node: Optional = None):
        self.val = val
        self.next_node = next_node
