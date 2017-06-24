n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    result = 0
    x = list(map(int, str(arr[i])))
    for j in range(1, len(x) + 1):
        result = result + x[j - 1] * j
    print(result, end=' ')
