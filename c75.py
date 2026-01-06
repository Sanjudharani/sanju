import re

s = input().strip()

pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

matches = re.findall(pattern, s)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)