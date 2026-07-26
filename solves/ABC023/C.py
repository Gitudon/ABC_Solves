R, C, K = map(int, input().split())
N = int(input())
r = [0] * N
c = [0] * N
row = [0] * R
col = [0] * C
for i in range(N):
    r[i], c[i] = map(int, input().split())
    r[i] -= 1
    c[i] -= 1
    row[r[i]] += 1
    col[c[i]] += 1

num = [0] * (N + 1)
for i in range(C):
    num[col[i]] += 1

A = 0
for i in range(R):
    if K >= row[i]:
        A += num[K - row[i]]

B = 0
C = 0
for i in range(N):
    sum_num = row[r[i]] + col[c[i]]
    if sum_num == K:
        B += 1
    elif sum_num == K + 1:
        C += 1

print(A - B + C)
