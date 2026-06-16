N = int(input())
A = list(map(int, input().split()))
C = [0] * N
D = [0] * (N + 1)

for i in range(N):
    if i != 0:
        C[i] = C[i - 1] + D[i]
        A[i] += C[i]
    cnt = min(N - i - 1, A[i])
    A[i] -= cnt
    D[i + 1] += 1
    D[min(N, i + cnt + 1)] -= 1
print(*A)
