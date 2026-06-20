import math

N, M = map(int, input().split())
if N * N < M:
    print(-1)
    exit()
end = math.ceil(M**0.5)
ans = 2**63 - 1
for a in range(1, end + 1):
    b = math.ceil(M / a)
    if b <= N:
        ans = min(ans, a * b)
if ans == (2**63 - 1):
    print(-1)
else:
    print(ans)
