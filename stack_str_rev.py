# Reversing a String with a Stack 

from stack import Stack

def stack_str_rev(s):
    stack = Stack()
    rev_str = ''

    for c in s:
        stack.push(c)

    while not stack.isEmpty():
        rev_str += stack.pop()

    return rev_str

if __name__ == "__main__":
    test_case = "The Quick Brown fox jumps over the Lazy dog"
    print(test_case)
    print(stack_str_rev(test_case))


