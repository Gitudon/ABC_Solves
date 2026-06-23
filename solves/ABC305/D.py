from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
r = [0] * Q
l = [0] * Q
for i in range(Q):
    r[i], l[i] = map(int, input().split())
fA = [0] * N  # A[i]分までに何分寝たか
for i in range(1, N):
    if i % 2 == 0:
        fA[i] = fA[i - 1] + A[i] - A[i - 1]
    else:
        fA[i] = fA[i - 1]


def solve(r):
    i = bisect_left(A, r)
    if i % 2 != 0:
        return fA[i]
    else:
        return fA[i] - (A[i] - r)


for i in range(Q):
    print(solve(l[i]) - solve(r[i]))
