X, K = map(str, input().split())
X = list(map(int, list("0" + X)))
K = int(K)
N = len(X)
if K >= N:
    print(0)
else:
    for i in reversed(range(N - K, N)):
        if X[i] >= 5:
            X[i - 1] += 1
        X[i] = 0
    for i in reversed(range(1, N - K)):
        if X[i] >= 10:
            X[i - 1] += 1
            X[i] %= 10
    for start in range(N):
        if X[start] != 0:
            break
    for i in range(start, N):
        print(X[i], end="")
