# The Wall

[> *Challenge (1000)*](https://training.olicyber.it/challenges#challenge-595)

This challenge is really simple.

The flag is being read and stored in a common buffer at the offset `0x14`.

This buffer is also used to store user input. So if the input length is less than `0x13` there will be a `\0` between input and flag making the flag unprintable by printf

## Gathering
This is the decompiled source:
```c
file = fopen("flag.txt", "r");
fread(buffer + 0x14, file);
fclose(file);
```

```c
printf("\nShare some thoughts: ");
sVar1 = read(0, buffer, 0x1000);
```

A buffer overflow isn't possible here

# Assembling
As you can imagine we just have to fill `0x13` bytes in the buffer so our flag will be finally printable

`( b"?" * (FLAG_OFFSET-1) )` A string of `?` as we cannot use `\x00`
