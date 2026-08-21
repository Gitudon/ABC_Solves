N = int(input())

memo = [0] * (N + 1)


def solve(n):
    if n == 0:
        if memo[n] == 0:
            memo[n] = 2
    if n == 1:
        if memo[n] == 0:
            memo[n] = 1
    if memo[n] == 0:
        memo[n] = solve(n - 1) + solve(n - 2)
    return memo[n]


print(solve(N))
