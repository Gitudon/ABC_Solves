N = int(input())
S = [input() for _ in range(N)]
flag = True
for s in S:
    if s[0] not in ["S", "H", "D", "C"]:
        flag = False
        break
    if s[1] not in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
        flag = False
        break
    flag2 = True
S2 = list(set(S))
if len(S) != len(S2):
    flag = False
if flag:
    print("Yes")
else:
    print("No")
