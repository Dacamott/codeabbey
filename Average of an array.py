from decimal import Decimal, ROUND_HALF_UP
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(Decimal(sum(arr) / (len(arr) - 1)).quantize(Decimal("1"),
                                                      rounding=ROUND_HALF_UP), end=' ')
