import numpy as np

# Read N, M, P
N, M, P = map(int, input().split())

# Read first array
array1 = np.array([list(map(int, input().split())) for _ in range(N)])

# Read second array
array2 = np.array([list(map(int, input().split())) for _ in range(M)])

# Concatenate along axis 0
result = np.concatenate((array1, array2), axis=0)

print(result)
