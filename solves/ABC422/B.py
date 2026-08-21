H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = "Yes"
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            black = 0
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = (i + di), (j + dj)
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if S[ni][nj] == "#":
                    black += 1
            if black != 2 and black != 4:
                ans = "No"
print(ans)
