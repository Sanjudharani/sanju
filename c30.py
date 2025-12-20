# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read n (array size) and m (set sizes)
n, m = map(int, input().split())

# Read array
arr = list(map(int, input().split()))

# Read like set
A_like = set(map(int, input().split()))

# Read dislike set
B_dislike = set(map(int, input().split()))

happiness = 0

# Calculate happiness
for x in arr:
    if x in A_like:
        happiness += 1
    elif x in B_dislike:
        happiness -= 1

print(happiness)
