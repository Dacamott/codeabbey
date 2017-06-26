def checkSum(arr):
    seed = 113
    limit = 10000007
    result = 0
    for i in range(len(arr)):
        result = (result + arr[i]) * seed
        if result > limit:
            result = result % limit
    return result


def bubbleSort(myList):
    count = 0
    for element in range(len(myList) - 1):
        if myList[element] > myList[element + 1]:
            temp = myList[element + 1]
            myList[element + 1] = myList[element]
            myList[element] = temp
            count += 1
    check_sum = checkSum(myList)
    print(count, check_sum, sep=' ')


arr = list(map(int, input().split()))
bubbleSort(arr[:-1])
