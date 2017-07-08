for _ in range(int(input())):
    match = input().split()
    p1_count, p2_count = 0, 0
    result = "2"
    for m in match:
        if any(m == x for x in ["RR", "SS", "PP"]):
            0
        elif any(m == x for x in ["RS", "PR", "SP"]):
            p1_count += 1
        else:
            p2_count += 1

    if p1_count > p2_count:
        result = "1"

    print(result, end=' ')
