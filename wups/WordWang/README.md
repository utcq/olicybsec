# Word Wang

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-27)

## Solution

We filter by `x11 && tcp.stream eq 0 && frame.len == 131` (this is very specific just bc there are other x11 packets) 

We follow the stream and find out that WordWang works like this `?WORD!`
