import sys

sys.setrecursionlimit(5000)
K = int(input())
l = []
if K <= 10:
    print(K)
    exit()


def solve(x):
    global l
    l.append(x)
    last = x % 10
    for j in range(0, last):
        if x * 10 + j <= 9876543210:
            solve(x * 10 + j)


for i in range(1, 10):
    solve(i)
l.sort()
print(l[K - 1])
