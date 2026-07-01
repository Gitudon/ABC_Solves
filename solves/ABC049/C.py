S = input()
s = len(S)
i = 0
while i < s:
    if S[i : i + 11] == "dreameraser":
        i += 11
    elif S[i : i + 10] == "dreamerase":
        i += 10
    elif S[i : i + 7] == "dreamer":
        i += 7
    elif S[i : i + 6] == "eraser":
        i += 6
    elif S[i : i + 5] == "dream" or S[i : i + 5] == "erase":
        i += 5
    else:
        print("NO")
        exit()
print("YES")
