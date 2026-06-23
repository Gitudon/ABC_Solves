H, W = map(int, input().split())
ss = [input() for _ in range(H)]
snuke = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}
visit = [[False] * W for _ in range(H)]
stack = list([(0, 0)])
while stack:
    ty, tx = stack.pop()
    visit[ty][tx] = True
    if ss[ty][tx] in snuke:
        next = snuke[ss[ty][tx]]
        for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ny = ty + dy
            nx = tx + dx
            if not (0 <= ny < H):
                continue
            if not (0 <= nx < W):
                continue
            if visit[ny][nx]:
                continue
            if ss[ny][nx] != next:
                continue
            stack.append((ny, nx))
    else:
        break
ans = "Yes" if visit[H - 1][W - 1] else "No"
print(ans)
