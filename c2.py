import re
for _ in range(int(input())) : 
    val = True
    try :
        re.compile(input())
    except : 
        val = False
    print(val)