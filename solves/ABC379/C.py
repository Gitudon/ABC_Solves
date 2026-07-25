N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
solve = {}
for i in range(M):
    solve[X[i] - 1] = A[i]
solve = sorted(solve.items())
sum = 0
sum_idx = 0
for i in range(M):
    if sum < solve[i][0]:
        print(-1)
        exit()
    sum += solve[i][1]
    sum_idx += solve[i][1] * (solve[i][0] + 1)
if sum != N:
    print(-1)
    exit()
print(N * (N + 1) // 2 - sum_idx)
