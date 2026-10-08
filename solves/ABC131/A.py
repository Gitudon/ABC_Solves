S = input()
c = 0
for i in range(1, 4):
    if S[i - 1] == S[i]:
        c += 1
if c > 0:
    print("Bad")
else:
    print("Good")
