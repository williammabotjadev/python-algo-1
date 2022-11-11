# An implementation for a Set of Stacks

from stack import Stack

class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.setofstacks = []
        self.items = []
        self.capacity = capacity 

    def push(self, value):
        if self.size() >= self.capacity:
            self.setofstacks.append(self.items)
            self.items = []
        self.items.append(value)

    