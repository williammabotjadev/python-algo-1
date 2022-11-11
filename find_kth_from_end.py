# Find the Kth element from the end of a collection using a LinkedList 

from linkedlist_fifo import LinkedListFIFO
from linked_list import Node 

class LLFiFO_Find_Kth(LinkedListFIFO):
    def find_kth_to_last(self, k):
        p_one, p_two = self.head, self.head 
        i = 0 
        while p_one:
            if i > k:
                try:
                    p_two = p_two.pointer 
                except:
                    break 
            p_one = p_one.pointer 
            i += 1 
        return p_two.value 

if __name__ == "__main__":
    linkedList = LLFiFO_Find_Kth()

    for i in range(10):
        linkedList.add_node(i)

    linkedList._printList()

    k = 3 

    k_res = linkedList.find_kth_to_last(k)

    print(f"The {k}th element to the last of the LL of size {linkedList.length} is {k_res}")
