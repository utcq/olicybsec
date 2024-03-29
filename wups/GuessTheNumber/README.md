# GuessTheNumber
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-93)

## Gathering
We have a global variable in `.data` called `gamedata`. It contains the player's name + the random number.

It's a 32 bytes array but only 28 are used. 
```php
 0...19 = NAME
20...27 = NUMBER
```

The buffer is written from 0 to 27. So we can overflow the name bytes and overwrite the random number.

We can repeat a letter 32 times and then retrieve the number to guess:
```php
GUESS = int.from_bytes( (LETTER * 8).encode() byteorder='big')

# We can just find the letter ascii position and turn it to HEX.
# Then we can repeat this hex for 8 times and decode this long long from hex to dec
```
