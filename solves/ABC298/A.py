N = int(input())
S = input()
a = 0
b = 0
for i in range(N):
    if S[i] == "o":
        a += 1
    elif S[i] == "x":
        b += 1
if a >= 1 and b == 0:
    print("Yes")
else:
    print("No")
