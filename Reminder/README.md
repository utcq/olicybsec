# Just a reminder

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-34)

## Solution

Through the debugger we find out about `default.js`

[Source](http://just-a-reminder.challs.olicyber.it/default.js)


The actual source is just junk, but this line is interesting:
```js
if (
    username_field.value === 'admin' &&
    AES_decrypt('U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl', s3cr37) ===
      password_field.value
  ) {
```

It checks if username is admin and password is the plaintext of `AES(key, cipher)` 

we can run `AES_decrypt('U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl', s3cr37)` in the console and get `v3ry_l337_p455w0rd_!`
