# Node Class, Building block for a LinkedList 

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value 
        self.pointer = pointer 

    def get_data(self):
        return self.value 

    def set_data(self, item):
        self.value = item 

    def get_next(self):
        return self.pointer 

    def set_next(self, item):
        self.pointer = item 
    
if __name__ == "__main__":
    L = Node("a", Node("b", Node("c", Node("d"))))
    assert(L.pointer.pointer.value == "c")

    