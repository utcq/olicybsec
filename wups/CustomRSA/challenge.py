from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

p,q = getPrime(1024), getPrime(1024)
n = p*q
e = n-p-q+4

ct = pow(bytes_to_long(flag), e, n)

print("n =", n)
print("ct =", ct)
