X, Y = map(int, input().split())


def f(n):
    if n == 1:
        return X
    if n == 2:
        return Y
    return int(str(f(n - 1) + f(n - 2))[::-1])


print(f(10))
