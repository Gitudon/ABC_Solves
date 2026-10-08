Y = int(input())

a = Y % 4
if a == 0:
    print(Y + 2)
elif a == 1:
    print(Y + 1)
elif a == 3:
    print(Y + 3)
else:
    print(Y)
