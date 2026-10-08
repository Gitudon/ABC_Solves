N = int(input())
S = [0] * N
T = [0] * N
for i in range(N):
    S[i], T[i] = map(str, input().split())
    T[i] = int(T[i])
U = sorted(T, reverse=True)
shigh = U[1]
for i in range(N):
    if T[i] == shigh:
        print(S[i])
