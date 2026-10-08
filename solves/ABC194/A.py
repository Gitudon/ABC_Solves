A, B = map(int, input().split())

c = A + B
if c >= 15 and B >= 8:
    print(1)
else:
    if c >= 10 and B >= 3:
        print(2)
    else:
        if c >= 3:
            print(3)
        else:
            print(4)
