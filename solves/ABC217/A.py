S, T = map(str, input().split())

ans = 0
a = len(S)
b = len(T)
c = min(a, b)
for i in range(c):
    if ord(S[i]) < ord(T[i]):
        ans += 1
        break
    elif ord(S[i]) > ord(T[i]):
        ans += 2
        break
if ans == 1:
    print("Yes")
elif ans == 2:
    print("No")
else:
    if a > b:
        print("No")
    else:
        print("Yes")
