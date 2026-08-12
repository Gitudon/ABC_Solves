H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            if W - 1 - j >= 4:
                if S[i][j + 1] == "n":
                    if S[i][j + 2] == "u":
                        if S[i][j + 3] == "k":
                            if S[i][j + 4] == "e":
                                for k in range(5):
                                    print(str(i + 1) + " " + str(j + k + 1))
                                exit()
                if H - 1 - i >= 4:
                    if S[i + 1][j + 1] == "n":
                        if S[i + 2][j + 2] == "u":
                            if S[i + 3][j + 3] == "k":
                                if S[i + 4][j + 4] == "e":
                                    for k in range(5):
                                        print(str(i + 1 + k) + " " + str(j + k + 1))
                                    exit()
                if i >= 4:
                    if S[i - 1][j + 1] == "n":
                        if S[i - 2][j + 2] == "u":
                            if S[i - 3][j + 3] == "k":
                                if S[i - 4][j + 4] == "e":
                                    for k in range(5):
                                        print(str(i + 1 - k) + " " + str(j + k + 1))
                                    exit()
            if H - 1 - i >= 4:
                if S[i + 1][j] == "n":
                    if S[i + 2][j] == "u":
                        if S[i + 3][j] == "k":
                            if S[i + 4][j] == "e":
                                for k in range(5):
                                    print(str(i + k + 1) + " " + str(j + 1))
                                exit()
            if i >= 4:
                if S[i - 1][j] == "n":
                    if S[i - 2][j] == "u":
                        if S[i - 3][j] == "k":
                            if S[i - 4][j] == "e":
                                for k in range(5):
                                    print(str(i + 1 - k) + " " + str(j + 1))
                                exit()
                if j >= 4:
                    if S[i - 1][j - 1] == "n":
                        if S[i - 2][j - 2] == "u":
                            if S[i - 3][j - 3] == "k":
                                if S[i - 4][j - 4] == "e":
                                    for k in range(5):
                                        print(str(i + 1 - k) + " " + str(j - k + 1))
                                    exit()
            if j >= 4:
                if S[i][j - 1] == "n":
                    if S[i][j - 2] == "u":
                        if S[i][j - 3] == "k":
                            if S[i][j - 4] == "e":
                                for k in range(5):
                                    print(str(i + 1) + " " + str(j - k + 1))
                                exit()
                if H - 1 - i >= 4:
                    if S[i + 1][j - 1] == "n":
                        if S[i + 2][j - 2] == "u":
                            if S[i + 3][j - 3] == "k":
                                if S[i + 4][j - 4] == "e":
                                    for k in range(5):
                                        print(str(i + 1 + k) + " " + str(j - k + 1))
                                    exit()
