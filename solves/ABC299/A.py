N = int(input())
S = input()
a = -1
b = -1
for i in range(N):
    if S[i] == "|" and a == -1:
        a = i
    if S[i] == "|" and a != -1:
        b = i
T = S[a + 1 : b]
if "*" in T:
    print("in")
else:
    print("out")
