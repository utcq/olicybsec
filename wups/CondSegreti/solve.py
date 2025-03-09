import requests
from sympy.ntheory.modular import crt

url = 'http://condividendosegreti.challs.olicyber.it/'
primes = [690909282108739, 702862391767649, 739314349693453, 784627120326557, 851891142565129, 862496600114951]


def get_flag_shares() -> list:
    r = requests.post(url+"/execute", json={"fn": "get_flag_shares", "inputs": []})
    return r.json()['result']

def recover_secret(shares: list) -> bytes:
    inputs = [', '.join(str(x) for x in shares)]
    r = requests.post(url+"/execute", json={"fn": "recover_secret", "inputs": inputs})
    res = r.json()['result']
    return res.encode().decode('unicode_escape')

flag_shares = get_flag_shares()

r_val, N = crt(primes[:5], flag_shares)

candidate = None
for k in range(256):
    cand = r_val + k * N
    try:
        cand_bytes = cand.to_bytes(32, byteorder='big')
    except OverflowError:
        continue
    if cand_bytes.startswith(b'ITASEC{'):
        candidate = cand
        print("k =", k)
        break


final_share = candidate % primes[5]
flag = recover_secret(flag_shares + [final_share])
print("Flag:", flag)

