N = int(input())
S = input()
dp = [0, 0, 0]
rock, scissors, paper = 0, 1, 2
for c in S:
    prev_dp = dp[:]
    dp[rock] = max(prev_dp[scissors], prev_dp[paper])
    dp[scissors] = max(prev_dp[rock], prev_dp[paper])
    dp[paper] = max(prev_dp[rock], prev_dp[scissors])

    if c == "R":
        dp[scissors] = 0
        dp[paper] += 1
    elif c == "S":
        dp[paper] = 0
        dp[rock] += 1
    elif c == "P":
        dp[rock] = 0
        dp[scissors] += 1

print(max(dp))
