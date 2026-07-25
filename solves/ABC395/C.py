N = int(input())
A = list(map(int, input().split()))

ans = -1
last_seen = {}

for i in range(N):
    if A[i] in last_seen:
        distance = i - last_seen[A[i]] + 1
        if ans == -1:
            ans = distance
        else:
            ans = min(ans, distance)
    last_seen[A[i]] = i

print(ans)
