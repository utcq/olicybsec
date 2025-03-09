import requests

url = "http://lemosse.challs.olicyber.it"
cookies = {}
r = requests.get(url+"/step1")
cookies.update(r.cookies)
r = requests.post(url+"/step2", cookies=cookies, data={"hello": "world", "dead": "beef"})
cookies.update(r.cookies)
r = requests.put(url+"/step3", cookies=cookies)
cookies.update(r.cookies)
r = requests.delete(url+"/step4", cookies=cookies)
flag= r.text.split(" ")[-1]
print(flag)
