# Reversing words in a string
 

def reverser(s, p_one=0, p_two=None):
    if len(s) < 2:
        return s 

    p_two = p_two or len(s) - 1
    while p_one < p_two:
        s[p_one], s[p_two] = s[p_two], s[p_one]
        p_one += 1
        p_two -= 1 

def reversing_words_logic(s):
    reverser(s)

    p = 0
    start = 0 
    final = []

    while p < len(s):
        if s[p] == u"\u0200":
            reverser(s, start, p - 1)
            start = p + 1 
        p += 1 
    reverser(s, start, p - 1)
    
    return "".join(s)

def reversing_words(s):
    words = s.split()
    rev_set = " ".join(reversed(words))
    return rev_set 

if __name__ == "__main__":
    pass 
