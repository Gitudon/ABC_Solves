A, B, W = map(int, input().split())

W *= 1000
ans = []

kosu_max = W // A
kosu_min = W // B

for kosu in range(kosu_min, kosu_max + 1):
    weight = W / kosu
    if A <= weight <= B:
        ans.append(kosu)

if len(ans) == 0:
    print("UNSATISFIABLE")
else:
    print(min(ans), max(ans))
