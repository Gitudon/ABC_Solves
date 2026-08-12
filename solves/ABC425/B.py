N = int(input())
A = list(map(int, input().split()))

dist = [i for i in range(1, N + 1)]

P = [0] * N
for i in range(N):
    if A[i] != -1:
        if A[i] in dist:
            P[i] = A[i]
            dist.remove(A[i])
        else:
            print("No")
            exit()
zero_cnt = 0
for p in P:
    if p == 0:
        zero_cnt += 1
if zero_cnt > len(dist):
    print("No")
    exit()
else:
    for i in range(N):
        if P[i] == 0:
            P[i] = dist.pop()
    print("Yes")
    print(*P)
