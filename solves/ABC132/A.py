S = input()
a = []
for i in range(4):
    a.append(ord(S[i]))
b = sorted(a)
if b[0] == b[1] and b[2] == b[3] and b[0] != b[3]:
    print("Yes")
else:
    print("No")
