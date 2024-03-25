# Make a wish

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-47)

## Solution

As you may know php is very weak on datatypes.

PHP `preg_match()` expects a string as input but if we give it an array it will crash and return False.

```php
if(isset($_GET['richiesta'])) {
  if (preg_match("/.*/i", $_GET['richiesta'], $match))  {
    echo "No, mi dispiace non posso fare questo!";
  } else {
    echo "flag{TROVAMI}";
  }
} else {
  echo "Fai una richiesta e provero a realizzarla";
}
```

So we just resend the request but we use this url parameter: `/?richiesta[]=anything`
