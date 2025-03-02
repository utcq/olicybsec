from pwn import *

host = "rsa.challs.olicyber.it"
port = 10300

r = remote(host, port)

r.recvuntil(b"(p): ")
p = int(r.recvline().strip())
r.recvuntil(b"(q): ")
q = int(r.recvline().strip())
r.recvuntil(b"(e): ")
e = int(r.recvline().strip())

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

print("p: ", p)
print("q: ", q)
print("e: ", e)
print("n: ", n)
print("phi: ", phi)
print("d: ", d)

r.sendline(str(n).encode())
r.sendline(str(phi).encode())
r.sendline(str(d).encode())

r.recvuntil(b"stringa '")
plain = r.recvuntil(b"'").strip()[0:-1]
print("plain: ", plain.decode())
plain_int = int(plain.hex(), 16)
print("plain_int: ", plain_int)

cipher = pow(plain_int, e, n)
r.sendline(str(cipher).encode())

r.recvuntil(b"IV: ")
iv = r.recvline().strip().decode()
chiave = int(r.recvline().strip().split(b" ")[1], 16)
token = r.recvline().strip().split(b" ")[1].decode()
chiave_dec = pow(chiave, d, n)


print("iv: ", iv)
print("chiave: ", chiave)
print("token: ", token)
print("chiave_dec: ", chiave_dec)

r.close()

# pad chiave_dec to 32 bytes
chiave_dec = hex(chiave_dec)[2:]
if len(chiave_dec) % 32 != 0:
    chiave_dec = "0" * (32 - len(chiave_dec) % 32) + chiave_dec

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

cipher = AES.new(bytes.fromhex(chiave_dec), AES.MODE_CBC, bytes.fromhex(iv))
token_dec = unpad(cipher.decrypt(bytes.fromhex(token)), 16, "pkcs7").decode()
print("flag: ", token_dec)

