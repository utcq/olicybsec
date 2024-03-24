# Big Bird
This challenge aims at canary handling.

We need to call the `win()` function to expose the flag.

But the executable gives us the canary, so we don't even need to find any way to find it; we just read it and store it.

## Small Intro
In this challenge, our main function stack frame is structured like this:
```
- Return Address
- RBP
- Canary
- Buffer
```
So we need to reach the return address at an offset of `[RBP - 56]`.

## Gathering

> WIN = `gdb > p &win`

> RBP = `8 bytes`

## Assembling

`(b"\x00" * BUFF_SIZE)`  0x00 empty string to fill the buffer

`CANARY` The saved canary

`(b"\x00"*RBP_SKIP)` We just overwrite the RBP

`WIN` We write the win() address that will be called after `return`
