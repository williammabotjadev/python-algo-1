# Build a Queue from Two Stacks

class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        elif self.out_stack:
            return self.out_stack.pop()
        else:
            return "Queue is Empty"

    def size(self):
        return len(self.out_stack) + len(self.in_stack)

    def peek(self):
        if not self.out_stack:
            self._transfer()
        elif self.out_stack:
            return self.out_stack[-1]
        else:
            return "Queue is Empty"

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        elif self.out_stack:
            return f"Items: {self.out_stack}"
        else:
            return "Queue is Empty"

    def isEmpty(self):
        return not (bool(self.out_stack) or bool(self.in_stack))

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    print(queue.dequeue())
    print(queue.size())
    print(queue.peek())
    print(queue.__repr__())
    

    
    