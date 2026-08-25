N, L, R = map(int, input().split())
A = list(map(int, input().split()))

X = []
for i in range(N):
    if A[i] < L:
        X.append(L)
    elif R <= A[i]:
        X.append(R)
    else:
        X.append(A[i])
print(*X)
