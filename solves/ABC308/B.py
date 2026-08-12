N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    if C[i] not in D:
        ans += P[0]
    for j in range(M):
        if C[i] == D[j]:
            ans += P[j + 1]
print(ans)
