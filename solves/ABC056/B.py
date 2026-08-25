W, a, b = map(int, input().split())

if a <= b:
    if a <= b <= a + W:
        print(0)
    else:
        print(b - (a + W))
else:
    if b <= a <= b + W:
        print(0)
    else:
        print(a - (b + W))
