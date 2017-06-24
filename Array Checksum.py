n = int(input())
arr = list(map(int, input().split()))
seed = 113
limit = 10000007
result = 0
for i in range(n):
    result = (result + arr[i]) * seed
    if result > limit:
        result = result % limit
print(result)
