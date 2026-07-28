S = input()

ans = "AC"

if S[0] != "A":
    ans = "WA"
foo = -1
count = 0
for i in range(2, len(S) - 1):
    if S[i] == "C":
        foo = i
        count += 1
if count != 1:
    ans = "WA"
for i in range(len(S)):
    if i != 0 and i != foo:
        if ord("A") <= ord(S[i]) <= ord("Z"):
            ans = "WA"

print(ans)
