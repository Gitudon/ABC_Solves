N, Q = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(N)]
for _ in range(Q):
    s, t = map(int, input().split())
    print(a[s - 1][t - 1])
