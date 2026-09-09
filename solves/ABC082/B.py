s = input()
t = input()
S = []
for i in range(len(s)):
    S.append(s[i])
T = []
for i in range(len(t)):
    T.append(t[i])
S = sorted(S)
T = sorted(T, reverse=True)
s2 = ""
t2 = ""
for i in S:
    s2 += i
for j in T:
    t2 += j
if s2 < t2:
    print("Yes")
else:
    print("No")
