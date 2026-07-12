T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = "yes"
if N < M:
    ans = "no"
for i in range(M):
    flag = False
    for j in range(len(A)):
        if B[i] - A[j] <= T and B[i] >= A[j]:
            del A[j]
            flag = True
            break
    if not flag:
        ans = "no"
print(ans)
