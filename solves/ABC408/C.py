N, M = map(int, input().split())

zyoheki = [0] * (N + 2)

for _ in range(M):
    L, R = map(int, input().split())
    zyoheki[L] += 1
    zyoheki[R + 1] -= 1

for i in range(1, N + 1):
    zyoheki[i] += zyoheki[i - 1]

print(min(zyoheki[1 : N + 1]))
