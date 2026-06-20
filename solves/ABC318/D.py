N = int(input())
D = [list(map(int, input().split())) for _ in range(N - 1)]
weights = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j, w in enumerate(D[i]):
        weights[i][i + j + 1] = w
        weights[i + j + 1][i] = w
dp = [0] * (1 << N)
for bit in range(1 << N):
    for i in range(N):
        for j in range(i + 1, N):
            if (bit & (1 << i)) and (bit & (1 << j)):
                dp[bit] = max(dp[bit], dp[bit ^ (1 << i) ^ (1 << j)] + weights[i][j])
print(dp[(1 << N) - 1])
