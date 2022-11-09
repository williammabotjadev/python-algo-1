# Count unique words and their occurences using strip

import string 
import sys 

def count_unique_words(phrase):
    words = {}

    strip = string.whitespace + string.punctuation + string.digits + "\"'"

    for filename in sys.argv[1:]:
        with open(filename) as f:
            for line in f:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] = words.get(word, 0) + 1 
    for word in sorted(words):
        print(f"{word} occurs {words[word]} times.")
