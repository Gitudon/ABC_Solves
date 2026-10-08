S = input()
num = int(S[3:])
flag = True
if 1 <= num <= 349:
    flag = True
else:
    flag = False
if num == 316:
    flag = False
if flag:
    print("Yes")
else:
    print("No")
