N, T = map(int, input().split())
A = list(map(int, input().split()))

T %= sum(A)
for i in range(N):
    if 0 <= T <= A[i]:
        print(i + 1, T)
    T -= A[i]
