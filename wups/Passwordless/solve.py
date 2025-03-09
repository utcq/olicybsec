import requests, json

url = 'http://passwordlesslogin.challs.olicyber.it/'

def register(username):
    r = requests.post(url+"/execute", json={"fn": "register", "inputs": [username]})
    return r.json()['result']

def login(token):
    r = requests.post(url+"/execute", json={"fn": "login", "inputs": [token]})
    return r.json()['result']

admin = "Amministratore"
dummy_username = admin[:-1] + "o"
dummy = register(dummy_username)
plain = json.dumps({"username": dummy_username}).encode()
dummy_blocks = [dummy[i:i+32] for i in range(0, len(dummy), 32)]
plain_blocks = [plain[i:i+16] for i in range(0, len(plain), 16)]
dummy_username2 = "X"+admin[1:]
dummy2 = register(dummy_username2)
plain2 = json.dumps({"username": dummy_username2}).encode()
dummy_blocks2 = [dummy2[i:i+32] for i in range(0, len(dummy2), 32)]
plain_blocks2 = [plain2[i:i+16] for i in range(0, len(plain2), 16)]
final_blocks = [dummy_blocks[0], dummy_blocks2[1]] + dummy_blocks[2:]
print(dummy_blocks)
print(dummy_blocks2)
print(plain_blocks)
print(plain_blocks2)
print(final_blocks)
token = ''.join(final_blocks)
flag = login(token).split(' ')[-1][:-1]
print("Flag:", flag)

