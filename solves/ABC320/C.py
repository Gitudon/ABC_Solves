M = int(input())
S = [0] * 3
for i in range(3):
    S[i] = input()
ans = 1e9
for i in range(3 * M):
    for j in range(3 * M):
        for k in range(3 * M):
            if (
                i != j
                and i != k
                and j != k
                and S[0][i % M] == S[1][j % M] == S[2][k % M]
            ):
                ans = min(ans, max(i, j, k))
if ans < 1e9:
    print(ans)
else:
    print(-1)
