X, Y = map(int, input().split())

if X - Y >= 0:
    print(0)
else:
    a = Y - X
    b = a // 10
    c = a % 10
    if c == 0:
        print(b)
    else:
        print(b + 1)
