# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read K
K = int(input())

# Read the room number list
rooms = list(map(int, input().split()))

# Convert to sets
unique_rooms = set(rooms)

# Using formula: Captain = (sum(unique_rooms) * K - sum(rooms)) // (K - 1)
captain = (sum(unique_rooms) * K - sum(rooms)) // (K - 1)

print(captain)
