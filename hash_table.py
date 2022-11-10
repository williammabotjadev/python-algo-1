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

    