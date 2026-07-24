H, W = map(int, input().split())

S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

s_elems = {}
for i in range(W):
    retsu = ""
    for j in range(H):
        retsu += S[j][i]
    if retsu not in s_elems:
        s_elems[retsu] = 0
    s_elems[retsu] += 1

t_elems = {}
for i in range(W):
    retsu = ""
    for j in range(H):
        retsu += T[j][i]
    if retsu not in t_elems:
        t_elems[retsu] = 0
    t_elems[retsu] += 1

if s_elems == t_elems:
    print("Yes")
else:
    print("No")
