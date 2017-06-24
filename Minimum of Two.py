n = int(input())
result = []
for i in range(n):
    arr = (map(int, input().split()))
    result.append(min(arr))
print(" ".join(str(x) for x in result))
