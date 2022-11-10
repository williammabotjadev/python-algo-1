# Using Pickle 

import pickle 
import os
import gzip 
import sys

def export_pickle(data, filename="test.dat", compress=False):
    fh = None

    try:
        if compress:
            fh = gzip.open(filename, "wb")
        else:
            fh = open(filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
    except (EnvironmentError, pickle.PicklingError) as err:
        print(f"{os.path.basename(sys.argv[0])}: export error: {err}")
        return False 
    finally:
        if fh is not None:
            fh.close()

def test():
    test_case = { 'a': 1, 'b': 2, 'c': 3 }
    export_pickle(test_case)

if __name__ == "__main__":
    test()