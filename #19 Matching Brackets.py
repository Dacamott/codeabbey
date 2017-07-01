for _ in range(int(input())):
    data = input()
    check_data = ''.join([char for char in data if char in ('(){}[]<>')])

    length = len(check_data) + 1

    while len(check_data) < length:
        length = len(check_data)
        check_data = check_data.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')

    print("0", end=' ') if len(check_data) > 0 else print("1", end=' ')
