H, W = map(int, input().split())
S = [input() for _ in range(H)]

koma1_x = -1
koma1_y = -1
koma2_x = -1
koma2_y = -1
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            if koma1_x == -1:
                koma1_x = i
                koma1_y = j
            else:
                koma2_x = i
                koma2_y = j

print(abs(koma1_x - koma2_x) + abs(koma1_y - koma2_y))
