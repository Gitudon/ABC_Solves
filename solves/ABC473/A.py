N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N // 2, N):
    ans += A[i]
print(ans)
