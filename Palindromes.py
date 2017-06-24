import re
for _ in range(int(input())):
    x = input()
    x = (re.sub("\W+", "", x)).lower()
    print("Y", end=' ') if x == x[::-1] else print("N", end=' ')
