for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(round((arr[2] / 2) * ((2 * arr[0]) + ((arr[2] - 1) * arr[1]))),
          end=' ')
