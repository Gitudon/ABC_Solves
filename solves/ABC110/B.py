N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = "War"
for i in range(X + 1, Y + 1):
    if max(x) < i <= min(y):
        ans = "No War"

print(ans)
