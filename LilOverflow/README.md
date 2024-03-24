# Lil-Overflow

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-388)

In this challenge we have to overwrite `local_20 (uint32)` with a magic number.

## Small Intro

Stack frame structure:
```
- Return Address
- RBP
- Canary
- local_4c
- local_48
- local_28
- local_20
- local_10
- Buffer
```

## Gathering

`MAGIC` could be found through ghidra and is `0x5ab1bb0` (gabibbo)

`local_20` offset from RBP will be `[RBP - 8]`

## Assembling

`(b"\x00" * BUFF_SIZE)` 0x00 empty string to fill the buffer

`(b"\x00" * L20_OFFSET)` 8 bytes to fill `local_10` and point to `local_20`

`MAGIC` we just overwrite `local_20` with our magic number
