for _ in range(int(input())):
    n = int(input())
    s = input()
    a = [0] * (n + 1)
    for i in reversed(range(n)):
        a[i] = a[i + 1] + (s[i] == "1")
    ans = n

    def f(l, r):
        global ans
        if l > r:
            return n
        res = r - l - 2 * (a[l] - a[r]) + a[0]
        ans = min(ans, res)
        return res

    def g(lx, rx, ly, ry):
        if lx >= rx or ly >= ry:
            return
        tyx = (lx + rx) >> 1
        best, idx = n + 1, -1
        for i in range(ly, ry):
            fval = f(tyx, i)
            if best > fval:
                best = fval
                idx = i
        g(lx, tyx, ly, idx + 1)
        g(tyx + 1, rx, idx, ry)

    g(0, n, 0, n + 1)
    print(ans)
