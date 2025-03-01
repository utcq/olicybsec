#!/usr/bin/env python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def generateKey():
start = random.randint(1,25)
    key = "".join([alphabet[start:], alphabet[0:start]])
    return key

def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]
 
        if ord(character) <= 90 and ord(character) >= 65: #lowercase
            i = alphabet.index(chr(ord(character)+32))
            characterEncrypted = chr(ord(key[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
            i = alphabet.index(character)
            characterEncrypted = key[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        else:
            ciphertext = "".join([ciphertext,character])
        
    return ciphertext


def handle():
    plaintextFLAG = "...{...}"
    key = generateKey()
    ciphertext = encrypt(plaintextFLAG, key)
    print(ciphertext)
    
    return



if __name__ == "__main__":
    handle()
