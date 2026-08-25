N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
a = max(A)
for i in range(1, N + 1):
    if A[-i] != a:
        ans = A[-i]
        break
print(ans)
