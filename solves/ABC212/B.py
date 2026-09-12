S = input()
ans = "Strong"
same = 0
for i in range(3):
    if S[i] == S[i + 1]:
        same += 1
if same == 3:
    ans = "Weak"
point = 0
for i in range(3):
    if (int(S[i]) + 1) % 10 == int(S[i + 1]):
        point += 1
if point == 3:
    ans = "Weak"
print(ans)
