S = input()
ans = 0
for i in range(len(S)):
    ans += ord(S[i])
if ans == 294:
    print("Yes")
else:
    print("No")
