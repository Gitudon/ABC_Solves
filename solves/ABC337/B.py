S = input()
mozi = []
for i in range(len(S)):
    mozi.append(S[i])
mozi = sorted(mozi)
true = "".join(mozi)
if true == S:
    print("Yes")
else:
    print("No")
