N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

x = 0
ans = 0
for i in range(M):
    while x < N and A[x] * 2 < B[i]:
        x += 1
    if x < N:
        ans += 1
        x += 1

print(ans)
