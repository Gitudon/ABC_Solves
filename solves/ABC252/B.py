N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
oisi = max(A)
ans = "No"
for i in range(K):
    if A[B[i] - 1] == oisi:
        ans = "Yes"
print(ans)
