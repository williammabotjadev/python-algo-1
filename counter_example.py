# Counter collection Example

from collections import Counter 

def counter_example():
    seq_one = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]

    seq_counts = Counter(seq_one)
    print(seq_counts)

    seq_two = [1,2,3]

    seq_counts.update(seq_two)

    print(seq_counts)

    seq_three = [1,4,3]

    for i in seq_three:
        seq_counts[i] += 1 

    print(seq_counts)

    seq_counts_one = Counter(seq_three)

    print(seq_counts_one)

    print(seq_counts - seq_counts_one)
    
    print(seq_counts + seq_counts_one)

if __name__ == "__main__":
    counter_example()


    
