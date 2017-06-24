m, n = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    print(arr.count(i + 1), end=' ')
