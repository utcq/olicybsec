# C style login

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-57)

## Solution

The login is using this if for the password:
```php
if (strcmp($_POST['password'], $password) == 0) {}
```

Remember that `false == 0`

strcmp expects 2 string, but if we give an array as the first argument strcmp will crash and return false making our statement true

so we just resend the request with a payload like this:
```php
password[]=anything
```
