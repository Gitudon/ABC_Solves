# 再帰関数を用いた全探索

N = int(input())
A = [input() for i in range(N)]


def solve(i, j, n, ans, k):
    if n == N:
        return ans
    if k == 0:
        return solve((i + 1) % N, j, n + 1, ans + A[i][j], 0)
    elif k == 1:
        return solve((i - 1) % N, j, n + 1, ans + A[i][j], 1)
    elif k == 2:
        return solve(i, (j + 1) % N, n + 1, ans + A[i][j], 2)
    elif k == 3:
        return solve(i, (j - 1) % N, n + 1, ans + A[i][j], 3)
    elif k == 4:
        return solve((i + 1) % N, (j + 1) % N, n + 1, ans + A[i][j], 4)
    elif k == 5:
        return solve((i + 1) % N, (j - 1) % N, n + 1, ans + A[i][j], 5)
    elif k == 6:
        return solve((i - 1) % N, (j + 1) % N, n + 1, ans + A[i][j], 6)
    elif k == 7:
        return solve((i - 1) % N, (j - 1) % N, n + 1, ans + A[i][j], 7)


ans = 0
for i in range(N):
    for j in range(N):
        for k in range(8):
            ans = max(ans, int(solve(i, j, 0, "", k)))
print(ans)
