from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from math import isqrt

def GeneratePublicKey():
    while True:
        p = getPrime(512)
        q = p + 100
        if isPrime(q):
            return (p, q)

#p, q = GeneratePublicKey()
#n = p*q
e = 65537
#d = pow(e, -1, (p-1)*(q-1))

#print(n)
#print(e)
#print(ciphertext)

# OUTPUT    
n = 73835355773586632749497813712844974279688700968581353676365718256887741429589293987167857318819304298761226530765222129869744268663458302484923609419850715086294772630316875879671931990860760168632405376915473464245173555210859733420012801323450300287286827847372572895767079204521003431182215766356958645741
e = 65537
ciphertext = 69088718730225565550533207665423162086878540640610709978042785622785990794595484186604907117720523080139401746613418389574889276052615162202284720710353059616183359504400646419053826554396432853908827511966214885915759786569544232364425295062591653836236590708223539383404510598672913303248612361154693570128

# n = p * (p+100)
# x * (x+100) = n -> x^2 + 100x - n = 0
# delta = (100/2)^2 + n
# x = -(100/2) + sqrt(delta)
# x = -50 + sqrt(delta)

p = int(-50 + isqrt(2500 + n))
q = int(p + 100)

nn = p * q
assert n == nn

phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)

plaintext = pow(ciphertext, d, n)

plaintext_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')
try:
    plaintext_str = plaintext_bytes.decode('utf-8')
except UnicodeDecodeError:
    plaintext_str = plaintext_bytes.hex()

print(f"Decrypted: {plaintext_str}")

