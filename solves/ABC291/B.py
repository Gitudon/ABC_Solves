N = int(input())
X = list(map(int, input().split()))
X.sort()
sum = 0
for i in range(N, 4 * N):
    sum += X[i]
print(sum / (3 * N))
