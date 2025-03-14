import requests
import pytesseract
from PIL import Image

url = "http://captcha.challs.olicyber.it"

cookies = {}
r = requests.get(url)
cookies.update(r.cookies)

def read_captcha(html):
    if not '<img' in html:
        return None
    p_url = html.split('<img src="')[1].split('"')[0]
    r = requests.get(url + p_url, cookies=cookies)
    with open('captcha.png', 'wb') as f:
        f.write(r.content)
    img = Image.open('captcha.png')
    return pytesseract.image_to_string(img).strip()
for i in range(101):
    captcha = read_captcha(r.text)
    if not captcha:
        if i == 100:
            flag = r.text.split("<h1>")[1].split("</h1>")[0]
            print("Flag:", flag)
            exit()
        print("No captcha found")
        print(r.text)
        break
    print("[{}] Captcha:".format(i+1), captcha)
    r = requests.post(url + "/next", data={"risposta": captcha}, cookies=cookies)
    cookies.update(r.cookies)
