N, D = map(int, input().split())
T = [0] * N
L = [0] * N
for i in range(N):
    T[i], L[i] = map(int, input().split())
for k in range(1, D + 1):
    ans = 0
    for i in range(N):
        buf = T[i] * (L[i] + k)
        if ans < buf:
            ans = buf
    print(ans)
