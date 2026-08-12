N, M = map(int, input().split())
X = [list(map(int, input().split()))[1:] for _ in range(M)]
hantei = [[False] * N for _ in range(N)]
for i in range(N):
    hantei[i][i] = True
for x in X:
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            hantei[x[i] - 1][x[j] - 1] = True
            hantei[x[j] - 1][x[i] - 1] = True
ans = True
for i in range(N):
    for j in range(i + 1, N):
        if not hantei[i][j]:
            ans = False
if ans:
    print("Yes")
else:
    print("No")
