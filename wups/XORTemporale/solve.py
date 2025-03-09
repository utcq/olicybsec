import datetime, random, requests

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def temporal_xor(hex_string: str):
  message = bytes.fromhex(hex_string)
  random.seed(datetime.datetime.now().minute)
  return bytes([message[i] ^ random.randint(1,255) for i in range(len(message))])

def get_temporal():
    r = requests.post("http://xortemporale.challs.olicyber.it/execute", json={"fn": "get_encrypted_flag", "inputs": []})
    return r.json()["result"]

print(temporal_xor(get_temporal()).decode())
