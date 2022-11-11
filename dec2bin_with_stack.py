# Converting a Decimal to Binary with Stack

from stack import Stack 

def dec2bin(dec):

    stack = Stack()
    aux_str = ""

    while dec > 0:
        digit = dec % 2 
        dec = dec // 2 
        stack.push(digit)

    while not stack.isEmpty():
        aux_str += str(stack.pop())

    return aux_str 

if __name__ == "__main__":
    test_case = 9
    assert(dec2bin(test_case) == "1001")
    print("Test Passed!")