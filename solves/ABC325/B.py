N = int(input())
W, X = [0] * N, [0] * N
for i in range(N):
    W[i], X[i] = map(int, input().split())

ans = 0
for t in range(0, 24):
    tmp = 0
    for i in range(N):
        time = (t + X[i]) % 24
        if 9 <= time <= 17:
            tmp += W[i]
    ans = max(ans, tmp)
print(ans)
