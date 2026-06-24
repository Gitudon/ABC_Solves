import sys
from collections import deque

sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
A = [input() for _ in range(H)]


sx, sy = 0, 0
gx, gy = 0, 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            sx, sy = i, j
        if A[i][j] == "G":
            gx, gy = i, j
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = 10**9
dist = [[[INF] * W for _ in range(H)] for _ in range(2)]
dist[0][sx][sy] = 0

q = deque([(0, sx, sy)])
while q:
    (
        c,
        x,
        y,
    ) = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (
            not (0 <= nx < H and 0 <= ny < W)
            or A[nx][ny] == "#"
            or (c == 0 and A[nx][ny] == "x")
            or (c == 1 and A[nx][ny] == "o")
        ):
            continue
        nc = c ^ (A[nx][ny] == "?")
        if dist[nc][nx][ny] != INF:
            continue
        q.append((nc, nx, ny))
        dist[nc][nx][ny] = dist[c][x][y] + 1
ans = min(dist[0][gx][gy], dist[1][gx][gy])
print(ans if ans != INF else -1)
