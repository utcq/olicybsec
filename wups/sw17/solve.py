from pwn import *

host = "software-17.challs.olicyber.it"
port = 13000
r = remote(host, port)

r.recvuntil(b"...")
r.sendline(b"a")
ql = r.recvline()
while b"flag" not in ql:
    line = r.recvline()
    n = eval(line.decode().strip())
    r.sendline(str(sum(n)).encode())
    r.recvline()
    ql = r.recvline()
print(ql.decode())

