N = int(input())
res = [[] for _ in range(N)]

for i in range(N):
    K, *A = map(int, input().split())
    for j in range(K):
        res[A[j] - 1].append(i + 1)

for i in range(N):
    print(len(res[i]), *res[i])
