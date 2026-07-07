import itertools


def kaizyo(n):
    if n == 1:
        return 1
    return n * kaizyo(n - 1)


d = [0] * 3
for i in range(3):
    d[i] = list(map(int, input().split()))
c = []
for dd in d:
    for i in range(3):
        c.append(dd[i])
retsu = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

order = [0, 1, 2, 3, 4, 5, 6, 7, 8]
ans = 0
tmp = 0
for perm in itertools.permutations(order):
    boo = False
    tmp += 1
    for i in range(8):
        if (
            c[retsu[i][0]] == c[retsu[i][1]]
            and perm[retsu[i][2]] > perm[retsu[i][0]]
            and perm[retsu[i][2]] > perm[retsu[i][1]]
        ):
            boo = True
        elif (
            c[retsu[i][2]] == c[retsu[i][1]]
            and perm[retsu[i][0]] > perm[retsu[i][2]]
            and perm[retsu[i][0]] > perm[retsu[i][1]]
        ):
            boo = True
        elif (
            c[retsu[i][0]] == c[retsu[i][2]]
            and perm[retsu[i][1]] > perm[retsu[i][0]]
            and perm[retsu[i][1]] > perm[retsu[i][2]]
        ):
            boo = True
    if not boo:
        ans += 1
print(ans / tmp)
