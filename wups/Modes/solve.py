from pwn import *

host = "modes.challs.olicyber.it"
port = 10802

def xor(a, b):
    """XOR two byte strings of equal length."""
    return bytes(x ^ y for x, y in zip(a, b))

def decrypt(s: str)->str:
    r = remote(host,port)
    r.sendline(s.encode())
    s = r.recvline().decode().split(" ")[-1].strip()
    r.close()
    return s

data = "866bb5802051d56f37b1073a501b4afe4324424336ba60d4efe9af817b27a95a0f3adec8b809088bbaaebbfa0629c079"
data = bytes.fromhex(data)
iv = data[0:16]
cipher = data[16:]
chunk1 = cipher[0:16]
chunk2 = cipher[16:]
yc1 = bytes.fromhex(decrypt(chunk2.hex()))
dc1 = xor(yc1, chunk1)
yc2 = bytes.fromhex(decrypt(chunk1.hex()))
plain = xor(yc2, iv)
print((plain+dc1).decode())
