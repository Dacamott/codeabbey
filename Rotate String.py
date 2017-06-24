for _ in range(int(input())):
    k, s = input().split()
    k = int(k)
    str1, str2 = s[0:k], s[k:]
    print(str2 + str1, end=' ')
