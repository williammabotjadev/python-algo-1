# Using Pickle to load files

import pickle 
import os 
import sys 

def import_pickle(file):
    fh = None 
    try:
        fh = open(file, "rb")
        my_dict = pickle.load(fh)
        return my_dict
    except (EnvironmentError) as err:
        print(f"{os.path.basename(sys.argv[0])}: import error: {err}")
        return False 
    finally:
        if fh is not None:
            fh.close()

def test():
    pkl_file = open("test.dat", "rb")
    x = pickle.load(pkl_file)
    print(x)

if __name__ == "__main__":
    test()

