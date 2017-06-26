for _ in range(int(input())):
    x, y, n = map(int, input().split())
    a = int((y * n) / (x + y))
    b = int((x * n) / (x + y))

    ans1 = int(max((a + 1) * x, b * y))
    ans2 = int(max(a * x, (b + 1) * y))
    print(min(ans1, ans2), end=' ')
