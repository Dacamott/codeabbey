result = []
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(sum(list(map(int, str((arr[0] * arr[1]) + arr[2])))), end=' ')
