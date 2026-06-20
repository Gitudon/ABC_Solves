N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
dp = [[0 for j in range(2)] for i in range(N + 1)]
for i in range(N):
    dp[i][0] = -4e18
    dp[i][1] = -4e18
dp[0][0] = 0
for i in range(N):
    if X[i] == 0:
        dp[i + 1][0] = max(dp[i][0], max(dp[i][0], dp[i][1]) + Y[i])
    else:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + Y[i])
    dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
    dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
print(max(dp[N][0], dp[N][1]))
