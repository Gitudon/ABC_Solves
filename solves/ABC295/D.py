S = input()
dp = [0] * (1 << 10)
ans = 0
now = 0
dp[0] = 1
for i in S:
    now ^= 1 << (int(i))
    ans += dp[now]
    dp[now] += 1
print(ans)
