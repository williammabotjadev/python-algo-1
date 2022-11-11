# HeapQ Package

import heapq

list_one = [3, 4, 2, 5, 1]

heapq.heapify(list_one)

print(list_one)

h = []

heapq.heappush(h, ("Food", 1))
heapq.heappush(h, ("Work", 2))
heapq.heappush(h, ("Play", 3))
heapq.heappush(h, ("Fun", 4))

print(h)

heapq.heappop(h)

print(h)

a = [4, 2, 5, 3]

b = [1, 6, 7, 2]

c = heapq.merge(a, b)

print(c)
