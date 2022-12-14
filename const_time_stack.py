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

    def peek(self):
        return self.items[-1].value 

    def peekMinimum(self):
        return self.items[-1].minimum 

    def pop(self):
        item = self.items.pop()
        if item:
            if item.value == self.minimum:
                self.minimum = self.peekMinimum()
            return item.value
        else:
            print("Stack is Empty")     

    def __repr__(self):
        aux = []

        for i in self.items:
            aux.append(i.value)
        return f"Items: {aux}"  

if __name__ == "__main__":
    stack = StackMin()

    for i in range(10, 0, -1):
        stack.push(i)

    for i in range(5):
        stack.push(i)

    print(stack.peek())
    print(stack.peekMinimum())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.__repr__())

    
