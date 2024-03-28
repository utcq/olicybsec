# keygenme
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-102)

## Solution
The pseudo-source shows:
```c
makeSerial(uid,serialkey);
```
`makeSerial` uses the `pairStrings` function, so we have to copy pairStrings and makeSerial into an empty C file.

Here's the new source:
```c
#include <stdio.h>
#include <stdlib.h>

void pairStrings(long param_1,long param_2,long param_3,int param_4) {
  uint local_14;
  int local_10;
  int local_c;
  
  local_14 = 0;
  local_10 = 0;
  local_c = 0;
  while ((local_10 < param_4 || (local_c < param_4))) {
    if ((local_14 & 1) == 0) {
      *(char *)((int)local_14 + param_1) = *(char *)(local_10 + param_2);
      local_14 = local_14 + 1;
      local_10 = local_10 + 1;
    }
    else {
      *(char *)((int)local_14 + param_1) = *(char *)(local_c + param_3);
      local_14 = local_14 + 1;
      local_c = local_c + 1;
    }
  }
  return;
}

void makeSerial(long param_1,long param_2) {
  pairStrings(param_2,param_1 + 0x12,param_1 + 9,8);
  pairStrings(param_2 + 0x10,param_1,param_1 + 0x12,8);
  pairStrings(param_2 + 0x20,param_1 + 9,param_1,8);
  *(char *)(param_2 + 0x30) = 0;
  return;
}


int main() {
    char uid[64];
    char serial[64];
    scanf("%s", uid);
    makeSerial(uid, serial);
    printf("%s\n", serial);
}
```

Now we can compile, run, connect to the server and give our solver the uid given by the server. 
