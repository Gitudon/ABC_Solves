N, A, X, Y = map(int, input().split())

a = N - A
if a >= 0:
    print(A * X + a * Y)
else:
    print(N * X)
