S = input()
a = []
for i in range(len(S) - 2):
    X = int(S[i]) * 100 + int(S[i + 1]) * 10 + int(S[i + 2])
    a.append(abs(X - 753))
print(min(a))
