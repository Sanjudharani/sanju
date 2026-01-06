import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
