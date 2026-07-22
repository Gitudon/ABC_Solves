N = int(input())
A = list(map(int, input().split()))

ans = 0
current = 0
for i in range(1, N + 1):
    current -= A[-i]
    if current < 0:
        ans += abs(current)
        current = 0

print(ans)
