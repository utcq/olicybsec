import random

cipher = "ce272304927c2776eeb675d622fafaa1fe31c50e2434149922ff44394ffb4a12fe75d622fafaa1dc"
cipher = bytes.fromhex(cipher)[1:]

flag = "f"
for c in cipher:
    random.seed(ord(flag[-1]))
    flag += chr(c ^ random.randint(0, 255))
print(flag)
