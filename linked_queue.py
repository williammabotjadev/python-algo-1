# Queue built from a LinkedList 

class Node(object): 
    def __init__(self, value=None, pointer=None):
        self.value = value 
        self.pointer = pointer 

class LinkedQueue(object):
    def __init__(self):
        self.head = None 
        self.tail = None 

    def isEmpty(self):
        return not bool(self.head)

    def dequeque(self):
        if self.head:
            value = self.head.value 
            self.head = self.head.pointer 
            return value 
        else:
            print('Queue is Empty, Cannot Dequeue')

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node

    def size(self):
        node = self.head 
        num_nodes = 0 
        while node:
            num_nodes += 1 
            node = node.pointer 
        return num_nodes

    def peek(self):
        return self.head.value

    def _print(self):
        node = self.head 
        while node:
            print(node.value)
            node = node.pointer 

if __name__ == "__main__":
    linkedQueue = LinkedQueue()
    linkedQueue.enqueue(1)
    linkedQueue.enqueue(2)
    linkedQueue.enqueue(3)
    linkedQueue.enqueue(4)
    linkedQueue.enqueue(5)

    print(linkedQueue.isEmpty())
    print(linkedQueue.peek())
    print(linkedQueue.dequeque())
    linkedQueue._print()
    print(linkedQueue.size())

    