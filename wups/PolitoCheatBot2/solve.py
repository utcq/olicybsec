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

pad_byte = 0
psw_bytes = bytes.fromhex(password)
for _ in range(len(psw_bytes)//4):
    pad_test_cipher = bytes.fromhex(encrypt(password))
    pad_byte_n = pad_test_cipher[0] ^ bytes.fromhex(password)[0]
    if pad_byte != 0:
        assert pad_byte_n == pad_byte + 1
    if pad_byte != 0:
        prevision = xor(psw_bytes, bytes([pad_byte+1]*len(psw_bytes)))
        assert pad_test_cipher == prevision
    pad_byte = pad_byte_n
    print("[{}] Pad byte:".format(_+1), hex(pad_byte)[2:], " -> Prevision correct")


pad_bytes = bytes([0x7a]*len(psw_bytes))
prevision = xor(psw_bytes, pad_bytes)
print("Pad bytes:", pad_bytes.hex())
print("Password cipher:", prevision.hex())
assert xor(prevision, pad_bytes) == psw_bytes
msg_r = requests.post(api_url + "message", cookies={"session": session}, json={"message": prevision.hex()}).json()
print(msg_r)
