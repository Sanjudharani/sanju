# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

print(np.polyval(coefficients, x))
