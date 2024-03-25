# Rick Roller

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-42)

## Solution

The button redirects us to `http://roller.challs.olicyber.it/get_flag.php` that redirects to youtube.

We cannot find the `get_flag.php` content from the browser bc of the redirection.

```py
import requests
r = requests.get("http://roller.challs.olicyber.it/get_flag.php", allow_redirects=False)
print(r.text)
```

easy flag
