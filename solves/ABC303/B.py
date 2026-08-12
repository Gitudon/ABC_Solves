N, M = map(int, input().split())
a = [[]] * M
for i in range(M):
    a[i] = list(map(int, input().split()))
b = [[0] * N for i in range(N)]
c = 0
for i in range(M):
    for j in range(N - 1):
        b[(a[i][j]) - 1][(a[i][j + 1]) - 1] += 1
        b[(a[i][j + 1]) - 1][(a[i][j]) - 1] += 1
for i in range(N):
    for j in range(N):
        if b[i][j] == 0 and i != j:
            c += 1
print(c // 2)
