A, B = map(int, input().split())
S = input()

ans = "Yes"

if S[A] != "-":
    ans = "No"
if S[0:A].count("-") != 0:
    ans = "No"
if S[A + 1 :].count("-") != 0:
    ans = "No"
print(ans)
