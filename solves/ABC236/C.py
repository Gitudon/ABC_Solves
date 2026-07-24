N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

solve = {}

for t in T:
    solve[t] = 0

for i in range(N):
    if S[i] in solve:
        print("Yes")
    else:
        print("No")
