# Password changer 3000

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-59)

## Solution

When we try to change any username that isn't admin the page redirects us to `/change-password.php?token=dW5pdHk=`

`token` is just base64-encoded username.

so we encode admin to base64 and visit `/change-password.php?token=YWRtaW4=`

