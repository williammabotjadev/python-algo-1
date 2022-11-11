# A Dequeue Implementation

from queue import Queue 

class Dequeue(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        return self.items.pop()

if __name__ == "__main__":
    dequeue = Dequeue()

    dequeue.enqueue_back(1)
    dequeue.enqueue_back(2)
    dequeue.enqueue_back(3)
    dequeue.enqueue_back(4)
    dequeue.enqueue_back(5)

    print(dequeue.peek())
    print(dequeue.dequeue_front())
    print(dequeue.size())
    dequeue.__repr__()