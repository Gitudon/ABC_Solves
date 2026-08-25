import bisect

N = int(input())
A = list(map(int, input().split()))

A.sort()

idx = bisect.bisect_left(A, 0)

l = idx - 1
r = idx

ans = 0
current = 0

for _ in range(N):
    dist_l = current - A[l] if l >= 0 else float("inf")
    dist_r = A[r] - current if r < N else float("inf")
    if dist_l <= dist_r:
        ans += dist_l
        current = A[l]
        l -= 1
    else:
        ans += dist_r
        current = A[r]
        r += 1

print(ans)
