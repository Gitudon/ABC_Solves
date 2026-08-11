S = input()
mozi = []
for i in range(len(S)):
    mozi.append(S[i])
mozi = list(set(mozi))
flag = True
for i in range(1, len(S) + 1):
    syurui = 0
    for m in mozi:
        cnt = 0
        for j in range(len(S)):
            if S[j] == m:
                cnt += 1
        if cnt == i:
            syurui += 1
    if syurui not in [0, 2]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
