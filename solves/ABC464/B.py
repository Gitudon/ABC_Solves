H, W = map(int, input().split())
C = [0] * H
for i in range(H):
    C[i] = input()

up = 0
down = 0
left = 0
right = 0

for i in range(H):
    flag = True
    for j in range(W):
        if C[i][j] == "#":
            flag = False
            break
    if not flag:
        up = i
        break

for i in range(H - 1, up - 1, -1):
    flag = True
    for j in range(W):
        if C[i][j] == "#":
            flag = False
            break
    if not flag:
        down = i
        break

for i in range(W):
    flag = True
    for j in range(up, down + 1):
        if C[j][i] == "#":
            flag = False
            break
    if not flag:
        left = i
        break

for i in range(W - 1, left - 1, -1):
    flag = True
    for j in range(up, down + 1):
        if C[j][i] == "#":
            flag = False
            break
    if not flag:
        right = i
        break

for i in range(up, down + 1):
    for j in range(left, right + 1):
        print(C[i][j], end="")
    print()
