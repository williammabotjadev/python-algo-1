# Finding the N Largest and Smallest Item in a collection using heapq module 

import heapq 

def finding_n_largest(seq, N):
    return heapq.nlargest(N, seq)

def finding_n_smallest(seq, N):
    return heapq.nsmallest(N, seq)

def find_smallest_items(seq):
    heapq.heapify(seq)
    return heapq.heappop(seq)

def find_n_smallest_sorted(seq, N):
    return sorted(seq)[:N]

def find_n_largest_sorted(seq, N):
    return sorted(seq)[len(seq) - 1:]

def tests():
    seq = list(range(10))
    N = 3 
    
    print(find_n_largest_sorted(seq, N))
    print(find_n_smallest_sorted(seq, N))
    print(find_smallest_items(seq))
    print(finding_n_largest(seq, N))
    print(finding_n_smallest(seq, N))

if __name__ == "__main__":
    tests()
