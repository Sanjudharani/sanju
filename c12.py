# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

# Read group A words and store their positions (1-indexed)
for i in range(1, n + 1):
    d[input()].append(i)

# Read group B and print results
for _ in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)
