N, M = map(int, input().split())
A = [0] * (2 * N)
for i in range(2 * N):
    A[i] = input()

people_points = [0] * (2 * N)


def decide_winner(p1, p2, round):
    p1_hand = A[p1][round]
    p2_hand = A[p2][round]
    if p1_hand == p2_hand:
        return "draw"
    if p1_hand == "G":
        if p2_hand == "C":
            return p1
        else:
            return p2
    elif p1_hand == "C":
        if p2_hand == "P":
            return p1
        else:
            return p2
    else:
        if p2_hand == "G":
            return p1
        else:
            return p2


def count_point():
    buf = set()
    for point in people_points:
        buf.add(point)
    return list(buf)


def devide_group():
    points = count_point()
    groups = {}
    for point in points:
        groups[point] = []
    for i in range(2 * N):
        groups[people_points[i]].append(i)
    return groups


def decide_rank(groups):
    rank = []
    keys = sorted(groups.keys(), reverse=True)
    for key in keys:
        rank += sorted(groups[key])
    return rank


rank = [i for i in range(2 * N)]

for i in range(M):
    for k in range(N):
        p1 = rank[2 * k]
        p2 = rank[2 * k + 1]
        winner = decide_winner(p1, p2, i)
        if winner != "draw":
            people_points[winner] += 1
    rank = decide_rank(devide_group())

for r in rank:
    print(r + 1)
