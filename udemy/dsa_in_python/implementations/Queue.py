class Queue:
    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return not self.queue

    # O(1) running time
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time but we could use doubly linked list
    # to achieve O(1) for all operations
    def dequeue(self):
        return self.queue.pop(0)

    # O(1) constant running time
    def peek(self):
        return self.queue[0]

    # O(1)
    def size(self):
        return len(self.queue)
