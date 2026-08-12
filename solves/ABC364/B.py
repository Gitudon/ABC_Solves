H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C = [0] * H
for i in range(H):
    C[i] = input()
X = input()
Si -= 1
Sj -= 1
for i in range(len(X)):
    if X[i] == "U":
        if Si - 1 >= 0 and C[Si - 1][Sj] == ".":
            Si -= 1
    elif X[i] == "D":
        if Si + 1 < H and C[Si + 1][Sj] == ".":
            Si += 1
    elif X[i] == "L":
        if Sj - 1 >= 0 and C[Si][Sj - 1] == ".":
            Sj -= 1
    elif X[i] == "R":
        if Sj + 1 < W and C[Si][Sj + 1] == ".":
            Sj += 1
print(Si + 1, Sj + 1)
