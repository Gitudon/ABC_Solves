import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = 10**10
for a in A:
    idx = bisect.bisect_left(B, a)
    if idx < M:
        ans = min(ans, abs(a - B[idx]))
    if idx > 0:
        ans = min(ans, abs(a - B[idx - 1]))
print(ans)
