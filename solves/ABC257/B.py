N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

masu = [0] * N
for i in range(K):
    masu[A[i] - 1] += 1
for i in range(Q):
    if A[L[i] - 1] != N:
        if masu[A[L[i] - 1]] == 0:
            masu[A[L[i] - 1]] += 1
            masu[A[L[i] - 1] - 1] -= 1
            A[L[i] - 1] += 1
print(*A)
