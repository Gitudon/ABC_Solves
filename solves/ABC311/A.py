N = int(input())
S = input()
A = True
B = True
C = True
i = 0
while A or B or C:
    if S[i] == "A":
        A = False
    elif S[i] == "B":
        B = False
    elif S[i] == "C":
        C = False
    i += 1
print(i)
