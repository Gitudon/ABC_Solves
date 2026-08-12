H, W, D = map(int, input().split())
S = [0] * H
for i in range(H):
    S[i] = input()
ans = 2
for i in range(H):
    for j in range(W):
        for k in range(H):
            for l in range(W):
                if i != k or j != l:
                    warm = [[0] * W for _ in range(H)]
                    if S[i][j] == "." and S[k][l] == ".":
                        for y in range(H):
                            for x in range(W):
                                if S[y][x] == ".":
                                    if (abs(i - y) + abs(j - x)) <= D or (
                                        abs(k - y) + abs(l - x)
                                    ) <= D:
                                        warm[y][x] = 1
                        cnt = 0
                        for y in range(H):
                            for x in range(W):
                                if warm[y][x] == 1:
                                    cnt += 1
                        ans = max(ans, cnt)
print(ans)
