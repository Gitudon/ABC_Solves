N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
point = 0
for i in range(M):
    point += A[B[i] - 1]
print(point)
