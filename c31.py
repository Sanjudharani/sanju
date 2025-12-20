# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of elements in set A
m = int(input())
# Read elements of set A
a = set(map(int, input().split()))

# Read number of elements in set B
n = int(input())
# Read elements of set B
b = set(map(int, input().split()))

# Symmetric difference
result = sorted(a.symmetric_difference(b))

# Print one value per line
for val in result:
    print(val)
