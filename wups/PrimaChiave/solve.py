e = 65537
n = 11599469215086283756239000323368207328888145111801687279952858519692571454576743213591474246385542521855249880051364427742007447330667804421622274846205769
r = open('dati.txt', "r").read().strip().splitlines()[2][5:-1].split(", ")
cipher = [int(i) for i in r]


mapping = {}
for m in range(256):
    c = pow(m, e, n)
    mapping[c] = m

plaintext = ""
for c in cipher:
    if c in mapping:
        plaintext += chr(mapping[c])
    else:
        plaintext += "?"

print("Decrypted plaintext:", plaintext)

