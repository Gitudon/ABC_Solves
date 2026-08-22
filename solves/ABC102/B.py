N = int(input())
A = list(map(int, input().split()))

ans = -1000000000

for i in range(N):
    for j in range(i + 1, N):
        ans = max(ans, abs(A[j] - A[i]))
print(ans)
