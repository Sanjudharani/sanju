# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read k and M
k, M = map(int, input().split())

# Read all k lists
lists = []
for _ in range(k):
    arr = list(map(int, input().split()))
    lists.append(arr[1:])  # Skip the first number (length of list)

# Initialize max value
max_value = 0

# Iterate over all combinations
for combo in product(*lists):
    s = sum(x**2 for x in combo) % M
    if s > max_value:
        max_value = s

print(max_value)