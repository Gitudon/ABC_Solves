M, D = map(int, input().split())
S = input()

watched = [False] * M

guardman = []
for i in range(M):
    if S[i] == "G":
        guardman.append(i)

for i in range(M):
    for g in guardman:
        if abs(i - g) <= D:
            watched[i] = True

print(M - sum(watched))
