N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(2 * N - 2):
        if A[j] == A[j + 2] and A[j] == i + 1:
            ans += 1
print(ans)
