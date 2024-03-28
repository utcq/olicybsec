# NFT gallery
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-226)


## Solution
We cannot directly use path traversal (there's a check) but PHP is weak and the source code uses `==` instead of `===` so we can use an array as url parameter and bypass that check.

`/nft?id[]=../flag.txt`

Then open the dev tools, copy the b64 image source, decode and get the flag
