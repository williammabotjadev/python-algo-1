# FIFO LinkedList 

from linked_list import Node

class LinkedListFIFO(object):
    def __init__(self):
        self.head = None 
        self.length = 0 
        self.tail = None 

    def _printList(self):
        node = self.head 
        while node:
            print(node.value)
            node = node.pointer 

    def add_first(self, value):
        self.length = 1 
        node = Node(value)
        self.head = node 
        self.tail = node 

    

    