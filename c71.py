import re

# Read rows and columns
n, m = map(int, input().split())

# Read the matrix
matrix = [input() for _ in range(n)]

# Read column by column
decoded = ''.join(''.join(matrix[i][j] for i in range(n)) for j in range(m))

# Replace non-alphanumeric characters between alphanumerics with a single space
decoded = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', decoded)

print(decoded)
