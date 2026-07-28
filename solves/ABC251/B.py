N, W = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
flag = [False] * W
for i in range(N):
    if A[i] <= W:
        flag[A[i] - 1] = True
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            flag[A[i] + A[j] - 1] = True
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                flag[A[i] + A[j] + A[k] - 1] = True
for n in flag:
    if n:
        ans += 1
print(ans)
