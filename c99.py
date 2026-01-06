import numpy

N, M = map(int, input().split())
arr = numpy.array([input().split() for _ in range(N)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))
