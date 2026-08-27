N = int(input())
P = list(map(int, input().split()))

rank = [0] * N

r = 1

while r <= N:
    max_score = 0
    for i in range(N):
        if rank[i] == 0:
            max_score = max(max_score, P[i])
    k = 0
    for i in range(N):
        if P[i] == max_score and rank[i] == 0:
            rank[i] = r
            k += 1
    r += k

for i in range(N):
    print(rank[i])
