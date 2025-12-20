# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())   # number of test cases

for _ in range(t):
    a = int(input())               # number of elements in set A
    A = set(map(int, input().split()))
    b = int(input())               # number of elements in set B
    B = set(map(int, input().split()))
    
    # Check subset condition
    print(A.issubset(B))
