import requests

root_url = "http://politocheatbot2.challs.olicyber.it/"
api_url = "	http://politocheatbot2.challs.olicyber.it/api/v1/"

root_r = requests.get(root_url)
session = root_r.headers["Set-Cookie"].split("=")[1].split(";")[0]

init_r = requests.get(api_url + "init")
password = init_r.json()["messages"][1]["text"].split(": ")[1]

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def encrypt(plain: str):
    return requests.post(
        api_url + "encrypt",
        cookies={"session": session},
        json={"plaintext": plain}
    ).json()["ciphertext"]

print("Session:", session)
print("Password:", password)

rounds = [-1]
latest_round = 0
i=0
while latest_round != rounds[0]:
    rd = encrypt(password)
    xor_key = xor(bytes.fromhex(rd), bytes.fromhex(password))
    rd = bytes.fromhex(rd)
    if i != 0:
        rounds.append(rd)
        latest_round = rd
    else:
        rounds[i] = rd
    i+=1
del rounds[-1]

psw_bytes = bytes.fromhex(password)
for pad in rounds:
    cipher = xor(psw_bytes, pad)

    r_msg = requests.post(api_url + "message", cookies={"session": session}, json={"message": cipher.hex()})
    print(r_msg.json())
