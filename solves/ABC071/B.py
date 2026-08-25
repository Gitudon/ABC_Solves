S = input()

ans = "None"
for i in range(26):
    foo = chr(ord("a") + i)
    if foo not in S:
        ans = foo
        break
print(ans)
