def distance(x, y):
    return (x) ** 2 + (y) ** 2


ans = 0
N, D = map(int, input().split())
for i in range(N):
    X, Y = map(int, input().split())
    if distance(X, Y) <= D**2:
        ans += 1
print(ans)
