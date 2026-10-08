X, Y = map(int, input().split())

a = min(X, Y)
b = max(X, Y)
if b - a < 3:
    print("Yes")
else:
    print("No")
