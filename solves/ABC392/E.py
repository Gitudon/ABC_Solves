class UnionFind:
    def __init__(self, n):
        self.unicnt = [1] * n
        self.parent = list(range(n))
        self.amari = [[] for _ in range(n)]

    def ufroot(self, x):
        if self.unicnt[x] <= 0:
            self.unicnt[x] = -self.ufroot(-self.unicnt[x])
            return -self.unicnt[x]
        return x

    def ufsame(self, x, y):
        return self.ufroot(x) == self.ufroot(y)

    def uni(self, x, y):
        x = self.ufroot(x)
        y = self.ufroot(y)
        if x == y:
            return
        if self.unicnt[x] < self.unicnt[y]:
            x, y = y, x
        self.unicnt[x] += self.unicnt[y]
        self.unicnt[y] = -x
        self.amari[x].extend(self.amari[y])
        self.amari[y].clear()


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if uf.ufsame(x, y):
            uf.amari[uf.ufroot(x)].append((x, y, i))
        else:
            uf.uni(x, y)
    cc = [(len(uf.amari[i]), i) for i in range(n) if uf.ufroot(i) == i]
    cc.sort(reverse=True, key=lambda x: x[0])
    print(len(cc) - 1)
    pos = 1
    for _, root in cc:
        for x, y, i in uf.amari[root]:
            if pos < len(cc):
                print(i + 1, x + 1, cc[pos][1] + 1)
                pos += 1


if __name__ == "__main__":
    main()
