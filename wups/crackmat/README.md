# crackmat
[> *Challenge (500)*](https://training.olicyber.it/challenges#challenge-364)

## Gathering
The flag checker is:
```c
param_1[0x13] * -0xfa + (int)param_1[0x13] * (int)param_1[0x13] == -0x3d09 &&
(param_1[0x12] * -0x60 + (int)param_1[0x12] * (int)param_1[0x12] == -0x900 &&
(param_1[0x11] * -0xbe + (int)param_1[0x11] * (int)param_1[0x11] == -0x2341 &&
(param_1[0x10] * -0xca + (int)param_1[0x10] * (int)param_1[0x10] == -0x27d9 &&
(param_1[0xf] * -0xe8 + (int)param_1[0xf] * (int)param_1[0xf] == -0x3490 &&
(param_1[0xe] * -0xdc + (int)param_1[0xe] * (int)param_1[0xe] == -0x2f44 &&
(param_1[0xd] * -0xc2 + (int)param_1[0xd] * (int)param_1[0xd] == -0x24c1 &&
(param_1[0xc] * -0xdc + (int)param_1[0xc] * (int)param_1[0xc] == -0x2f44 &&
(param_1[0xb] * -0xd2 + (int)param_1[0xb] * (int)param_1[0xb] == -0x2b11 &&
(param_1[10] * -0xda + (int)param_1[10] * (int)param_1[10] == -0x2e69 &&
(param_1[9] * -0xe4 + (int)param_1[9] * (int)param_1[9] == -0x32c4 &&
(param_1[8] * -0xca + (int)param_1[8] * (int)param_1[8] == -0x27d9 &&
(param_1[7] * -0xe8 + (int)param_1[7] * (int)param_1[7] == -0x3490 &&
(param_1[6] * -0x66 + (int)param_1[6] * (int)param_1[6] == -0xa29 &&
(param_1[5] * -200 + (int)param_1[5] * (int)param_1[5] == -10000 &&
(param_1[4] * -0xf6 + (int)param_1[4] * (int)param_1[4] == -0x3b19 &&
(param_1[3] * -0xce + (int)param_1[3] * (int)param_1[3] == -0x2971 &&
(param_1[2] * -0xc2 + (int)param_1[2] * (int)param_1[2] == -0x24c1 &&
(param_1[1] * -0xd8 + (int)param_1[1] * (int)param_1[1] == -0x2d90 &&
*param_1 * -0xcc + (int)*param_1 * (int)*param_1 == -0x28a4
```

You can notice that these are just 2nd grade equations.

We can parse them and use sympy to solve them.
