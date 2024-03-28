# TIMP

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-50)

## Solution

Our flag is in `/flag.txt`. But `cat` will just show a cat.

So we have to cowsay the read file (i didn't even read the source):
```bash
cowsway "$(cat /flag.txt)"
```
