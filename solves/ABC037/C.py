n, k = map(int, input().split())
a = list(map(int, input().split()))

ruisekiwa = [0] * n
ruisekiwa[0] = a[0]
for i in range(1, n):
    ruisekiwa[i] = ruisekiwa[i - 1] + a[i]

ans = 0
for i in range(n - k + 1):
    ans += ruisekiwa[i + k - 1]
    if i > 0:
        ans -= ruisekiwa[i - 1]
print(ans)
