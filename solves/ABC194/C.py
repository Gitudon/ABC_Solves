N = int(input())
A = list(map(int, input().split()))

one = 0
two = 0
for i in range(N):
    one += A[i] ** 2
    two += A[i]
print(N * one - two**2)
