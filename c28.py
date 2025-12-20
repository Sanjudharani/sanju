# Read number of elements
n = int(input())

# Read the set elements and convert them to integers
s = set(map(int, input().split()))

# Read number of commands
N = int(input())

# Execute each command
for _ in range(N):
    command = input().split()  # split command into words

    if command[0] == "pop":
        s.pop()  # removes an arbitrary element
    elif command[0] == "remove":
        s.discard(int(command[1]))  # safe remove
    elif command[0] == "discard":
        s.discard(int(command[1]))  # safe discard

# Print sum of remaining elements
print(sum(s))
