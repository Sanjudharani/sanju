# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n, m = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.max(numpy.min(A, axis=1)))
