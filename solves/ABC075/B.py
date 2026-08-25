H, W = map(int, input().split())

S = [input() for _ in range(H)]

ans = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] = "#"
            continue
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                    ans[i][j] += 1

for i in range(H):
    print("".join(map(str, ans[i])))
