# A Dequeue Implementation

from queue import Queue 

class Dequeue(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self, item):
        return self.items.pop()
