N, M = map(int, input().split())

L = [0] * M
R = [0] * M

for i in range(M):
    L[i], R[i] = map(int, input().split())

ans = min(R) - max(L) + 1
if ans < 0:
    ans = 0
print(ans)
