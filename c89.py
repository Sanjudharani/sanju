import re
t = int(input())
for _ in range(t):
    uid = input().strip()
    if len(uid) != 10:
        print("Invalid")
        continue
    if not uid.isalnum():
        print("Invalid")
        continue
    if len(set(uid)) != 10:
        print("Invalid")
        continue
    if len(re.findall(r'[A-Z]', uid)) < 2:
        print("Invalid")
        continue
    if len(re.findall(r'[0-9]', uid)) < 3:
        print("Invalid")
        continue

    print("Valid")
