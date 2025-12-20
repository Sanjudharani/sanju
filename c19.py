# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

z = complex(input().strip())   # read complex number as Python complex
r = abs(z)                     # modulus
phi = cmath.phase(z)           # phase angle

print(r)
print(phi)
