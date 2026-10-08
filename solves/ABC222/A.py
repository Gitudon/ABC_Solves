N = int(input())

a = str(N)
b = len(a)
if b == 4:
    print(a)
elif b == 3:
    print("0" + a)
elif b == 2:
    print("00" + a)
else:
    print("000" + a)
