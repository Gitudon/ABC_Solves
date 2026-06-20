# 10^9<<10^100

N, W = map(int, input().split())
blocks = [[] for _ in range(W + 1)]
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    blocks[X[i]].append((Y[i], i))

INF = 10**10
cnt = [0] * N
disappear = [-1] * (N + 1)

for x in range(1, W + 1):
    blocks[x].sort(key=lambda p: p[0])
    for j, (y, i) in enumerate(blocks[x]):
        cnt[i] = j
        disappear[j] = max(disappear[j], y)
    disappear[len(blocks[x])] = INF
for i in range(N):
    disappear[i + 1] = max(disappear[i + 1], disappear[i] + 1)

Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    if disappear[cnt[A - 1]] > T:
        print("Yes")
    else:
        print("No")
