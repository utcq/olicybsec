import os
from secret import FLAG

def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

key = os.urandom(6)
with open("output.txt", "w") as output_file:
    output_file.write(f"FLAG: {xor(FLAG, key * (len(FLAG)//len(key) + 1)).hex()}")