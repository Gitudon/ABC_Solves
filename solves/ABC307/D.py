N = int(input())
S = input()
T = ""
A = []
for i in range(N):
    if S[i] == "(":
        T += S[i]
        A.append(len(T) - 1)
    elif S[i] == ")":
        if A == []:
            T += S[i]
        else:
            T = T[: A[-1]]
            del A[-1]
    else:
        T += S[i]
print(T)
