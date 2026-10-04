N, M = map(int, input().split())

ans = [M // N] * N
M %= N
for i in range(M):
    ans[i] += 1

for a in ans:
    print(a)
