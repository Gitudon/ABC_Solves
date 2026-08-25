N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
for i in range(N):
    ans *= A[i]
    if len(str(ans)) >= K + 1:
        ans = 1

print(ans)
