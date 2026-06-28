N, K, Q = map(int, input().split())

points = [K] * N
for _ in range(Q):
    A = int(input())
    points[A - 1] += 1

for i in range(N):
    if points[i] > Q:
        print("Yes")
    else:
        print("No")
