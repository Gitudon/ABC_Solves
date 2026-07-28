N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    adj[A - 1].append(B)
    adj[B - 1].append(A)
for ad in adj:
    print(len(ad), *(sorted(ad)))
