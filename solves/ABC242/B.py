S = input()

S_list = sorted(S)
ans = ""
for i in range(len(S_list)):
    ans += S_list[i]
print(ans)
