N, K = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(set(A))
B = [i for i in range(N)]
ans = 0
for i in range(min(K, len(A))):
    if A[i] == B[i]:
        ans = i + 1
    else:
        break
print(ans)
