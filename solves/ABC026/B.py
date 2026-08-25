import math

N = int(input())
R = [0] * N
for i in range(N):
    R[i] = int(input())
R.sort(reverse=True)
foo = 0
for i in range(N):
    if i % 2 == 0:
        foo += R[i] ** 2
    else:
        foo -= R[i] ** 2
print(foo * math.pi)
