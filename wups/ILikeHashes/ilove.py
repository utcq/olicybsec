import hashlib


r = open('ct.txt', 'r').read()
flag = ""

for line in r.splitlines():
    for ch in range(ord('A'), ord('~')):
        m = hashlib.sha256()
        m.update(chr(ch).encode('utf-8'))
        if m.digest().hex() == line:
            flag += chr(ch)
            break
print(flag)
