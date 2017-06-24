for _ in range(int(input())):
    arr = list(map(int, input().split()))
    a = round((arr[1] - arr[3]) / (arr[0] - arr[2]))
    b = round(arr[1] - (a * arr[0]))
    string = "(" + str(a) + " " + str(b) + ")"
    print(string, end=' ')
