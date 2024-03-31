# Form sicurissimo
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-126)

## Solution
I first looked up for `http` and found this:
```
Invece di questo form, puoi usare la porta 1234 per inviarci la prima flag tramite protocollo TCP e la valideremo.<br>
Per renderla irriconoscibile, manda l'i-esimo carattere della flag (partendo da 0) cifrato col Cifrario di Cesare, usando i come chiave (i simboli rimangono cos.. come sono).
```

So we can just look for anything on port 1234: `tcp.port == 1234`

We search for the latest request and we get the encoded flag, then we have to reformat it into a single line:
```
fmcj{yo_ackyzb_ihruvcvjam}
```

```py
def caesar(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            plaintext += shifted_char.upper() if char.isupper() else shifted_char
        else:
            plaintext += char
    return plaintext

def decode(enc):
    dec=''
    for i, char in enumerate(enc):
        dec += caesar(char, i)
    return dec

flag = decode(r"fmcj{yo_ackyzb_ihruvcvjam}")
print(flag)
```

And we get the flag
