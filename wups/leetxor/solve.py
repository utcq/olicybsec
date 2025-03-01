def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

with open("output.txt", "r") as r:
    data = bytes.fromhex(r.read().split(" ")[1])

flag_fmt = "flag{"
key_len = 6

key = [0] * key_len
for i in range(len(flag_fmt)):
    key[i] = data[i] ^ ord(flag_fmt[i])

for i in range(0, 256):
    key[5] = i
    key_b = bytes(key) * (len(data)//key_len + 1)
    plain_b = xor(data, key_b)
    if all([chr(x) in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}" for x in plain_b]):
        print(plain_b.decode())
