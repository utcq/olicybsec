# super_market
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-99)

## Solution

Our balance is 10$ but the flag costs 1mln $

By looking at the source we can notice this line:
```c
cost = ps[choice-1].price * amount;
```

It won't let us insert 0 but we can still insert a negative number that will make the cost lower than the balance.

So we just need to use -1 as amount to get the flag for free
