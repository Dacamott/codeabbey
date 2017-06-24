for _ in range(int(input())):
    string = input()
    vowels = 0
    for i in string.lower():
        if i in 'aeiouy':
            vowels = vowels + 1
    print(vowels, end=' ')
