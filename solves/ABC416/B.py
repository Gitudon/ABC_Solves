S = input()

T = ["."] * len(S)
hiraki = True
for i in range(len(S)):
    if S[i] == "#":
        T[i] = "#"
        hiraki = True
    elif S[i] == ".":
        if hiraki:
            T[i] = "o"
            hiraki = False
        else:
            T[i] = "."

print("".join(T))
