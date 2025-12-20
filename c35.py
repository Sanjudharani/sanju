def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    n = len(string)
    stuart = 0
    kevin = 0

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


