import numpy as np
n,m = map(int,input().split())

data = [input().split() for _ in range(n)]

np_array = np.array(data,int)

print(np.transpose(np_array))
print(np_array.flatten())
