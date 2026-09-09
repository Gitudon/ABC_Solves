n, X = map(int, input().split())
a = list(map(int, input().split()))

binary_X = bin(X)[2:]
binary_X = binary_X.zfill(n)[::-1]

ans = 0
for i in range(n):
    if binary_X[i] == "1":
        ans += a[i]
print(ans)
