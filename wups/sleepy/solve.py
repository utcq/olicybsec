msg = "zZZzzZZz zZZzZZzz zZZzzzzZ zZZzzZZZ zZZZZzZZ zZzzZzzZ zzZzzzzz zZzzZZzz zZZzZZZZ zZZZzZZz zZZzzZzZ zzZzzzzz zZzzzzzZ zZzZzzZZ zZzzzzZZ zZzzZzzZ zZzzZzzZ zZZZZZzZ"

msg = msg.replace("z", "0").replace("Z", "1").replace(" ", "")
flag = ''.join([
    chr(int(msg[i:i+8], 2))
    for i in range(0, len(msg), 8)
])
print(flag)
