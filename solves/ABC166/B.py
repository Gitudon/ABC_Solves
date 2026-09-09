N, K = map(int, input().split())

d = [0] * K
A = [0] * K

for i in range(K):
    d[i] = int(input())
    A[i] = list(map(int, input().split()))

snuke = [0] * N
for i in range(K):
    for j in range(d[i]):
        snuke[A[i][j] - 1] += 1
ans = 0
for i in range(N):
    if snuke[i] == 0:
        ans += 1
print(ans)
