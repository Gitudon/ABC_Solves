S = input()

ans = "even"
for s in S:
    if s == "o":
        if ans == "even":
            ans = "odd"
        else:
            ans = "even"
print(ans)
