import math

A, B = map(int, input().split())

if A != 0:
    theta = math.atan(B / A)
    print(math.cos(theta), math.sin(theta))
else:
    print(0, 1)
