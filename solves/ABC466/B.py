N, M = map(int, input().split())

k = [-1] * M
for _ in range(N):
    C, S = map(int, input().split())
    k[C - 1] = max(k[C - 1], S)

for i in range(M):
    print(k[i])
