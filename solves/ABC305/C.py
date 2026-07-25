H, W = map(int, input().split())
S = [0] * H
for i in range(H):
    S[i] = input()
for i in range(H):
    for j in range(W):
        c = 0
        if S[i][j] == ".":
            if i == 0:
                if j == 0:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                elif j == W - 1:
                    if S[i][j - 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                else:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if S[i][j - 1] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
            elif i == H - 1:
                if j == 0:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                elif j == W - 1:
                    if S[i][j - 1] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                else:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if S[i][j - 1] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
            else:
                if j == 0:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                elif j == W - 1:
                    if S[i][j - 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
                else:
                    if S[i][j + 1] == "#":
                        c += 1
                    if S[i + 1][j] == "#":
                        c += 1
                    if S[i][j - 1] == "#":
                        c += 1
                    if S[i - 1][j] == "#":
                        c += 1
                    if c >= 2:
                        print(i + 1, j + 1)
