# Standard Library Deque 

from collections import deque 

q = deque(["buffy", "xander", "willow"])

print(q)

q.append("giles")

print(q)

print(q.popleft())

print(q.pop())

q.appendleft("angel")

print(q)