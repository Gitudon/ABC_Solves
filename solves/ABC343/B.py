N = int(input())
A = [0] * N
for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    ans = []
    for j in range(N):
        if A[i][j] == 1:
            ans.append(j + 1)
    print(*ans)
