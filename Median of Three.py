for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(arr[1], end=' ')