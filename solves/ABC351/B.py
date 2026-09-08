N = int(input())
A = [0] * N
for i in range(N):
    A[i] = input()
B = [0] * N
for i in range(N):
    B[i] = input()
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            ans = [i + 1, j + 1]
            print(*ans)
            exit()
