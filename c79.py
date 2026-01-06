# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())
for _ in range(n):
    line = input()
    parsed_address = email.utils.parseaddr(line)
    name, address = parsed_address
    pattern = r'^[a-zA-Z][\w\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    if re.match(pattern, address):
        print(email.utils.formataddr((name, address)))
