A, B = map(str, input().split())

a = len(A)
b = len(B)

ans = "Easy"
if a >= b:
    for i in range(1, b + 1):
        if int(A[-i]) + int(B[-i]) >= 10:
            ans = "Hard"
else:
    for i in range(1, a + 1):
        if int(A[-i]) + int(B[-i]) >= 10:
            ans = "Hard"
print(ans)
