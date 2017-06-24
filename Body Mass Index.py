import math
for _ in range(int(input())):
    weight, height = map(float, input().split(" "))
    bmi = weight / math.pow(height, 2)
    result = "under"
    if bmi >= 18.5:
        if bmi < 25:
            result = "normal"
        elif bmi < 30:
            result = "over"
        else:
            result = "obese"
    print(result, end=' ')
