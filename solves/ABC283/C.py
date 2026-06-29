S = int(input())
T = str(S)
ans = len(T)
i = 0
while i < len(T) - 1:
    if T[i] == "0" and T[i + 1] == "0":
        ans -= 1
        i += 2
    else:
        i += 1
print(ans)
