N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minimum = [0] * N
for i in range(N):
    minimum[i] = min(A[i], B[i])
ans = sum(minimum)

for _ in range(Q):
    query = list(map(str, input().split()))
    c = query[0]
    X = int(query[1])
    V = int(query[2])
    if c == "A":
        A[X - 1] = V
    else:
        B[X - 1] = V
    ans -= minimum[X - 1]
    minimum[X - 1] = min(A[X - 1], B[X - 1])
    ans += minimum[X - 1]
    print(ans)
