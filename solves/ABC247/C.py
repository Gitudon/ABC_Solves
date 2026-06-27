N = int(input())


def solve(N):
    if N == 1:
        return [1]
    else:
        return solve(N - 1) + [N] + solve(N - 1)


print(*solve(N))
