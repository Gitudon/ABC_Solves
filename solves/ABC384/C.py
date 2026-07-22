from itertools import combinations

a, b, c, d, e = map(int, input().split())
point = {"A": a, "B": b, "C": c, "D": d, "E": e}
names = {}
substrings = []
for i in range(1, len("ABCDE") + 1):
    for combo in combinations("ABCDE", i):
        substrings.append("".join(combo))
for s in substrings:
    point_sum = 0
    for m in s:
        point_sum += point[m]
    names[s] = point_sum
sorted_names = sorted(names.items(), key=lambda x: x[1], reverse=True)
sorted_names = sorted(names.items(), key=lambda x: (-x[1], x[0]))
for name in sorted_names:
    print(name[0])
