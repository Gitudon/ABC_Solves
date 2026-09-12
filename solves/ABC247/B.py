N = int(input())
s = [0] * N
t = [0] * N
for i in range(N):
    s[i], t[i] = map(str, input().split())
ans = "Yes"
for i in range(N):
    s_flag = False
    t_flag = False
    for j in range(N):
        if i != j:
            if s[i] == s[j] or s[i] == t[j]:
                s_flag = True
    for j in range(N):
        if i != j:
            if t[i] == s[j] or t[i] == t[j]:
                t_flag = True
    if s_flag and t_flag:
        ans = "No"
        break
print(ans)
