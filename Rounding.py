n = int(input())
result = []

for i in range(n):
    arr = list(map(int, input().split()))
    result.append(round(arr[0] / arr[1]))

print(" ".join(str(x) for x in result))
