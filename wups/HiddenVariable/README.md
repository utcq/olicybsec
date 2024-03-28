# Hidden Variable
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-96)

## Solution

Our flag is the label `fl4g` in `.data`

So we can just run:
```bash
objdump -d hidden_variable -j .data
```

to show the .data section and get the flag (you have to write it char by char)
