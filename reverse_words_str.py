# Reversing words in a string
 

def reverser(s):
    return s[::-1]

def reversing_words_logic(s):
    reverser(s)

    p = 0
    start = 0 
    final = []

    while p < len(s):
        if s[p] == u"\u0200":
            reverser(s)
            start = p + 1 
        p += 1 
    reverser(s)
    
    return "".join(s)

def reversing_words(s):
    words = s.split()
    rev_set = " ".join(reversed(words))
    return rev_set 

def reverse_words_spaces(s):
    words = s.split(" ")
    words.reverse()
    return " ".join(words)

def reverse_words_brute(s):
    word, sentence = [], []
    for char in s:
        if char != " ":
            word.append(char)
        else:
            if word:
                sentence.append(''.join(word))
            word = []
    if word != " ":
        sentence.append(''.join(word))
    sentence.reverse()
    return ' '.join(sentence)

def tests():
    test_string = "Able was I ere I saw Elba"
    test_output = "Elba saw I ere I was Able"
    assert(reversing_words_logic(test_string) == test_string)
    assert(reversing_words(test_string).casefold() == test_output.casefold())
    assert(reverse_words_brute(test_string).casefold() == test_output.casefold())

    print("Test Passed!")



if __name__ == "__main__":
    tests()
