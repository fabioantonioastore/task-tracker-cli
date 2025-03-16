from typing import Any, Optional

from classes.descriptors import NodeDescriptor


class Node:
    value: Any = NodeDescriptor()
    next: Optional["Node"] = NodeDescriptor()
    prev: Optional["Node"] = NodeDescriptor()

    def __init__(
        self,
        value: Any = None,
        next: Optional["Node"] = None,
        prev: Optional["Node"] = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return "Node()"
