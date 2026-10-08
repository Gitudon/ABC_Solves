A, B, C = map(int, input().split())

s = B // A
if s <= C:
    print(s)
else:
    print(C)
