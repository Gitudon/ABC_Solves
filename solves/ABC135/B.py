N = int(input())
p = list(map(int, input().split()))

q = sorted(p)
ans = "YES"

wrong = 0
for i in range(N):
    if p[i] != q[i]:
        wrong += 1

if wrong > 2:
    ans = "NO"
print(ans)
