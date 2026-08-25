S = input()
omozi = False
for s in S:
    if ord("A") <= ord(s) <= ord("Z"):
        omozi = True
        break
komozi = False
for s in S:
    if ord("a") <= ord(s) <= ord("z"):
        komozi = True
        break
mozi = []
for s in S:
    mozi.append(s)
mozi = list(set(mozi))
if len(mozi) == len(S) and omozi and komozi:
    print("Yes")
else:
    print("No")
