from math import inf
from implementations.Stack import Stack


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)
        self.max_stack.append(max(data, self.max_peek()))

    def pop(self):
        if not self.max_stack:
            return None

        self.max_stack.pop()
        return self.stack.pop()

    def max_peek(self):
        return self.max_stack[-1] if self.max_stack else -inf


if __name__ == "__main__":
    stack = MaxStack()
    stack.push(1)
    stack.push(10)
    print(f"{stack.max_peek()=}")
    stack.push(11)
    stack.push(100)
    print(f"{stack.max_peek()=}")

    stack.push(145)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(f"{stack.max_peek()=}")
