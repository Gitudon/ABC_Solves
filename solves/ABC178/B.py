a, b, c, d = map(int, input().split())
ac = a * c
ad = a * d
bc = b * c
bd = b * d
if ac >= ad and ac >= bc and ac >= bd:
    print(ac)
elif ad >= ac and ad >= bc and ad >= bd:
    print(ad)
elif bc >= ac and bc >= ad and bc >= bd:
    print(bc)
else:
    print(bd)
