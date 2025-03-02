import os

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

SBOX = [241, 48, 42, 240, 190, 182, 141, 119, 143, 53, 175, 83, 152, 184, 130, 64,
        107, 87, 51, 163, 127, 1, 21, 52, 252, 80, 134, 20, 46, 129, 189, 106,
        197, 235, 35, 43, 136, 174, 139, 137, 100, 215, 250, 14, 101, 103, 156,
        178, 244, 32, 153, 39, 202, 76, 4, 2, 128, 231, 98, 123, 56, 91, 96,
        135, 97, 50, 74, 209, 65, 236, 94, 90, 221, 150, 180, 218, 93, 160, 120,
        203, 237, 6, 26, 164, 192, 246, 195, 114, 233, 58, 15, 185, 84, 49, 63,
        205, 172, 54, 162, 208, 170, 212, 131, 125, 206, 62, 82, 210, 67, 194,
        115, 68, 69, 138, 186, 183, 31, 8, 154, 126, 37, 33, 133, 177, 146, 242,
        223, 157, 148, 3, 116, 140, 168, 232, 57, 81, 18, 238, 45, 73, 13, 11,
        105, 222, 77, 217, 188, 16, 24, 200, 17, 30, 7, 220, 40, 155, 211, 60,
        142, 124, 88, 117, 113, 102, 27, 110, 216, 61, 247, 225, 165, 169, 227,
        201, 179, 214, 86, 75, 254, 243, 167, 70, 132, 159, 158, 9, 59, 144, 198,
        79, 112, 89, 19, 204, 181, 108, 22, 191, 111, 41, 166, 10, 44, 55, 147,
        71, 72, 104, 5, 171, 187, 78, 47, 255, 199, 149, 28, 25, 34, 249, 118,
        251, 92, 239, 228, 36, 230, 151, 161, 173, 196, 248, 219, 109, 229, 193,
        245, 29, 145, 213, 95, 23, 226, 0, 121, 38, 12, 253, 99, 207, 122, 234,
        224, 176, 66, 85]

SWAPS = [(25, 62), (23, 8), (6, 16), (2, 38), (21, 37), (47, 5), (8, 18),
         (13, 43), (28, 17), (27, 43), (17, 56), (16, 59), (28, 44), (34, 0),
         (12, 45), (42, 27), (43, 15), (15, 25), (15, 14), (47, 16), (43, 58),
         (56, 43), (56, 14), (49, 2), (7, 12), (38, 11), (10, 5), (44, 37),
         (24, 28), (51, 37), (48, 61), (63, 26), (59, 48), (8, 11), (32, 30),
         (39, 60), (54, 19), (18, 42), (9, 23), (0, 48), (24, 41), (38, 49),
         (28, 39), (11, 10), (58, 42), (10, 22), (2, 31), (40, 39), (8, 13),
         (52, 61), (10, 19), (36, 4), (39, 10), (23, 33), (56, 55), (24, 60),
         (3, 38), (42, 40), (45, 7), (12, 41), (63, 61), (51, 7), (1, 42),
         (24, 45), (38, 36), (34, 16), (48, 5), (61, 54), (43, 10), (4, 30),
         (53, 45), (63, 21), (30, 7), (27, 48), (14, 55), (22, 26), (8, 16),
         (60, 18), (27, 32), (21, 48), (38, 28), (33, 38), (46, 18), (21, 13),
         (63, 39), (15, 29), (41, 20), (56, 62), (53, 38), (15, 35), (24, 51),
         (26, 34), (18, 59), (50, 25), (11, 59), (0, 58), (52, 17), (48, 60),
         (7, 35), (24, 21), (20, 41), (3, 9), (8, 55), (17, 38), (49, 46),
         (31, 10), (4, 48), (52, 46), (40, 8), (46, 38), (38, 19), (7, 16),
         (57, 42), (53, 47), (9, 53), (12, 31), (24, 30), (43, 53), (29, 7),
         (51, 18), (38, 34), (9, 40), (63, 59), (62, 32), (58, 54), (0, 58),
         (59, 4), (14, 8)]

INV_SBOX = [0] * 256
for i, s in enumerate(SBOX):
    INV_SBOX[s] = i

def round_decrypt(state, r):
    round_key = bytes([r % 256]) * 64
    state = xor(state, round_key)
    state = list(state)
    for x, y in reversed(SWAPS):
        state[x], state[y] = state[y], state[x]
    state = [INV_SBOX[x] for x in state]
    state = xor(bytes(state), round_key)
    return state

def decrypt(ct_hex, rounds=1337):
    ct = bytes.fromhex(ct_hex)
    blocks = [ct[i:i+64] for i in range(0, len(ct), 64)]
    decrypted = []
    for i, block in enumerate(blocks):
        state = block
        for r in reversed(range(rounds)):
            state = round_decrypt(state, r)
        start = bytes([(128 - i) % 256]) * 64
        pt_block = xor(state, start)
        decrypted.append(pt_block)
    return b"".join(decrypted)

ct_hex = open("flag.enc", "r").read().strip()
decrypted = decrypt(ct_hex)
flag = ""
for ch in decrypted:
    try:
        flag += bytes([ch]).decode("ascii")
    except UnicodeDecodeError:
        break
print("Flag:", flag)
