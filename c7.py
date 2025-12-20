# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# Number of test cases
T = int(input())

for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    
    # Start with a very large cube on top
    top = float('inf')
    possible = True
    
    while cubes:
        # Pick the larger of the two ends if <= top
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()
        
        # Check if it can be placed on top
        if cube <= top:
            top = cube
        else:
            possible = False
            break
    
    print("Yes" if possible else "No")
