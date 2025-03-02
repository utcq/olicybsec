import datetime, hashlib, random

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


timestamp = "2021-03-21 17:37:40"
timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
ts = int(timestamp.timestamp())
h = hashlib.sha256(int_to_bytes(ts)).digest()

seed = int_from_bytes(h[32:])
key = h[:32]

random.seed(seed)
for _ in range(32):
    key += bytes([random.randint(0, 255)])

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

cipherb = open("flag.enc", "rb").read()
key = key * (len(cipherb) // len(key)) + key[:len(cipherb) % len(key)]
flag = xor(cipherb, key)

open("flag.pdf", "wb").write(flag)
from pypdf import PdfReader

reader = PdfReader("flag.pdf")
page = reader.pages[0]
pagestr = page.extract_text().splitlines()
flag = pagestr[0].replace("ﬂ", "fl").replace(" ", "_")
print(flag)

