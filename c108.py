# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

def sort_key(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif int(c) % 2 == 1:
        return (2, c)
    else:
        return (3, c)

print("".join(sorted(s, key=sort_key)))
