S = [0] * 5
for i in range(5):
    S[i] = input()

ans = 5

# 横
for i in range(5):
    buf = 0
    for j in range(5):
        if S[i][j] == ".":
            buf += 1
    ans = min(ans, buf)

# 縦
for i in range(5):
    buf = 0
    for j in range(5):
        if S[j][i] == ".":
            buf += 1
    ans = min(ans, buf)

# 左上から右下
buf = 0
for i in range(5):
    if S[i][i] == ".":
        buf += 1
ans = min(ans, buf)

# 右上から左下
buf = 0
for i in range(5):
    if S[4 - i][i] == ".":
        buf += 1
ans = min(ans, buf)

print(ans)
