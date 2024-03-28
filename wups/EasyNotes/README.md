# EasyNotes
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-225)

## Solution

The session cookie is jwt encoded: so we cannot edit it.

Looking at the network traffic we can clearly see an API request. The API is exposed and doesn't have any encryption.

`/api/note/{index}`

_(the flag is at index 1)_
