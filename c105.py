# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

indices = list(range(n))

total = 0
count = 0

for comb in combinations(indices, k):
    total += 1
    if any(letters[i] == 'a' for i in comb):
        count += 1

print(round(count / total, 4))