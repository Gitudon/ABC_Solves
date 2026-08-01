X = input()

ans = "YES"

i = len(X) - 1
while i >= 0:
    if i >= 1:
        if X[i - 1 : i + 1] == "ch":
            i -= 2
            if i < 0:
                break
    if X[i] not in ["o", "k", "u"]:
        ans = "NO"
        break
    i -= 1

print(ans)
