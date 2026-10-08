A, B, C = map(int, input().split())

a = B // C
b = C * a
if b < A:
    print(-1)
else:
    print(b)
