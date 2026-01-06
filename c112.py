import re

n = int(input())

for _ in range(n):
    card = input().strip()
    
    pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    if not re.match(pattern, card):
        print("Invalid")
        continue

    digits = card.replace("-", "")

    if re.search(r'(\d)\1{3,}', digits):
        print("Invalid")
    else:
        print("Valid")
