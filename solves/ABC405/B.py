N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(N + 1):
    flag = True
    for j in range(1, M + 1):
        if j not in A:
            flag = False
            break
    if flag:
        ans += 1
        A = A[:-1]
    else:
        print(ans)
        break
