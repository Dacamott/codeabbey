for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area = abs(0.5 * (x1 * (y1 - y2) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    print(area, end=' ')
