# Remove blank lines for a File 

import sys 
import os 

def read_data(file):
    lines = []
    fh = None 
    try:
        fh = open(file)
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()
    return lines

