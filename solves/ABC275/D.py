memo = {}


def f(N):
    if N in memo:
        return memo[N]
    if N == 0:
        return 1
    memo[N] = f(N // 2) + f(N // 3)
    return memo[N]


N = int(input())
print(f(N))
