import re

n = int(input())

pattern = r'(?<!^)(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))'

for _ in range(n):
    line = input()
    for match in re.findall(pattern, line):
        print(match)
