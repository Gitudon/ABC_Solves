N = int(input())
q, r = [0] * N, [0] * N
for i in range(N):
    q[i], r[i] = map(int, input().split())
Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    hinichi = r[t - 1]
    if hinichi < d:
        increment_count = (d - hinichi + q[t - 1] - 1) // q[t - 1]
        hinichi += increment_count * q[t - 1]
    print(hinichi)
