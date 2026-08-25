S = input()

buf = ""
for i in range(len(S)):
    if S[i] == "#":
        if buf == "":
            buf += str(i + 1) + ","
        else:
            buf += str(i + 1)
            print(buf)
            buf = ""
