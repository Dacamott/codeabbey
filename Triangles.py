for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print("1" if (arr[0] + arr[1] > arr[2]) else "0", end=' ')
