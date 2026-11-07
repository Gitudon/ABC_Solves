N, M = map(int, input().split())

answers = [0] * N
penalties = [0] * N

for _ in range(M):
    p, S = map(str, input().split())
    p = int(p)
    if S == "AC":
        answers[p - 1] = 1
    else:
        if answers[p - 1] == 0:
            penalties[p - 1] += 1
penalty_points = 0
for i in range(N):
    if answers[i] == 1:
        penalty_points += penalties[i]

print(sum(answers), penalty_points)
