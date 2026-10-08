import math

A, B = map(int, input().split())

floor = math.floor(A / B)
ceil = math.ceil(A / B)

if abs(floor - A / B) < abs(ceil - A / B):
    print(floor)
else:
    print(ceil)
