S = input()

ans = "Yes"

if S != S[::-1]:
    ans = "No"

foo = S[: (len(S) - 1) // 2]
if foo != foo[::-1]:
    ans = "No"

bar = S[(len(S) + 3) // 2 - 1 :]
if bar != bar[::-1]:
    ans = "No"

print(ans)
