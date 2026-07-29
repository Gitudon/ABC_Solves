N, X = map(int, input().split())
m = [0] * N
for i in range(N):
    m[i] = int(input())

ans = N
X -= sum(m)
foo = min(m)
ans += X // foo
print(ans)
