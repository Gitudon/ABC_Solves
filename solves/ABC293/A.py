S = input()
T = ""
for i in range(len(S) // 2):
    T += S[2 * i + 1]
    T += S[2 * i]
print(T)
