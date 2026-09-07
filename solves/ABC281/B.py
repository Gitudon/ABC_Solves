S = input()
if (ord("A") <= ord(S[0]) <= ord("Z")) and (ord("A") <= ord(S[-1]) <= ord("Z")):
    if (S[1:-1]).isdigit() and S[1] != "0" and len((S[1:-1])) == 6:
        print("Yes")
        exit()
print("No")
