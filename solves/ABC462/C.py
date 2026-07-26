N = int(input())

XY = [0] * N
for i in range(N):
    X, Y = map(int, input().split())
    XY[i] = (X - 1, Y - 1)

XY.sort()
min_val = N
ans = 0
for x, y in XY:
    min_val = min(min_val, y)
    ans += min_val == y
print(ans)
