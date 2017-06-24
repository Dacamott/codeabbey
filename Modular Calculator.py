def cal(num):
    n = input()
    while n[:1] != "%":

        if n[:1] == "+":
            num += int(n[2:].strip())

        elif n[:1] == "*":
            num *= int(n[2:].strip())

        n = input()
    num %= int(n[2:].strip())
    print(num)
cal(int(input()))
