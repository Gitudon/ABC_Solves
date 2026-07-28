N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
aki = K
while True:
    if A == []:
        ans += 1
        break
    else:
        if aki < A[0]:
            ans += 1
            aki = K
        else:
            aki -= A[0]
            A = A[1:]
print(ans)
