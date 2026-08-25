N = int(input())
A = [0] * N
P = [0] * N
X = [0] * N
for i in range(N):
    A[i], P[i], X[i] = map(int, input().split())

ans = -1
for i in range(N):
    if X[i] - A[i] > 0:
        if ans == -1:
            ans = P[i]
        else:
            ans = min(ans, P[i])
print(ans)
