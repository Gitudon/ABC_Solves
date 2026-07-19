X = input()
N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()

taio = {}
for i in range(26):
    taio[X[i]] = i

S.sort(key=lambda x: [taio[c] for c in x])
for s in S:
    print(s)
