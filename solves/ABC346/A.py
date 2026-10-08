N = int(input())
A = list(map(int, input().split()))
B = [0] * (N - 1)
for i in range(N - 1):
    B[i] = A[i] * A[i + 1]
print(*B)
