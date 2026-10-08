a, b, c = map(int, input().split())

M = max(a, b, c)
m = min(a, b, c)
d = a + b + c - M - m
if d == b:
    print("Yes")
else:
    print("No")
