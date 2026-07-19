N = int(input())
segments = [0] * N

for i in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        r -= 0.1
        l += 0.1
    segments[i] = (l, r)

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        flag = False
        if segments[i][0] <= segments[j][0] <= segments[i][1]:
            flag = True
        if segments[i][0] <= segments[j][1] <= segments[i][1]:
            flag = True
        if segments[j][0] <= segments[i][0] <= segments[j][1]:
            flag = True
        if segments[j][0] <= segments[i][1] <= segments[j][1]:
            flag = True
        if flag:
            ans += 1
print(ans)
