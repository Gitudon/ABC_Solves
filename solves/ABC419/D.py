N, M = map(int, input().split())
S = list(input())
T = list(input())

swap_flag = False

swap_count = [0] * (N + 1)

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    swap_count[L] += 1
    swap_count[R] -= 1

cumulative_swaps = 0
for i in range(N):
    cumulative_swaps += swap_count[i]
    if cumulative_swaps % 2 != 0:
        S[i], T[i] = T[i], S[i]

print("".join(S))
