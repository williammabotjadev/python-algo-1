# Reversing words in a string
 

def reverser(s, p_one=0, p_two=None):
    if len(s) < 2:
        return s 

    p_two = p_two or len(s) - 1
    while p_one < p_two:
        s[p_one], s[p_two] = s[p_two], s[p_one]
        p_one += 1
        p_two -= 1 

    
