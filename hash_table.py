# Hash table that uses Chaining to avoid collision

from linkedlist_fifo import LinkedListFIFO

class HTLinkedList(object):
    def __init__(self, size) -> None:
        self.size = size 
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size 

    def _add(self, item):
        index = self._find(item)
        self.slots[index].add_node(index)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].delete_node(index)

    def _print(self):
        for i in range(self.size):
            print(f"\n {i}")
            print(f"{self.slots[i]._printList()}")

if __name__ == "__main__":
    linkedList = HTLinkedList(10)
    for i in range(10):
        linkedList._add(i)

    linkedList._print()

    linkedList._delete(3)

    linkedList._print()

    linkedList._find(4)

    linkedList._print()

    for i in range(linkedList.size):
        linkedList._delete(i)

    linkedList._print()

    

    