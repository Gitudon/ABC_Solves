N, A, B = map(int, input().split())

ans = 0

for i in range(N):
    s, d = map(str, input().split())
    d = int(d)
    if s == "East":
        if d < A:
            ans += A
        elif A <= d <= B:
            ans += d
        elif d > B:
            ans += B
    elif s == "West":
        if d < A:
            ans -= A
        elif A <= d <= B:
            ans -= d
        elif d > B:
            ans -= B

if ans > 0:
    print("East", ans)
elif ans < 0:
    print("West", abs(ans))
else:
    print(0)
