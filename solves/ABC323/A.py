S = input()
flag = True
for i in range(16):
    if i % 2 == 1:
        if S[i] != "0":
            flag = False
if flag:
    print("Yes")
else:
    print("No")
