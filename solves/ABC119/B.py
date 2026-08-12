N = int(input())
ans = 0

btc = 380000.0

for i in range(N):
    x, u = map(str, input().split())
    x = float(x)
    if u == "BTC":
        ans += x * btc
    else:
        ans += x
print(ans)
