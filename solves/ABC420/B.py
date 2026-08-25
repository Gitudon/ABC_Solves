N, M = map(int, input().split())

point = [0] * N
S = [input() for _ in range(N)]

for j in range(M):
    buf = ""
    x = 0
    y = 0
    for i in range(N):
        buf += S[i][j]
        if S[i][j] == "0":
            x += 1
        elif S[i][j] == "1":
            y += 1
    if x == 0 or y == 0:
        for i in range(N):
            point[i] += 1
    elif x < y:
        for i in range(N):
            if S[i][j] == "0":
                point[i] += 1
    else:
        for i in range(N):
            if S[i][j] == "1":
                point[i] += 1
MAX = max(point)
ans = []
for i in range(N):
    if point[i] == MAX:
        ans.append(i + 1)
print(*ans)
