import numpy as np
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
sum_axis0 = np.sum(arr, axis=0)
result = np.prod(sum_axis0)
print(result)
