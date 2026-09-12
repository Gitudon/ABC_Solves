N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

s_dict = {}
for i in s:
    if i in s_dict:
        s_dict[i] += 1
    else:
        s_dict[i] = 1

t_dict = {}
for i in t:
    if i in t_dict:
        t_dict[i] += 1
    else:
        t_dict[i] = 1

ans = 0
for i in s_dict:
    if i in t_dict:
        ans = max(ans, s_dict[i] - t_dict[i])
    else:
        ans = max(ans, s_dict[i])

print(ans)
