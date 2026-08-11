s = int(input())
a = [s]
b = 0
i = 1


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


while b == 0:
    c = f(a[i - 1])
    if c in a:
        print(i + 1)
        b = 1
    else:
        a.append(c)
        i += 1
