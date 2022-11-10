# Queue ADT 

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __repr__(self):
        return f"Items: {self.items}"

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