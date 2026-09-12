N, M = map(int, input().split())
lose = [False] * N
for i in range(M):
    A, B = map(int, input().split())
    lose[B - 1] = True
notlose = []
for i in range(N):
    if not lose[i]:
        notlose.append(i + 1)
if len(notlose) == 1:
    print(notlose[0])
else:
    print(-1)
