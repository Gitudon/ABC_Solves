N, W = map(int, input().split())
oisisa = set()
a_to_b = {}
for _ in range(N):
    a, b = map(int, input().split())
    oisisa.add(a)
    if a not in a_to_b:
        a_to_b[a] = 0
    a_to_b[a] += b

oisisa = sorted(oisisa, reverse=True)
ans = 0
weight = 0
for a in oisisa:
    if weight + a_to_b[a] <= W:
        weight += a_to_b[a]
        ans += a * a_to_b[a]
    else:
        ans += (W - weight) * a
        break
print(ans)
