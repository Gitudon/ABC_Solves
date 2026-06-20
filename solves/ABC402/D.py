N, M = map(int, input().split())

cnt = [0] * N
for i in range(M):
    A, B = map(int, input().split())
    cnt[(A + B) % N] += 1

ans = M * (M - 1) // 2
for i in range(N):
    ans -= cnt[i] * (cnt[i] - 1) // 2

print(ans)
