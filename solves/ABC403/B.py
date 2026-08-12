T = input()
U = input()

lent = len(T)
ans = "No"


def solve(t, i):
    global ans
    if i == lent:
        if U in t:
            ans = "Yes"
        return
    if T[i] == "?":
        for j in range(26):
            solve(t[:i] + chr(j + ord("a")), i + 1)
    else:
        solve(t[:i] + T[i], i + 1)


solve("", 0)
print(ans)
