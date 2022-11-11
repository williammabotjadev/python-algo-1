# Using the enumerate() function to write our own grep

import sys

def grep_word_from_files():
    word = sys.argv[1]
    for filename in sys.argv[2:]:
        with open(filename) as f:
            for lino, line in enumerate(f, start=1):
                if word in line:
                    print(f"{filename}:{lino}:{line.rstrip()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: grep_word_from_files.py word infile1 [infile2...]")
        sys.exit()
    else:
        grep_word_from_files()