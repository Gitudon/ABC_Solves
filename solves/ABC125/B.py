import sys

sys.setrecursionlimit(10**7)

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

buf = -10 * 10


def solve(num, value, cost):
    global buf
    if num == N:
        buf = max(buf, value - cost)
        return
    solve(num + 1, value, cost)
    solve(num + 1, value + V[num], cost + C[num])


solve(0, 0, 0)
print(buf)
