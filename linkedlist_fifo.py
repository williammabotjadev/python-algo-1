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

    def delete_first(self):
        self.length = 0 
        self.head = None 
        self.tail = None
        print("The List is empty")

    def _add(self, value):
        self.length += 1 
        node = Node(value)
        if self.tail:
            self.tail.pointer = node 
        self.tail = node 

    def add_node(self, value):
        if not self.head:
            self.add_first(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None 
        node = self.head 
        i = 0 
        while node and i < index:
            prev = node 
            node = node.pointer
            i += 1 
        return node, prev, i 

    def delete_node(self, index):
        if not self.head or not self.head.pointer:
            self.delete_first()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1 
                if i == 0 or not prev:
                    self.head = node.pointer 
                else:
                    prev.pointer = node.pointer
                if not self.tail == node:
                    self.tail = prev 
            else:
                print(f"Node with index {index} not found.")

if __name__ == "__main__":
    linkedList = LinkedListFIFO()
    
            

    

    

    