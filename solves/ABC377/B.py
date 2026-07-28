S = [input() for _ in range(8)]
ans = [[True] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            for k in range(8):
                ans[k][j] = False
            for k in range(8):
                ans[i][k] = False
a = 0
for i in range(8):
    for j in range(8):
        if ans[i][j]:
            a += 1
print(a)
