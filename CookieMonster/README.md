# Cookie Monster Army

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-51)

## Solution

We register and login.
By looking at the cookies we find `session` that decoded from base64 shows `2024/03/25-1711402114-unity1234`
we turn it to `2024/03/25-0-admin`, encode and replace (remember to add `%3D%3D`)
