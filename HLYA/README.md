# How lucky you are

This challenge is really easy, the decompilation shows:
```c
random = generateRandomNumber();
printf("\nInsert your key: ");
scanf("%d",&key);
printf("\nYour key is %d\n",(ulong)key);
puts("\nLet\'s check your key...");
if (key == random) {
  puts("\nYes, you are lucky!! ");
  printf("%s\n", flag);
}
```

## Gathering
Looking at the `generateRandomNumber()` function, notice that it just calls `rand()` and returns its value.

`rand()` seed parameter is 1 by default, so our generated number will always be the same.

So we just need to emulate `generateRandomNumber()`: run `rand()` and print the value.

## Solving
[`Rand Generation`](https://github.com/utcq/olicybsec/blob/main/HLYA/howlucky.c)

We won't even need a python script; we can solve the challenge from our terminal:

```
Insert your key: 1804289383
Yes, you are lucky!!
flag{...}
```
