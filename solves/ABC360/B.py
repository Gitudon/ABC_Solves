S, T = map(str, input().split())
for i in range(1, len(S)):
    buf = []
    for j in range(len(S) // i + 1):
        if j * i < len(S):
            buffa = S[j * i : j * i + i]
        else:
            buffa = S[j * i :]
        nagasa = len(buffa)
        for k in range(i - nagasa):
            buffa += "#"
        buf.append(buffa)
    for c in range(i):
        buf2 = ""
        for b in buf:
            if b[c] != "#":
                buf2 += b[c]
        if buf2 == T:
            print("Yes")
            exit()
print("No")
