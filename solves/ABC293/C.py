import sys

sys.setrecursionlimit(10**7)
H, W = map(int, input().split())
A = [[0] * W for i in range(H)]
for i in range(H):
    A[i] = list(map(int, input().split()))
ans = 0


def happy(i, j, li):
    global ans
    if i == H - 1:
        if j == W - 1:
            ans += 1
            return
        elif A[i][j + 1] not in li:
            happy(i, j + 1, li + [A[i][j + 1]])
    elif j == W - 1:
        if A[i + 1][j] not in li:
            happy(i + 1, j, li + [A[i + 1][j]])
    else:
        if A[i + 1][j] not in li:
            happy(i + 1, j, li + [A[i + 1][j]])
        if A[i][j + 1] not in li:
            happy(i, j + 1, li + [A[i][j + 1]])


happy(0, 0, [A[0][0]])
print(ans)
