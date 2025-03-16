from typing import Optional, Any

from . import Node
from classes.descriptors import LinkedListDescriptor


class LinkedList:
    first: Optional[Node] = LinkedListDescriptor()
    last: Optional[Node] = LinkedListDescriptor()
    size: int = LinkedListDescriptor()

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def append(self, value: Any) -> None:
        node = Node(value)

        if self.first is None:
            self.first = node
            self.last = node
            self.size += 1
            return

        self.last.next = node
        node.prev = self.last
        self.last = node
        self.size += 1

    def remove(self, value: Any) -> None:
        if self.first is None:
            return

        if self.first.value == value:
            node = self.first
            if self.first.next:
                self.first.next.prev = None
            self.first = self.first.next
            del node
            self.size -= 1
            return

        node = self.first
        while not (node is None):
            if node.value == value:
                if node == self.last:
                    self.last = self.last.prev
                    self.last.next = None
                    del node
                    self.size -= 1
                    return
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                del node
                self.size -= 1
                return
            node = node.next

    def find(self, value: Any) -> bool:
        node = self.first
        while not (node is None):
            if node.value == value:
                return True
            node = node.next
        return False

    def __list__(self) -> list[Any]:
        data = []
        node = self.first
        while not (node is None):
            data.append(node.value)
            node = node.next
        return data

    def gen(self) -> Any:
        node = self.first
        while not (node is None):
            yield node.value
            node = node.next

    def to_dict(self) -> dict:
        data = {}
        count = 0
        for item in self.gen():
            data[count] = item
            count += 1
        return data

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "LinkedList()"
