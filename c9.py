# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    word = input().strip()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# Number of distinct words
print(len(words))

# Occurrences of each word in order of first appearance
print(*words.values())
