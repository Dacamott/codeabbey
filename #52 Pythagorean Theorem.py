import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    result = "A"
    if math.sqrt(a**2 + b**2) == c:
        result = "R"
    elif math.sqrt(a**2 + b**2) < c:
        result = "O"
    print(result, end=' ')
