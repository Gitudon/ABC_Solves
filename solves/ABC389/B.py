X = int(input())


def kaijo(n):
    if n == 0:
        return 1
    return n * kaijo(n - 1)


for i in range(1, 30):
    if kaijo(i) == X:
        print(i)
        break
