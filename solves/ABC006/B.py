import sys

sys.setrecursionlimit(10**8)

n = int(input())

memo = [-1] * (10**7)


def tribonacci(n):
    if memo[n] == -1:
        if n == 0 or n == 1:
            memo[n] = 0
        elif n == 2:
            memo[n] = 1
        else:
            memo[n] = (
                tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
            ) % 10007
    return memo[n]


print(tribonacci(n - 1))
