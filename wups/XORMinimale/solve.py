import requests

def minimal_xor(hex_string, char):
    message = bytes.fromhex(hex_string)
    return (bytes([message[i] ^ ((ord(char)+i) % 256) for i in range(len(message))]))

url = 'http://xorminimale.challs.olicyber.it/'

def get_encrypted_flag() -> list:
    r = requests.post(url+"/execute", json={"fn": "get_encrypted_flag", "inputs": []})
    return r.json()['result']

flag = get_encrypted_flag()

for c in range(256):
    candidate = minimal_xor(flag, chr(c))
    if candidate.startswith(b'ITASEC{'):
        print("Flag:", candidate.decode())
        break
