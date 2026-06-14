A, B = map(int, input().split())

if A == 0 or A == 7:
    ans = B
elif B == 0 or B == 7:
    ans = A
elif A == B:
    ans = A
elif (A == 1 or A == 2 or A == 4) and (B == 1 or B == 2 or B == 4):
    ans = A + B
elif A + B == 7:
    ans = 7
elif A % 2 == 0 and A % 2 == 0:
    ans = max(A, B)
elif min(A, B) == 1 or min(A, B) == 2 or min(A, B) == 4:
    ans = max(A, B)
else:
    ans = 7
print(ans)
