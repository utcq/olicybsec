import requests, os
import random, string, base64

url = "https://imager-xor.challs.olicyber.it"
ocr_space = "https://api.ocr.space/parse/image"

def random_filename() -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))

def flag_image() -> str:
    path = random_filename() + ".png"
    r = requests.get(url+"/get_flag")
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def encrypt_image(src: str) -> str:
    path = random_filename() + ".png"
    files = {
        "image": (src, open(src, "rb"), "image/png"),
    }
    r = requests.post(url+"/encrypt_image", files=files)
    if r.status_code != 200:
        raise Exception("Error while encrypting image " + r.text)
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def xor_images(path1: str, path2: str) -> str:
    path = random_filename() + ".png"
    files = {
        "first_image": (path1, open(path1, "rb"), "image/png"),
        "second_image": (path2, open(path2, "rb"), "image/png"),
    }
    r = requests.post(url+"/images_xor", files=files)
    if r.status_code != 200:
        raise Exception("Error while XORing images " + r.text)
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def generate_known() -> str:
    path = random_filename() + ".png"
    open(path, "wb").write(os.urandom(1000000)) # 1MB
    return path

def ocr_image(path: str) -> str:
    files = {
        "file": (path, open(path, "rb"), "image/png"),
    }
    r = requests.post(ocr_space, files=files, data={"apikey": "helloworld"})
    if r.status_code != 200:
        raise Exception("Error while OCRing image " + r.text)
    try:
        return r.json()["ParsedResults"][0]["ParsedText"].replace('\r', '').replace('\n', '').strip().replace("s1s", "s_1s")
    except:
        return ""

def cleanup(files: list):
    for f in files:
        os.remove(f)

flag = flag_image()
known = generate_known()
known_e = encrypt_image(known)
key = xor_images(known, known_e)
flag_plain = xor_images(flag, key)
flag_text = ocr_image(flag_plain)
cleanup([flag, known, known_e, key, flag_plain])
print("Flag:", flag_text)
