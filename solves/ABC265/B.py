N, M, T = map(int, input().split())
A = list(map(int, input().split()))
X = [0] * M
Y = [0] * M
for i in range(M):
    X[i], Y[i] = map(int, input().split())
i = 1
j = 0
while T > 0 and i <= (N - 1):
    if j < M:
        if i == X[j]:
            T += Y[j]
            j += 1
    T -= A[i - 1]
    i += 1
if T > 0:
    print("Yes")
else:
    print("No")
