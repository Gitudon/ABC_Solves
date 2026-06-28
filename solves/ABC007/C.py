from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

dist = [[-1] * C for _ in range(R)]
q = deque([(sy - 1, sx - 1)])
dist[sy - 1][sx - 1] = 0

while q:
    y, x = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and c[ny][nx] != "#" and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
print(dist[gy - 1][gx - 1])
