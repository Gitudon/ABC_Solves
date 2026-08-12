X = input()
ans = ""
flag = False
for i in range(1, len(X) + 1):
    if X[-i] == "0" and flag == False:
        if ans != "":
            ans = "0" + ans
    elif X[-i] == ".":
        flag = True
        if ans != "":
            ans = "." + ans
    else:
        ans = X[-i] + ans
print(ans)
