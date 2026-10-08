S = input()
a = 0
i = 0
while a == 0:
    if ord("A") <= ord(S[i]) <= ord("Z"):
        print(i + 1)
        a += 1
    else:
        i += 1
