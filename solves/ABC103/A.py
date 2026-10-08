A1, A2, A3 = map(int, input().split())
ans = 0
a = abs(A3 - A1)
b = abs(A2 - A1)
c = abs(A3 - A2)

r1 = b + c
r2 = a + c
r3 = b + a
print(min(r1, r2, r3))
