N, X = map(int, input().split())

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = X // N
c = X % N
if c == 0:
    print(a[b - 1])
else:
    print(a[b])
