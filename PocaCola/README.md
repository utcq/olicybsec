# Poca Cola's Recipe

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-25)

## Solution

We filter by `http && http.request.method == POST && frame contains "ricetta"`

then we just save the file as `recipe.txt.zip` (i usually turn the hex stream into an image and save it as a zip with [tool](https://codepen.io/abdhass/pen/jdRNdj))

The zip is password-protected. So we filter by `frame contains "password"` and retrieve the password: `qhcdpoktbjdsujbsrpjwr`

We unzip and get the flag
