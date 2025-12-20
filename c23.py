# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of elements in set A
n = int(input())

# Read elements of set A and convert to integers
A = set(map(int, input().split()))

# Read number of other sets
N = int(input())

# Perform each mutation operation
for _ in range(N):
    # Read operation and size of the other set (size is not needed)
    operation_info = input().split()
    operation = operation_info[0]
    
    # Read the other set elements
    other_set = set(map(int, input().split()))
    
    # Perform the mutation operation
    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

# Print the sum of elements in set A after all operations
print(sum(A))
