N, M = map(int, input().split())
A = list(map(int, input().split()))
a = 0

for i in A:
    a += i

ans = N - a

if ans < 0:
    print(-1)
else:
    print(ans)
