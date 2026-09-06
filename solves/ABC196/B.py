X = input()

ans = ""
for i in range(len(X)):
    if X[i] == ".":
        break
    ans += X[i]
print(ans)
