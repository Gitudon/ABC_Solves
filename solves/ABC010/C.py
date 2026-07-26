tx_a, ty_a, tx_b, ty_b, T, V = map(int, input().split())
n = int(input())

ans = "NO"
for _ in range(n):
    x, y = map(int, input().split())
    d1 = ((tx_a - x) ** 2 + (ty_a - y) ** 2) ** 0.5
    d2 = ((tx_b - x) ** 2 + (ty_b - y) ** 2) ** 0.5
    if d1 + d2 <= T * V:
        ans = "YES"
        break
print(ans)
