N, X, T = map(int, input().split())

a = N // X
b = N % X
if b == 0:
    print(a * T)
else:
    print(a * T + T)
