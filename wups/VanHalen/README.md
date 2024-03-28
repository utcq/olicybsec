# van_halen
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-100)

## Solution
No protection enabled, we can jump to our flag-printing function.

We launch gdb and run:
```bash
gef➤  info functions
All defined functions:

Non-debugging symbols:
0x0000000000001149  funzione_totalmente_anonima_non_mi_lanciare
0x000000000000119d  main

gef➤  break main
Breakpoint 1 at 0x11a5
gef➤  run
...
gef➤  jump funzione_totalmente_anonima_non_mi_lanciare
```
