# Enter your code here. Read input from STDIN. Print output to STDOUT
def design_door_mat(n, m):
    

    # Top half of the mat
    for i in range(n // 2):
        pattern = ".|." * (2 * i + 1)
        padding = "-" * ((m - len(pattern)) // 2)
        print(padding + pattern + padding)

    # Middle row with "WELCOME"
    welcome_padding = "-" * ((m - 7) // 2)
    print(welcome_padding + "WELCOME" + welcome_padding)

    # Bottom half of the mat
    for i in range(n // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        padding = "-" * ((m - len(pattern)) // 2)
        print(padding + pattern + padding)


if __name__ == "__main__":
    n, m = map(int, input().split())
    design_door_mat(n, m)
