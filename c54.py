# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    # Read input
    s, k = input().split()
    k = int(k)
    
    # Sort the string to ensure lexicographic order
    s = sorted(s)
    
    # Generate all combinations with replacement of size k
    for comb in combinations_with_replacement(s, k):
        print(''.join(comb))
