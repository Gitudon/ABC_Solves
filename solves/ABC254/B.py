N = int(input())
A = [[] for i in range(N)]
for i in range(N):
    for j in range(i + 1):
        if j == 0 or j == i:
            A[i].append(1)
        else:
            A[i].append(A[i - 1][j - 1] + A[i - 1][j])
for i in range(N):
    print(*A[i])
