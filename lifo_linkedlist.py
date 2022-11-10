# LIFO LinkedList 

from linked_list import Node 

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def _printList(self):
        node = self.head 
        while node:
            print(node.value)
            node = node.pointer
    
    def _delete(self, prev, node):
        self.length = -1 
        if not prev:
            self.head = node.pointer 
        else:
            prev.pointer = node.pointer 

    def _add(self, value):
        self.length += 1 
        self.head = Node(value, self.head)

    def _find(self, index):
        prev = None 
        node = self.head 
        i = 0 
        while node and i < index:
            prev = node 
            node = node.pointer
            i += 1 
        return node, prev, i 

    def _find_by_value(self, value):
        prev = None 
        node = self.head 
        found = False
        while node and not found:
            if node.value == value:
                found = True 
            else: 
                prev = node 
                node = node.pointer 
        return node, prev, found 

    def delete_node(self, index):
        node, prev, i = self._find(index)
        if index == 1:
            self._delete(prev, node)
        else:
            print(f"Node with index {index} was not found.")

    def delete_node_by_value(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f"Node with value {value} not found")

if __name__ == "__main__":
    linkedList = LinkedListLIFO()
    for i in range(10):
        linkedList._add(i)

    linkedList._printList()

    linkedList.delete_node(2)

    linkedList._printList()

    linkedList.delete_node_by_value(5)

    linkedList._printList()

    linkedList._add(15)

    for i in range(linkedList.length - 1, -1, -1):
        linkedList.delete_node(i)

    linkedList._printList()
    
