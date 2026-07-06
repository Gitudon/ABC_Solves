N, K = map(int, input().split())
R = list(map(int, input().split()))


def solve(buf):
    if len(buf) == N:
        if sum(buf) % K == 0:
            print(*buf)
        return
    for i in range(1, R[len(buf)] + 1):
        solve(buf + [i])


for i in range(1, R[0] + 1):
    solve([i])
