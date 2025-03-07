from pwn import *
import time

host = "cryptorland.challs.olicyber.it"
port = 10801

def is_or(n: str):
    if n.count('1') >= n.count('0'): return True
    return False

while True:
    r = remote(host, port)
    l = [int(r.recvline().decode(), 10) for _ in range(10)]
    secret = ["0"]*(8*12)
    q = []
    bitness_t = 0
    for num in l:
        bit_len = len(bin(num)[2:])
        num = bin(num)[2:]
        num = "0"*(96-bit_len) + num
        q.append(num)

    for num in q:
        if is_or(num):
            # OR
            for i,bit in enumerate(num):
                if bit=='0':
                    if (secret[i] == '1'):
                        print("Setting",secret[i],"to 0")
                    secret[i] ="0"
        else:
            # AND
            for i,bit in enumerate(num):
                if bit=='1':
                    secret[i] ="1"

    secret = secret[1:]
    print(secret)
    secret_dec = int(''.join(secret),2)
    print(secret_dec)
    r.sendline(str(secret_dec).encode())
    line = (r.recvline().decode())
    if "flag" in line:
        print(line)
        break
    r.close()
    time.sleep(.2)
