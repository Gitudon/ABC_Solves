N, X = map(int, input().split())
ans = -1
alcohol = 0
X *= 100
for i in range(N):
    v, p = map(int, input().split())
    alcohol += v * p
    if alcohol > X:
        ans = i + 1
        break
print(ans)
