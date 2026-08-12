N = int(input())
a = list(map(int, input().split()))

zenin = sum(a)
if zenin % N != 0:
    print(-1)
else:
    ans = 0
    average = zenin // N
    for i in range(N - 1):
        if sum(a[: i + 1]) != average * (i + 1):
            ans += 1
    print(ans)
