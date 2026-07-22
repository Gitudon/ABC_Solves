H, W = map(int, input().split())
S = [0] * H
for i in range(H):
    S[i] = input()
for i in range(H):
    for j in range(W - 1):
        if S[i][j] == S[i][j + 1] and S[i][j] == "T":
            S[i] = S[i][:j] + "PC" + S[i][j + 2 :]
for i in range(H):
    print(S[i])
