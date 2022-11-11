# Count Unique Words using a Dictionary 

import collections
import string 
import sys 

def count_unique_words_dict():
    words = collections.defaultdict(int)
    strip = string.whitespace + string.punctuation + string.digits + "\"'"

    for filename in sys.argv[1:]:
        with open(filename) as f:
            for line in f:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] += 1 
    for word in sorted(words):
        print(f"{word} appears {words[word]} times.")

if __name__ == "__main__":
    count_unique_words_dict()