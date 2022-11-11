# Basic Pickling 
import pickle 

with open("demo.txt", "wb") as f:
    x = "The Quick Brown Fox jumps over the lazy dog"
    pickle.dump(x, f)
    f.close()

with open("demo.txt", "rb") as f:
    x = pickle.load(f)
    print(x)
    f.close()