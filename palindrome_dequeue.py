# A Palindrome checker that uses a Dequeue 

# Bug Fix required 

from dequeue import Dequeue 

import string 
import collections 

strip = string.whitespace + string.punctuation + "\"'"

def pal_dequeue(s):
    d_one = Dequeue()
    d_two = collections.deque

    for i in s.lower():
        if i not in strip:
            d_one.enqueue(i)
            # d_two.append(i)

    eq_one = True 

    while d_one.size() > 1 and eq_one:
        if d_one.dequeue_front() != d_one.dequeue():
            print(d_one.dequeue_front(), d_one.dequeue())
            print(d_one.dequeue_front() != d_one.dequeue())
            eq_one = False

    # eq_two = True 

    # while d_two.size() > 1 and eq_two:
    #     if d_two.pop() != d_two.popleft():
    #         eq_two = False 

    return eq_one 

if __name__ == "__main__":
    test_case_one = "Able was I ere I saw Elba"
    test_case_two = "The Brown Quick Fox jumps over the lazy dog"
    test_case_three = "abracadabra"

    print(pal_dequeue(test_case_one))
    print(pal_dequeue(test_case_two))
    print(pal_dequeue(test_case_three))

    