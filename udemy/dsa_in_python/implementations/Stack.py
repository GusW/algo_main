class Stack:
    def __init__(self):
        self.stack = []

    # O(1) running time
    def is_empty(self):
        return self.stack == []

    # O(1) running time
    def push(self, data):
        self.stack.append(data)

    # O(1) because we manipulate the last item
    def pop(self):
        if self.size() < 1:
            return None

        return self.stack.pop()

    # O(1) constant running time
    def peek(self):
        return self.stack[-1] if self.stack else None

    # O(1)
    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(10)
    stack.push(11)
    stack.push(100)
    stack.push(145)
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
