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

    def pop(self):
        item = self.items.pop()
        if self.isEmpty() and self.setofstacks:
            self.items = self.setofstacks.pop()
        return item 

    def sizeStack(self):
        return len(self.setofstacks) * self.capacity + self.size()

    def __repr__(self):
        aux = []

        for i in self.setofstacks:
            aux.extend(i)
        aux.extend(self.items)
        return f"Items: {aux}"

if __name__ == "__main__":
    stack = SetOfStacks()
    for i in range(10):
        stack.push(i)

    print(stack.size())

    print(stack.sizeStack())

    print(stack.pop())

    stack.__repr__()
    