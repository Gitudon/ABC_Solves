N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = "Yes"
for i in range(M):
    flag = False
    for j in range(N):
        if B[i] == A[j]:
            A[j] = 0
            flag = True
            break
    if not flag:
        ans = "No"
        break
print(ans)
