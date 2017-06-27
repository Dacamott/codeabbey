def bubbleSort(myList, n):
    swap = True
    count = 0
    pass_count = 0
    while swap:
        swap = False
        for element in range(n - 1):
            if myList[element] > myList[element + 1]:
                swap = True
                temp = myList[element + 1]
                myList[element + 1] = myList[element]
                myList[element] = temp
                count += 1
        pass_count += 1
    print(pass_count, count, sep=' ')

n = int(input())
myList = list(map(int, input().split()))
bubbleSort(myList, n)
