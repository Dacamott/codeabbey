for _ in range(int(input())):
    problem = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    arr = list(map(str, input().split()))
    moves = 0
    flag = 1
    j = 0
    completed = False

    while completed is not True:
        moves += 1
        value = "X"
        if flag == 0:
            value = "O"
        problem = [[x.replace(arr[j], value) for x in lis] for lis in problem]
        flag = 1 if flag == 0 else 0
        j += 1

        if moves >= 3 and moves <= 9:
            if (problem[0][0] == problem[1][1] == problem[2][2] and problem[0][0] != "1"):
                completed = True

            elif (problem[0][2] == problem[1][1] == problem[2][0] and problem[0][2] != "3"):
                completed = True

            else:
                for i in range(3):
                    if all(problem[i][0] == problem[i][j] for j in range(1, 3)):
                        completed = True
                        break

                    elif all(problem[0][i] == problem[j][i] for j in range(1, 3)):
                        completed = True
                        break

    print(moves, end=' ') if completed is True else print("0", end=' ')