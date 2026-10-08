a, b = map(int, input().split())
c, d = map(int, input().split())

e = b - d
f = b - c
g = a - d
h = a - c
print(max(e, f, g, h))
