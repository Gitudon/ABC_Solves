from atcoder.dsu import DSU

n, q = map(int, input().split())
d = DSU(n + 1)
c = [0] * (n + 1)
s = [0] * (n + 1)

for _ in range(q):
    typ, *params = map(int, input().split())
    if typ == 1:
        u, v = params
        u = d.leader(u)
        v = d.leader(v)
        if u != v:
            d.merge(u, v)
            w = d.leader(u)
            s[w] = s[u] + s[v]
            s[u ^ v ^ w] = 0
    elif typ == 2:
        u = params[0]
        s[d.leader(u)] -= c[u]
        c[u] ^= 1
        s[d.leader(u)] += c[u]
    else:
        u = params[0]
        if s[d.leader(u)]:
            print("Yes")
        else:
            print("No")
