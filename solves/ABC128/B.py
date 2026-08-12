N = int(input())

S = [0] * N
P = [0] * N

for i in range(N):
    S[i], P[i] = map(str, input().split())
    P[i] = int(P[i])

dictionary = {}

for i in range(N):
    if S[i] not in dictionary:
        dictionary[S[i]] = [P[i]]
    else:
        dictionary[S[i]].append(P[i])

for s in dictionary:
    dictionary[s].sort(reverse=True)

cities = list(dictionary.keys())
cities.sort()

for c in cities:
    for p in dictionary[c]:
        for i in range(N):
            if P[i] == p:
                print(i + 1)
                break
