# Basic Struct example 

import struct

data = struct.pack("<2h", 11, -9)
print(data)
data = struct.unpack("<2h", data)
print(data)