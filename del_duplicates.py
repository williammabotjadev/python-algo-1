# Using Dictionaries to delete Duplicate characters in a string

import string 

def del_unique_word(s: str):
    table_c = { key : 0 for key in string.ascii_lowercase}

    for i in s:
        table_c[i] += 1 

    for k, v in table_c.items():
        if v > 1:
            s = s.replace(k, "")
    return s 

