import requests

api_url = "http://politocheatbot.challs.olicyber.it/api/v1/"

token = requests.get(api_url + "init").json()["messages"][-1]["text"].split('Send me your token "')[1].split('"')[0]

def encrypt(text: str) -> str:
    return requests.post(api_url + "encrypt", json={"plaintext": text}).json()["ciphertext"]

def token_encrypt(token: str) -> str:
    target_size = 64
    chunks = [token[i:i+16] for i in range(0, len(token), 16)]
    pad_distribution = 64 // (len(chunks)*16)
    for i, chunk in enumerate(chunks):
        chunks[i] = chunk + "B"*pad_distribution
    return "".join([encrypt(chunk) for chunk in chunks])

enc_token = token_encrypt(token)
flag = requests.post(api_url + "message", json={"message": enc_token}).json()["message"]
print(flag)
