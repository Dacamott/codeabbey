for _ in range(int(input())):
    d, s1, s2 = map(int, input().split())
    time = d / (s1 + s2)
    print((time * s1), end=' ')
