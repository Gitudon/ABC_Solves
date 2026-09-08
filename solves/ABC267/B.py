S = input()
ans = True

if S[0] != "0":
    ans = False
else:
    ans = False
    # 全て倒れている時True
    retsu = [True] * 7
    if S[4] == "1":
        retsu[3] = False
    if S[1] == "1" or S[7] == "1":
        retsu[2] = False
    if S[2] == "1" or S[8] == "1":
        retsu[4] = False
    if S[6] == "1":
        retsu[0] = False
    if S[3] == "1":
        retsu[1] = False
    if S[5] == "1":
        retsu[5] = False
    if S[9] == "1":
        retsu[6] = False
    for i in range(7):
        for j in range(7):
            if i != j:
                if retsu[i] == False and retsu[j] == False:
                    flag = False
                    for k in range(i + 1, j):
                        if retsu[k] == True:
                            flag = True
                    if flag:
                        ans = True
if ans:
    print("Yes")
else:
    print("No")
