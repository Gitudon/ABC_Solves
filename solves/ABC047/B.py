W, H, N = map(int, input().split())
chohokei = [[1] * (W) for _ in range(H)]
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for j in range(H):
            for k in range(x):
                chohokei[j][k] = 0
    elif a == 2:
        for j in range(H):
            for k in range(x, W):
                chohokei[j][k] = 0
    elif a == 3:
        for j in range(y):
            for k in range(W):
                chohokei[j][k] = 0
    else:
        for j in range(y, H):
            for k in range(W):
                chohokei[j][k] = 0
ans = 0
for i in range(H):
    for j in range(W):
        ans += chohokei[i][j]
print(ans)
