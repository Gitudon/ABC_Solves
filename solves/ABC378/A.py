A = list(map(int, input().split()))
A.sort()
ans = 0
while A != []:
    for i in range(1, len(A)):
        if A[i] == A[0]:
            ans += 1
            A.pop(i)
            break
    A.pop(0)
print(ans)
