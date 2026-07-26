N, M = map(int, input().split())
k = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))
ans = 0
for i in range(2**N):
    on = [0] * N
    for j in range(N):
        if (i >> j) & 1:
            on[j] = 1
    flag = 1
    for j in range(M):
        cnt = 0
        for l in range(1, k[j][0] + 1):
            if on[k[j][l] - 1]:
                cnt += 1
        if cnt % 2 != p[j]:
            flag = 0
            break
    if flag:
        ans += 1
print(ans)
