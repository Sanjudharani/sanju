# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))   # main set A
n = int(input())                     # number of other sets

is_strict_superset = True

for _ in range(n):
    other = set(map(int, input().split()))
    
    # Check strict superset conditions:
    # 1. A must contain all elements of other (superset)
    # 2. A must have more elements than other (strict)
    if not (A > other):
        is_strict_superset = False
        break

print(is_strict_superset)
