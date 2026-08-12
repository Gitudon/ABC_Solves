N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())
A = sorted(A, reverse=True)
ans = A[0]
for i in range(N):
    if A[i] != ans and ans == A[0]:
        ans = A[i]
print(ans)
