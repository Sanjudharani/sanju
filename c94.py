# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

# Read the shape as a tuple of integers
shape = tuple(map(int, input().split()))

# Create arrays
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
