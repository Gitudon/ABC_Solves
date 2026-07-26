N, Q = map(int, input().split())
A = [0] * (N + 1)
B = [0] * (Q + 1)
k = 0
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        A[x] += 1
        B[A[x]] += 1
        if B[A[x]] == N:
            k = A[x]
    else:
        if k + x > Q:
            print(0)
        else:
            print(B[k + x])
