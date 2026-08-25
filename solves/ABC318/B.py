N = int(input())
M = [[False] * 100 for i in range(100)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    for j in range(A, B):
        for k in range(C, D):
            M[k][j] = True
ans = 0
for i in range(100):
    for j in range(100):
        if M[i][j]:
            ans += 1
print(ans)
