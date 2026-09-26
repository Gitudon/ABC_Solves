N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = []
for i in range(N):
    flag = True
    for j in range(N):
        if i == j:
            continue
        if abs(X[i] - X[j]) < D:
            flag = False
            break
    if flag:
        ans.append(i + 1)
ans.sort()
print(len(ans))
print(*ans)
