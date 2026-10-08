N, S, K = map(int, input().split())
s = 0
for _ in range(N):
    P, Q = map(int, input().split())
    s += P * Q
if s >= S:
    print(s)
else:
    print(s + K)
