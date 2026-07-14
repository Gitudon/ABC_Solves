def g_1(x):
    x = str(x)
    buf = []
    for i in range(len(x)):
        buf.append(x[i])
    buf = sorted(buf, reverse=True)
    res = ""
    for i in range(len(buf)):
        res += buf[i]
    return int(res)


def g_2(x):
    x = str(x)
    buf = []
    for i in range(len(x)):
        buf.append(x[i])
    buf = sorted(buf)
    res = ""
    for i in range(len(buf)):
        res += buf[i]
    return int(res)


def f(x):
    return g_1(x) - g_2(x)


N, K = map(int, input().split())
a = N
for i in range(K):
    a = f(a)

print(a)
