import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
result = round(angle)

print(str(result) + chr(176))
