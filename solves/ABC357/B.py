S = input()

omozi = 0
komozi = 0
for i in range(len(S)):
    if S[i].islower():
        komozi += 1
    else:
        omozi += 1
if komozi >= omozi:
    print(S.lower())
else:
    print(S.upper())
