N, W = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0


def solve(cnt, value, volume):
    global ans
    if cnt == N:
        if volume <= W:
            ans = max(ans, value)
        return
    solve(cnt + 1, value + A[cnt], volume + B[cnt])
    solve(cnt + 1, value, volume)


solve(0, 0, 0)
print(ans)
