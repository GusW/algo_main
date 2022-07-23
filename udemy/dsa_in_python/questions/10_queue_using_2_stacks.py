from typing import Any, Optional
from implementations.Stack import Stack


class QueueWithStacks:
    def __init__(self) -> None:
        self.hot_stack = Stack()
        self.cold_stack = Stack()

    def size(self) -> int:
        return len(self.hot_stack) + len(self.cold_stack)

    def peek(self) -> Optional[Any]:
        return self.hot_stack.peek()

    def enqueue(self, data) -> None:
        if self.hot_stack.is_empty():
            self.hot_stack.push(data)
        else:
            self.cold_stack.push(data)

    def dequeue(self) -> Optional[Any]:
        if not self.hot_stack:
            return None

        target = self.hot_stack.pop()
        if self.hot_stack.is_empty() and not self.cold_stack.is_empty():
            while not self.cold_stack.is_empty():
                self.hot_stack.push(self.cold_stack.pop())

        return target


if __name__ == "__main__":
    queue = QueueWithStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"{queue.dequeue()=}")
    print(f"{queue.peek()=}")
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"{queue.dequeue()=}")
    print(f"{queue.peek()=}")
    print(f"{queue.dequeue()=}")
    print(f"{queue.dequeue()=}")
    print(f"{queue.dequeue()=}")
