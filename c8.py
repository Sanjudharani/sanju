# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# Initialize an empty deque
d = deque()

# Read number of operations
n = int(input())

# Process each operation
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "append":
        d.append(int(cmd[1]))
    elif cmd[0] == "appendleft":
        d.appendleft(int(cmd[1]))
    elif cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()

# Print the elements space-separated
print(*d)
