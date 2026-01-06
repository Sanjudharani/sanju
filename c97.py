# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(float, input().split())))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
