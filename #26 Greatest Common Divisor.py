from fractions import gcd

for _ in range(int(input())):
    a, b = map(int, input().split())
    result = "(" + str(gcd(a, b)) + " " + str((a * b) // gcd(a, b)) + ")"
    print(result, end=' ')
