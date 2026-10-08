A, B, C = map(int, input().split())
if A != B and B == C:
    print(A)
elif A == B and B != C:
    print(C)
else:
    print(B)
