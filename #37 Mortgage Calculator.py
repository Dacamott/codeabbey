principal, rate, time = map(int, input().split())
rate = (rate / 100) / 12
print(round((principal * (rate * (1 + rate)**time)) / (((1 + rate)**time) - 1)))
