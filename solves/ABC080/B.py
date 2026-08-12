N = int(input())

S = str(N)
foo = 0
for i in range(len(S)):
    foo += int(S[i])
if N % foo == 0:
    print("Yes")
else:
    print("No")
