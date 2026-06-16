N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

kiroku = [[0] * (10**5 + 1) for _ in range(N)]
for i in range(N):
    for j in range(A[i][0]):
        kiroku[i][A[i][j + 1]] += 1

ans = []
for i in range(N):
    for j in range(i + 1, N):
        Ki = A[i][0]
        Kj = A[j][0]
        buf = 0
        if Ki > Kj:
            for k in range(Kj):
                buf += kiroku[i][A[j][k + 1]]
        else:
            for k in range(Ki):
                buf += kiroku[j][A[i][k + 1]]
        ans.append(buf / (Ki * Kj))

print(max(ans))
