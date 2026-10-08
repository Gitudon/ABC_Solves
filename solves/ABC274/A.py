A, B = map(int, input().split())

c = str(B / A)
if len(c) == 1:
    c += ".000"
    print(c)
elif len(c) == 3:
    c += "00"
    print(c)
elif len(c) == 4:
    c += "0"
    print(c)
elif len(c) == 5:
    print(c)
else:
    d = int(c[5])
    if d <= 4:
        print(c[:5])
    else:
        e = int(c[4])
        print(c[:4] + str(e + 1))
