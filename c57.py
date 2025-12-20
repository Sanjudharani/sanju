from itertools import permutations

if __name__ == '__main__':
    s, n = input().split()
    n = int(n)
    perm_list = sorted(permutations(s, n))
    for p in perm_list:
        print(''.join(p))
