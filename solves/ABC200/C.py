def conb(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2


N = int(input())
A = list(map(int, input().split()))

buf = [0] * 200
for i in range(N):
    buf[A[i] % 200] += 1

ans = 0
for i in range(200):
    ans += conb(buf[i])
print(ans)
