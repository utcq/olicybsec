#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

cipher = 'xcqv{gvyavn_zvztv_etvtddlnxcgy}'

# key = split alphabet

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

def decrypt(cipher, key):
    plaintext = ""
    for k in range(len(cipher)):
        character = cipher[k]

        if ord(character) <= 90 and ord(character) >= 65: #lowercase
            i = key.index(chr(ord(character)+32))
            characterDecrypted = chr(ord(alphabet[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            plaintext = "".join([plaintext,characterDecrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
            i = key.index(character)
            characterDecrypted = alphabet[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            plaintext = "".join([plaintext,characterDecrypted])
        else:
            plaintext = "".join([plaintext,character])
        
    return plaintext


for i in range(1, 26):
    key = "".join([alphabet[i:], alphabet[0:i]])
    e = encrypt('flag{', key)
    if e == cipher[:5]:
        plaintext = decrypt(cipher, key)
        print(plaintext)
        break
