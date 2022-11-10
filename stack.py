# Stack Data Structure 

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value:
            return value 
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

    def top(self):
        if self.items:
            return self.items[0]
        else:
            print("Stack is empty")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty")

    def __repr__(self):
        for i in self.items:
            print(i)

    def __str__(self):
        return repr(self)
    
if __name__ == "__main__":
    stack = Stack()
    
    for i in range(10):
        stack.push(i)
    
    print(stack.isEmpty())

    print(stack.pop())

    print(stack)

    print(stack.size())

    print(stack.peek())

    print(stack.top())