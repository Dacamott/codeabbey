arr = list(map(int, input().split()))
result = []

for i in range(1, len(arr)):
    result.append(round(5 * (arr[i] - 32) / 9))

print(" ".join(str(x) for x in result))
