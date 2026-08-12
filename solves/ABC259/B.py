import math

a, b, d = map(int, input().split())

r = math.sqrt(a**2 + b**2)
theta = math.atan2(b, a)
theta += math.radians(d)
print(r * math.cos(theta), r * math.sin(theta))
