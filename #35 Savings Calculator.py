for _ in range(int(input())):
    s, r, p = map(int, input().split())
    p = (p / 100.0) + 1
    y = 0
    while s < r:
        s *= p
        y += 1
    print(y, end=' ')
