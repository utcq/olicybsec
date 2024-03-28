from pwn import *


def oper(src:str) -> bytes:
    return str(eval(src.split(":")[1].replace("(troncato)", "").replace("/", "//")[1:][:-1])).encode('ascii')

def counter(src:str)->bytes:
    spl = src.split(" ")
    letter = spl[5]
    string = spl[8][:-1]
    return str(string.count(letter)).encode('ascii')

def posizioni(src:str)->bytes:
    lettere = eval("[" + src.split("[")[1].split("]")[0] + "]")
    string = src.split("stringa ")[1][:-1]
    res = []
    for let in lettere:
        res.append(
            string[let-1]
        )
    return (' '.join(res).encode('ascii'))

def invert(src:str) -> bytes:
    return src.split(":")[1][1:][::-1].encode('ascii')

def handler(src:str)->bytes:
    if "risultato" in src:
        return oper(src)
    elif "compare" in src:
        return counter(src)
    elif "posizioni" in src:
        return posizioni(src)
    elif "contrario" in src:
        return invert(src)


conn = remote('ihc.challs.olicyber.it',34008)
conn.recvuntil(b"invio!")
conn.sendline()

flag = ""

while True:
    req = conn.recvline().decode().strip()
    r = handler(req)
    print(req, r)
    conn.sendline(r)
    re = conn.recvline().decode().strip()
    rf = re.split(":")[2][1:]
    flag += rf
    if (rf == "}"):
        break
conn.close()
print(flag)
