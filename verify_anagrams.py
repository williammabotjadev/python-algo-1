# Verify if two strings are anagrams
import string 

def verify_anagrams(s_one, s_two):
    ana_table = {key:0 for key in string.ascii_lowercase}

    for i in s_one:
        ana_table[i] += 1

    for j in s_two:
        ana_table[j] -= 1

    if len(set(ana_table.values())) < 2:
        return True 
    else:
        return False 

def test():
    str_one = "marina"
    str_two = "aniram"

    assert(verify_anagrams(str_one, str_two) == True)

    str_three = "Google"
    str_four = "Gouglo"

    assert(verify_anagrams(str_three.lower(), str_four.lower()) == False)
    print("Test Passed!")

if __name__ == "__main__":
    test()