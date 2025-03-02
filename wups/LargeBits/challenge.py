#!/bin/env python3

from Crypto.Util.number import bytes_to_long, isPrime

import random
from secret import FLAG

def gen_prime(nbits):
    while True:
        p = 2**(nbits+1) - 1
        for i in range(30):
            x = random.randint(2, nbits-1)
            p -= 2**x
        if isPrime(p):
            return p


def keygen(nbits):
    p = gen_prime(nbits//2)
    q = gen_prime(nbits//2)
    n = p*q
    return n


n = keygen(2048)
e = 65537
msg = bytes_to_long(FLAG)
ct = pow(msg, e, n)
print(f"n = {n}")
print(f"ct = {ct}")
