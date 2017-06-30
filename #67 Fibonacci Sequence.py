# Solution 1 - using Math's formula

import math


def Fibonacci(n):
    print(round(math.log(n * math.sqrt(5) + 0.5) / math.log(1.61803398875)), end=' ')


for _ in range(int(input())):
    x = float(input())
    count = 0
    Fibonacci(x)


# Solution 2

for _ in range(int(input())):
    x = int(input())
    a, b, c, count = 0, 1, 0, 0

    while c <= x and x != 0:
        c = a + b
        a = b
        b = c
        count += 1
    print(count, end=' ')
