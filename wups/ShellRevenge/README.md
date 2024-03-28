# Shells' Revenge

[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-52)

## Solution

_(flag in `/flag.txt`)_

We can upload any kind of file but we have a size limit (i think it's 100 bytes).

So we can upload any php file but has to be small.

```php
<?=@file_get_contents("/flag.txt");
```
