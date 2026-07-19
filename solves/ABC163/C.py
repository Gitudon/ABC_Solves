N = int(input())
A = list(map(int, input().split()))

buka = [0] * N
for i in range(N - 1):
    buka[A[i] - 1] += 1

for i in range(N):
    print(buka[i])
