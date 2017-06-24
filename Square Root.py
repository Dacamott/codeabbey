for _ in range(int(input())):
    x, n = map(int, input().split())
    r = 1.00
    if n >= 1:
        for i in range(n):
            d = x / r
            abs(r - d)
            r = (r + d) / 2
        print(r, end=' ')
    else:
        print("1", end=' ')
