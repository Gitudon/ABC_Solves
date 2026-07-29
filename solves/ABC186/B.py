H, W = map(int, input().split())
A = [0] * H
for i in range(H):
    A[i] = list(map(int, input().split()))
mini = A[0][0]
for i in range(H):
    for j in range(W):
        if A[i][j] < mini:
            mini = A[i][j]
ans = 0
for i in range(H):
    for j in range(W):
        ans += A[i][j] - mini
print(ans)
