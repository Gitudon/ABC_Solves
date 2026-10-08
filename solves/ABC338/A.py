S = input()
flag = True
if not ("A" <= S[0] <= "Z"):
    flag = False
for i in range(1, len(S)):
    if not ("a" <= S[i] <= "z"):
        flag = False
if flag:
    print("Yes")
else:
    print("No")
