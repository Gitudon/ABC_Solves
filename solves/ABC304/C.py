import math
import sys

sys.setrecursionlimit(5000)
N, D = map(int, input().split())
X = [0] * N
Y = [0] * N
Z = [False] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())


def eucrid(a1, a2, b1, b2):
    return math.sqrt((a1 - b1) ** 2 + (a2 - b2) ** 2)


def kansen(z):
    a = []
    for i in range(N):
        if not Z[i]:
            if eucrid(X[z], Y[z], X[i], Y[i]) <= D:
                Z[i] = True
                a.append(i)
    for i in range(len(a)):
        kansen(a[i])


Z[0] = True
kansen(0)
for i in range(N):
    if Z[i]:
        print("Yes")
    else:
        print("No")
