N, V = map(int, input().split())
W = list(map(int, input().split()))

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            buf = W[i] + W[j] + W[k]
            if i + j + k + 3 <= V:
                ans = max(ans, buf)
print(ans)
