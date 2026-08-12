N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = []
for i in range(N):
    for j in range(N):
        if i == j:
            ans.append(A[i] + B[j])
        else:
            ans.append(max(A[i], B[j]))
print(min(ans))
