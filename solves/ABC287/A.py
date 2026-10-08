N = int(input())
S = []
a = 0
for i in range(N):
    S.append(input())
    if S[i] == "For":
        a += 1
if a > (N / 2):
    print("Yes")
else:
    print("No")
