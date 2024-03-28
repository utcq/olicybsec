# NaaS
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-224)

## Solution
I found out there's an API for debugging purposes.

So we can filter by `http.request.uri contains "/api/"`

The API has two main features:
- users
- notes

The `/api/debug/users` path returns a JSON object with all the users' data. Here we can find the admin account, with the id `1`.

Now we can just use `/api/debug/notes/{id}` to read admin's notes and find the flag
