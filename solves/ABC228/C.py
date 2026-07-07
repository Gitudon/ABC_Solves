N, K = map(int, input().split())
P = [0] * N
for i in range(N):
    P[i] = sum(list(map(int, input().split())))

Q = sorted(P, reverse=True)
for i in range(N):
    if P[i] + 300 >= Q[K - 1]:
        print("Yes")
    else:
        print("No")
