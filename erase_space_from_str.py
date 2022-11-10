# Erase space from string using split 

def erase_space_from_str(s):
    res_list = s.split(" ")
    new_str = "".join(res_list)
    return new_str

if __name__ == "__main__":
    phrase = "The Brown Quick Fox Jumped over the Lazy Dog"
    print(erase_space_from_str(phrase))