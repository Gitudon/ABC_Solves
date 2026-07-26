S = list(input())
T = list(input())

X = []
N = len(S)
i = 0
while S != T:
    if i % 2 == 0:
        for j in range(N):
            if ord(S[j]) > ord(T[j]):
                S[j] = T[j]
                X.append("".join(S))
    else:
        for j in range(1, N + 1):
            if ord(S[-j]) < ord(T[-j]):
                S[-j] = T[-j]
                X.append("".join(S))
    i += 1

print(len(X))
for x in X:
    print(x)
