N = int(input())
A = list(map(int, input().split()))

kirikomi = [0] * 360
kirikomi[0] = 1
current = 0
for a in A:
    current += a
    current %= 360
    kirikomi[current] = 1

ans = 0
cnt = 1
for i in range(360):
    if i == 359:
        if kirikomi[i] == 0:
            cnt += 1
        ans = max(ans, cnt)
    if kirikomi[i] == 0:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
print(ans)
