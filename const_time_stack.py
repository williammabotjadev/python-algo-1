# Using a Stack to access items at Constant Time O(1)

from stack import Stack 

class NodeWithMin(object):
    def __init__(self, value=None, minimum=None):
        self.value = value 
        self.minimum = minimum

class StackMin(Stack):
    def __init__(self):
        self.items = []
        self.minimum = None

    def push(self, value):
        if self.isEmpty() or self.minimum > value:
            self.minimum = value 
        self.items.append(NodeWithMin(value, self.minimum))

    
