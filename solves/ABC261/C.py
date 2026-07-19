N = int(input())
namedict = {}
for i in range(N):
    S = input()
    if S in namedict:
        namedict[S] += 1
        print(S + "(" + str(namedict[S]) + ")")
    else:
        namedict[S] = 0
        print(S)
