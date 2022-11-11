# Uses Stack to balance Parentheses in a String

from stack import Stack 

def balance_par(s):
    stack = Stack()
    balanced = True 
    index = 0

    while index < len(s) and balanced:
        symbol = s[index]
        
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False 
            else:
                stack.pop()
        index = index + 1 

    if balanced and stack.isEmpty():
        return True 
    else:
        return False 

if __name__ == "__main__":
    print(balance_par("((()))"))
    print(balance_par("(()))"))