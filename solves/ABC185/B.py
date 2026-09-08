N, M, T = map(int, input().split())

battery = N
now = 0
ans = "Yes"
for i in range(M):
    a, b = map(int, input().split())
    battery -= a - now
    if battery <= 0:
        ans = "No"
    battery += b - a
    if battery > N:
        battery = N
    now = b
battery -= T - now
if battery <= 0:
    ans = "No"
print(ans)
